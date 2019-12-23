import swagger_client
import canopy


def load_study_job_data(session, study_id, sim_type, channel_names, job_index=0, tenant_id=None):
    session.authenticate()

    if tenant_id is None:
        tenant_id = session.tenant_id

    study_api = swagger_client.StudyApi(session.client)
    job_result = study_api.study_get_study_job_metadata(tenant_id, study_id, job_index)

    job_url = job_result.access_information.url
    sas = job_result.access_information.access_signature
    vector_metadata = canopy.load_vector_metadata(job_url, sas, sim_type)

    if vector_metadata is None:
        return None

    channels = {}
    for channel_name in channel_names:
        loaded_channel = canopy.load_channel(session, job_url, sas, sim_type, channel_name, vector_metadata=vector_metadata)
        if loaded_channel is not None:
            channels[channel_name] = loaded_channel

    return canopy.StudyJobDataResult(job_result.study_job, channels)