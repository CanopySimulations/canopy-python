from threading import Thread
from typing import Optional, Union
from aiohttp.client_exceptions import ClientResponseError

import numpy as np
import pandas as pd
import canopy
import logging
import asyncio

logger = logging.getLogger(__name__)


async def load_channel(
        session: canopy.Session,
        job_access_information: canopy.swagger.BlobAccessInformation,
        sim_type: str,
        channel_name: str,
        vector_metadata: Optional[pd.DataFrame] = None,
        semaphore: Optional[asyncio.Semaphore] = None) -> Optional[canopy.LoadedChannel]:

    if semaphore is None:
        semaphore = asyncio.Semaphore(1)

    async with semaphore:
        if vector_metadata is None:
            vector_metadata = await canopy.load_vector_metadata(session, job_access_information, sim_type)

        if vector_metadata is None:
            return None

        if channel_name not in vector_metadata.index:
            logger.debug('Channel not found: %s', channel_name)
            return None

        channel_metadata = vector_metadata.xs(channel_name)

        points_count: int = channel_metadata['NPtsInChannel']
        units: str = channel_metadata['units']

        file_name = ''.join([sim_type, '_', channel_name, '.bin'])
        channel_url = ''.join([job_access_information.url, file_name, job_access_information.access_signature])

        try:
            async with session.async_client_session.get(channel_url, raise_for_status=True) as response:
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
        except ClientResponseError as e:
            logger.warning('Channel found in metadata but could not be loaded: {} ({})'.format(file_name, e.message))
            return None
