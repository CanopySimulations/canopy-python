from __future__ import absolute_import

import swagger_client
import pandas as pd
import numpy as np


def load_study_data(api, study_id, sim_type, channel_names, job_index=0, tenant_id=None):
    api.authenticate()

    if tenant_id is None:
        tenant_id = api.tenant_id

    study_api = swagger_client.StudyApi(api.client)
    job_result = study_api.study_get_study_job_metadata(tenant_id, study_id, job_index)

    job_url = job_result.access_information.url
    sas = job_result.access_information.access_signature

    vector_metadata_url = ''.join([job_url, sim_type, '_VectorMetadata.csv', sas])
    vector_metadata = pd.read_csv(vector_metadata_url, index_col=False)
    vector_metadata.set_index(['name'], inplace=True)

    channels = []
    for channel_name in channel_names:
        if channel_name not in vector_metadata.index:
            print('Channel not found: ' + channel_name)
            continue

        channel_metadata = vector_metadata.xs(channel_name)

        points_count = channel_metadata['NPtsInChannel']
        units = channel_metadata['units']
        if units == '()':
            units = ''

        channel_url = ''.join([job_url, sim_type, '_', channel_name, '.bin', sas]);
        channel_result = api.client.rest_client.pool_manager.request('GET', channel_url)
        if points_count * 4 == len(channel_result.data):
            data_type = np.float32
        else:
            data_type = np.float64

        channel_data = np.frombuffer(channel_result.data, data_type)
        channels.append(Channel(channel_name, units, channel_data))

    return StudyJobDataResult(job_result, channels)


class StudyJobDataResult:
    def __init__(self, job, channels):
        self.job = job
        self.channels = channels


class Channel:
    def __init__(self, name, units, data):
        self.name = name
        self.units = units
        self.data = data