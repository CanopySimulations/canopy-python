from asyncio import Future
from typing import List, Optional, Any, Dict

import canopy
import asyncio
import pandas as pd
import logging

logger = logging.getLogger(__name__)


async def load_study_job(
        session: canopy.Session,
        study_id: str,
        sim_type: Optional[str] = None,
        channel_names: Optional[List[str]] = None,
        job_index: int = 0,
        tenant_id: str = None,
        job_access_information: canopy.openapi.BlobAccessInformation = None,
        semaphore: asyncio.Semaphore = None,
        include_inputs: bool = False,
        include_full_document: bool = False,
        include_scalar_results: bool = False,
        include_vector_metadata: bool = False,
        sim_version: Optional[str] = None) -> canopy.StudyJobResult:

    sim_type = canopy.ensure_sim_type_string(sim_type)

    session.authentication.authenticate()

    if tenant_id is None:
        tenant_id = session.authentication.tenant_id

    if semaphore is None:
        semaphore = asyncio.Semaphore(1)

    async with semaphore:
        logger.info('Loading job index %d', job_index)
        study_api = canopy.openapi.StudyApi(session.async_client)

        job_result_task = asyncio.ensure_future(
            study_api.study_get_study_job_metadata(
                tenant_id,
                study_id,
                job_index)
            if not include_inputs and not include_full_document else
            study_api.study_get_study_job(
                tenant_id,
                study_id,
                job_index,
                **canopy.defined_kwargs(
                    sim_version=sim_version)))

        job_result: Optional[canopy.openapi.GetStudyJobQueryResult] = None

        if job_access_information is None:
            job_result = await job_result_task
            job_access_information = job_result.access_information
        else:
            # Add job index to URL
            job_access_information = canopy.openapi.BlobAccessInformation(
                ''.join([job_access_information.url, str(job_index), '/']),
                job_access_information.access_signature)

        scalar_results_task: Optional[Future[Optional[pd.DataFrame]]] = None
        if include_scalar_results:
            if sim_type is None:
                raise RuntimeError('Sim type must be supplied when fetching scalar results.')

            scalar_results_task = asyncio.ensure_future(canopy.load_study_job_scalar_results(
                session,
                job_access_information,
                sim_type))

        channels_data = {}
        vector_units = {}
        vector_metadata: Optional[pd.DataFrame] = None

        if include_vector_metadata or (channel_names is not None and len(channel_names) > 0):
            if sim_type is None:
                raise RuntimeError('Sim type must be supplied when fetching channel data or vector metadata.')

            vector_metadata = await canopy.load_vector_metadata(session, job_access_information, sim_type)

            if vector_metadata is not None and channel_names is not None:
                channels_semaphore = asyncio.Semaphore(session.default_blob_storage_concurrency)
                tasks: List[Future[Optional[canopy.LoadedChannel]]] = []
                for channel_name in channel_names:
                    loaded_channel_task = asyncio.ensure_future(canopy.load_channel(
                        session,
                        job_access_information,
                        sim_type,
                        channel_name,
                        vector_metadata=vector_metadata,
                        semaphore=channels_semaphore))

                    tasks.append(loaded_channel_task)

                for channel_name, task in zip(channel_names, tasks):
                    loaded_channel = await task
                    if loaded_channel is not None:
                        # Convert to a series, which allows the DataFrame to pad with NaNs if
                        # channels happen to be different lengths.
                        channels_data[channel_name] = pd.Series(loaded_channel.data)
                        vector_units[channel_name] = loaded_channel.units

        vector_data = pd.DataFrame(channels_data)

        if job_result is None:
            job_result = await job_result_task

        scalar_data: Dict[str, float] = {}
        scalar_units: Dict[str, str] = {}
        if scalar_results_task is not None:
            scalar_results = await scalar_results_task
            if scalar_results is not None:
                scalar_data = dict(scalar_results['value'])
                scalar_units = dict(scalar_results['units'])

        job_inputs: Optional[Dict[str, Dict]] = None
        if include_inputs:
            job_inputs = canopy.ensure_dict(job_result.study_job_input)['simConfig']

        return canopy.StudyJobResult(
            session,
            job_result,
            job_result.study_job,
            vector_metadata,
            vector_data,
            vector_units,
            scalar_data,
            scalar_units,
            job_inputs)
