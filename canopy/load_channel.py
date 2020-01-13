from typing import Optional

import numpy as np
import canopy
import logging

logger = logging.getLogger(__name__)


def load_channel(
        session: canopy.Session,
        job_url: str,
        sas: str,
        sim_type: str,
        channel_name: str,
        vector_metadata=None) -> Optional[canopy.LoadedChannel]:

    if vector_metadata is None:
        vector_metadata = canopy.load_vector_metadata(job_url, sas, sim_type)

    if vector_metadata is None:
        return None

    if channel_name not in vector_metadata.index:
        logger.warning('Channel not found: %s', channel_name)
        return None

    channel_metadata = vector_metadata.xs(channel_name)

    points_count: int = channel_metadata['NPtsInChannel']
    units: str = channel_metadata['units']

    channel_url = ''.join([job_url, sim_type, '_', channel_name, '.bin', sas])
    channel_result = session.client.rest_client.pool_manager.request('GET', channel_url)
    if points_count * 4 == len(channel_result.data):
        data_type = np.float32
    else:
        data_type = np.float64

    channel_data: np.array = np.frombuffer(channel_result.data, data_type)

    desired_units = session.user_settings.get_channel_units(channel_name)
    if desired_units is not None:
        session.units.convert_values_from_si(channel_data, desired_units)
        units = desired_units

    if units == '()':
        units = ''

    loaded_channel = canopy.LoadedChannel(channel_name, units, channel_data)
    return loaded_channel
