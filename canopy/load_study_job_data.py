from asyncio import Future
from threading import Thread
from typing import List, Optional

import canopy
import asyncio
import pandas as pd
import logging

logger = logging.getLogger(__name__)


async def load_study_job_data(
        session: canopy.Session,
        study_id: str,
        sim_type: str,
        channel_names: List[str],
        job_index: int = 0,
        tenant_id: str = None,
        job_access_information: canopy.swagger.BlobAccessInformation = None,
        semaphore: asyncio.Semaphore = None) -> canopy.StudyJobDataResult:

    session.authentication.authenticate()

    if tenant_id is None:
        tenant_id = session.authentication.tenant_id

    if semaphore is None:
        semaphore = asyncio.Semaphore(1)

    async with semaphore:
        logger.info('Loading job index %d', job_index)
        study_api = canopy.swagger.StudyApi(session.async_client)

        job_result_task = asyncio.ensure_future(study_api.study_get_study_job_metadata(
            tenant_id,
            study_id,
            job_index))

        job_result: Optional[canopy.swagger.GetStudyJobMetadataQueryResult] = None

        if job_access_information is None:
            job_result = await job_result_task
            job_access_information = job_result.access_information
        else:
            # Add job index to URL
            job_access_information = canopy.swagger.BlobAccessInformation(
                ''.join([job_access_information.url, str(job_index), '/']),
                job_access_information.access_signature)

        vector_metadata = await canopy.load_vector_metadata(job_access_information, sim_type)

        channels_data = {}
        channels_units = {}

        if vector_metadata is not None:
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
                    channels_data[channel_name] = loaded_channel.data
                    channels_units[channel_name] = loaded_channel.units

        channels_data_frame = pd.DataFrame(channels_data)

        if job_result is None:
            job_result = await job_result_task

        return canopy.StudyJobDataResult(job_result.study_job, channels_data_frame, channels_units)
