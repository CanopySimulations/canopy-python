from __future__ import absolute_import

from typing import List, Optional

import canopy
import logging

logger = logging.getLogger(__name__)


def load_study_data(
        session: canopy.Session,
        study_id: str,
        sim_type: str,
        channel_names: List[str],
        tenant_id: Optional[str] = None) -> canopy.StudyDataResult:
    session.authentication.authenticate()

    if tenant_id is None:
        tenant_id = session.authentication.tenant_id

    study_api = canopy.swagger.StudyApi(session.client)
    study_result: canopy.swagger.GetStudyQueryResult = study_api.study_get_study_metadata(tenant_id, study_id)

    jobs = []
    study_document = canopy.get_study_document(session, study_result.study)
    for index in range(canopy.job_count_to_simulation_count(study_document.job_count)):
        logger.info('Loading job index %d', index)
        job = canopy.load_study_job_data(session, study_id, sim_type, channel_names, index, tenant_id=tenant_id)
        jobs.append(job)

    return canopy.StudyDataResult(study_result.study, jobs)
