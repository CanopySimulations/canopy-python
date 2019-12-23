import numpy as np
import canopy


def load_channel(session, job_url, sas, sim_type, channel_name, vector_metadata=None):

    if vector_metadata is None:
        vector_metadata = canopy.load_vector_metadata(job_url, sas, sim_type)

    if vector_metadata is None:
        return None

    if channel_name not in vector_metadata.index:
        print('Channel not found: ' + channel_name)
        return None

    channel_metadata = vector_metadata.xs(channel_name)

    points_count = channel_metadata['NPtsInChannel']
    units = channel_metadata['units']
    if units == '()':
        units = ''

    channel_url = ''.join([job_url, sim_type, '_', channel_name, '.bin', sas])
    channel_result = session.client.rest_client.pool_manager.request('GET', channel_url)
    if points_count * 4 == len(channel_result.data):
        data_type = np.float32
    else:
        data_type = np.float64

    channel_data = np.frombuffer(channel_result.data, data_type)
    loaded_channel = canopy.LoadedChannel(channel_name, units, channel_data)
    return loaded_channel
