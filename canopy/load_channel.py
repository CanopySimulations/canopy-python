from threading import Thread
from typing import Optional, Union

import numpy as np
import canopy
import logging
import asyncio

logger = logging.getLogger(__name__)


async def load_channel(
        session: canopy.Session,
        job_access_information: canopy.swagger.BlobAccessInformation,
        sim_type: str,
        channel_name: str,
        vector_metadata=None,
        semaphore: asyncio.Semaphore = None) -> Optional[canopy.LoadedChannel]:

    if semaphore is None:
        semaphore = asyncio.Semaphore(1)

    async with semaphore:
        if vector_metadata is None:
            vector_metadata = await canopy.load_vector_metadata(job_access_information, sim_type)

        if vector_metadata is None:
            return None

        if channel_name not in vector_metadata.index:
            logger.debug('Channel not found: %s', channel_name)
            return None

        channel_metadata = vector_metadata.xs(channel_name)

        points_count: int = channel_metadata['NPtsInChannel']
        units: str = channel_metadata['units']

        channel_url = ''.join([job_access_information.url, sim_type, '_', channel_name, '.bin', job_access_information.access_signature])

        async with session.async_client_session.get(channel_url) as response:
            channel_bytes = await response.read()
            if points_count * 4 == len(channel_bytes):
                data_type = np.float32
            else:
                data_type = np.float64
            channel_data: np.array = np.frombuffer(channel_bytes, data_type)

            if units == '()':
                units = ''

            loaded_channel = canopy.LoadedChannel(channel_name, units, channel_data)
            return loaded_channel
