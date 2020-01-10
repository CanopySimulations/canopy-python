from typing import List

import swagger_client
import canopy
import pandas as pd


def load_study_job_data(
        session: canopy.Session,
        study_id: str,
        sim_type: str,
        channel_names: List[str],
        job_index: int = 0,
        tenant_id: str = None) -> canopy.StudyJobDataResult:
    session.authenticate()

    if tenant_id is None:
        tenant_id = session.tenant_id

    study_api = swagger_client.StudyApi(session.client)
    job_result: swagger_client.GetStudyJobMetadataQueryResult = study_api.study_get_study_job_metadata(tenant_id, study_id, job_index)

    job_url = job_result.access_information.url
    sas = job_result.access_information.access_signature
    vector_metadata = canopy.load_vector_metadata(job_url, sas, sim_type)

    channels_data = {}
    channels_units = {}

    if vector_metadata is not None:
        for channel_name in channel_names:
            loaded_channel = canopy.load_channel(session, job_url, sas, sim_type, channel_name, vector_metadata=vector_metadata)
            if loaded_channel is not None:
                channels_data[channel_name] = loaded_channel.data
                channels_units[channel_name] = loaded_channel.units

    channels_data_frame = pd.DataFrame(channels_data)

    return canopy.StudyJobDataResult(job_result.study_job, channels_data_frame, channels_units)
