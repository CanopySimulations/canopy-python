from typing import Optional

import canopy
import asyncio
import time


async def wait_for_study(
        session: canopy.Session,
        study_id: str,
        tenant_id: Optional[str] = None,
        timeout_seconds: float = 0) -> canopy.StudyResult:

    session.authentication.authenticate()

    if tenant_id is None:
        tenant_id = session.authentication.tenant_id

    study_api = canopy.openapi.StudyApi(session.async_client)

    start_time = time.monotonic()
    while True:
        study_result: canopy.openapi.GetStudyQueryResult = await study_api.study_get_study_metadata(tenant_id, study_id)
        study_document = canopy.get_study_document(session, study_result.study)

        if study_document.completed_job_count == study_document.job_count:
            break

        current_time = time.monotonic()
        elapsed_time = current_time - start_time

        if timeout_seconds > 0 and elapsed_time > timeout_seconds:
            raise TimeoutError('Timed out waiting for study to complete. Process is {}/{} jobs complete.'.format(
                study_document.completed_job_count,
                study_document.job_count))

        await asyncio.sleep(_get_sleep_time_seconds(elapsed_time))

    return canopy.StudyResult(
        session,
        study_result,
        [])


def _get_sleep_time_seconds(current_duration_seconds: float):
    if current_duration_seconds < 30:
        return 3
    elif current_duration_seconds < 150:
        return 6
    elif current_duration_seconds < 300:
        return 15
    return 30
