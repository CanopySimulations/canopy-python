import asyncio
from asyncio import Future
from typing import List, Optional

import canopy
import logging

logger = logging.getLogger(__name__)


async def load_study(
        session: canopy.Session,
        study_id: str,
        sim_type: Optional[str] = None,
        channel_names: Optional[List[str]] = None,
        tenant_id: Optional[str] = None,
        include_inputs: bool = False,
        include_scalar_results: bool = False,
        sim_version: Optional[str] = None) -> canopy.StudyDataResult:

    session.authentication.authenticate()

    if tenant_id is None:
        tenant_id = session.authentication.tenant_id

    study_api = canopy.swagger.StudyApi(session.async_client)
    study_result: canopy.swagger.GetStudyQueryResult = await study_api.study_get_study_metadata(tenant_id, study_id)

    access_information: canopy.swagger.StudyBlobAccessInformation = study_result.access_information
    jobs_access_information: List[canopy.swagger.BlobAccessInformation] = access_information.jobs
    study_document = canopy.get_study_document(session, study_result.study)

    semaphore = asyncio.Semaphore(session.default_api_concurrency)

    job_tasks: List[Future[canopy.StudyJobDataResult]] = []
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
            include_inputs=include_inputs,
            include_scalar_results=include_scalar_results,
            sim_version=sim_version))
        job_tasks.append(job_task)

    jobs: List[canopy.StudyJobDataResult] = await asyncio.gather(*job_tasks)

    return canopy.StudyDataResult(session, study_result, jobs)
