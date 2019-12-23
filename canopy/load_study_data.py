from __future__ import absolute_import

import swagger_client
import canopy

def load_study_data(session, study_id, sim_type, channel_names, tenant_id=None):
    session.authenticate()

    if tenant_id is None:
        tenant_id = session.tenant_id

    study_api = swagger_client.StudyApi(session.client)
    study_result = study_api.study_get_study_metadata(tenant_id, study_id)

    jobs = []
    study_document = canopy.get_study_document(session, study_result.study)
    for index in range(canopy.job_count_to_simulation_count(study_document.job_count)):
        print(''.join(['Loading job index ', str(index)]))
        job = canopy.load_study_job_data(session, study_id, sim_type, channel_names, index, tenant_id=tenant_id)
        jobs.append(job)

    return canopy.StudyDataResult(study_result.study, jobs)
