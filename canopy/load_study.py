import asyncio
from asyncio import Future
from typing import List, Optional, Sequence

import canopy
import logging

logger = logging.getLogger(__name__)


async def load_study(
        session: canopy.Session,
        study_id: str,
        sim_type: Optional[str] = None,
        channel_names: Optional[List[str]] = None,
        tenant_id: Optional[str] = None,
        include_study_sim_types: bool = False,
        include_study_full_document: bool = False,
        include_study_inputs: bool = False,
        include_study_scalar_results: bool = False,
        include_job_metadata: bool = False,
        include_job_inputs: bool = False,
        include_job_full_document: bool = False,
        include_job_scalar_results: bool = False,
        include_job_vector_metadata: bool = False,
        sim_version: Optional[str] = None) -> canopy.StudyResult:

    sim_type = canopy.ensure_sim_type_string(sim_type)

    session.authentication.authenticate()

    if tenant_id is None:
        tenant_id = session.authentication.tenant_id

    study_api = canopy.openapi.StudyApi(session.async_client)

    study_result: canopy.openapi.GetStudyQueryResult
    if include_study_inputs or include_study_sim_types or include_study_full_document:
        study_result = await study_api.study_get_study(tenant_id, study_id)
    else:
        study_result = await study_api.study_get_study_metadata(tenant_id, study_id)

    access_information: canopy.openapi.StudyBlobAccessInformation = study_result.access_information
    jobs_access_information: List[canopy.openapi.BlobAccessInformation] = access_information.jobs
    study_document = canopy.get_study_document(session, study_result.study)

    scalar_results_task: Optional[Future[canopy.StudyScalarResults]] = None
    if include_study_scalar_results:
        scalar_results_task = asyncio.ensure_future(canopy.load_study_scalar_results(
            session,
            access_information))

    semaphore = asyncio.Semaphore(session.default_api_concurrency)

    jobs: Optional[Sequence[canopy.StudyJobResult]] = None
    if include_job_metadata \
            or include_job_inputs \
            or include_job_scalar_results \
            or include_job_vector_metadata \
            or (channel_names is not None and len(channel_names) > 0):

        job_tasks: List[Future[canopy.StudyJobResult]] = []
        for index in range(canopy.job_count_to_simulation_count(study_document.job_count)):
            job_task = asyncio.ensure_future(canopy.load_study_job(
                session,
                study_id,
                sim_type,
                channel_names,
                index,
                tenant_id=tenant_id,
                job_access_information=jobs_access_information[index % len(jobs_access_information)],
                semaphore=semaphore,
                include_inputs=include_job_inputs,
                include_full_document=include_job_full_document,
                include_scalar_results=include_job_scalar_results,
                include_vector_metadata=include_job_vector_metadata,
                sim_version=sim_version))
            job_tasks.append(job_task)
        jobs = await asyncio.gather(*job_tasks)

    scalar_results: Optional[canopy.StudyScalarResults] = None
    if scalar_results_task is not None:
        scalar_results = await scalar_results_task

    return canopy.StudyResult(session, study_result, jobs, scalar_results=scalar_results)
