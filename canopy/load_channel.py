from threading import Thread
from typing import Optional, Union

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
        vector_metadata=None,
        async_req=None) -> Optional[Union[canopy.LoadedChannel, Thread]]:

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

    desired_units = session.user_settings.get_channel_units(channel_name)

    if not async_req:
        return _load_channel_inner(channel_name, channel_url, points_count, session, units, desired_units)
    else:
        return session.client.pool.apply_async(_load_channel_inner, (channel_name, channel_url, points_count, session, units, desired_units))


def _load_channel_inner(
        channel_name: str,
        channel_url: str,
        points_count: int,
        session: canopy.Session,
        units: str,
        desired_units: Optional[str]) -> canopy.LoadedChannel:
    print('Loading %s', channel_name)
    channel_result = session.client.rest_client.pool_manager.request('GET', channel_url)
    if points_count * 4 == len(channel_result.data):
        data_type = np.float32
    else:
        data_type = np.float64
    channel_data: np.array = np.frombuffer(channel_result.data, data_type)
    if desired_units is not None:
        session.units.convert_values_from_si(channel_data, desired_units)
        units = desired_units
    if units == '()':
        units = ''
    loaded_channel = canopy.LoadedChannel(channel_name, units, channel_data)
    print('Loaded %s', channel_name)
    return loaded_channel
