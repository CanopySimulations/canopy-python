from threading import Thread
from typing import Optional, Union
from aiohttp.client_exceptions import ClientResponseError, ClientConnectionError, ServerTimeoutError, ClientError

import numpy as np
import pandas as pd
import canopy
import logging
import asyncio

logger = logging.getLogger(__name__)


async def load_channel(
        session: canopy.Session,
        job_access_information: canopy.openapi.BlobAccessInformation,
        sim_type: str,
        channel_name: str,
        vector_metadata: Optional[pd.DataFrame] = None,
        semaphore: Optional[asyncio.Semaphore] = None) -> Optional[canopy.LoadedChannel]:
    sim_type = canopy.ensure_sim_type_string(sim_type)

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

        channel_bytes: Optional[bytes] = await session.try_load_bytes(
            channel_url,
            f'"{file_name}" from "{job_access_information.url}"')

        if channel_bytes is None:
            return None

        if points_count * 4 == len(channel_bytes):
            data_type = np.float32
        else:
            data_type = np.float64
        channel_data: np.array = np.frombuffer(channel_bytes, data_type)

        loaded_channel = canopy.LoadedChannel(channel_name, units, channel_data)
        return loaded_channel


async def read_channel_data(channel_url: str, session: canopy.Session) -> bytes:
    async with session.async_client_session.get(
            channel_url,
            raise_for_status=True,
            proxy=session.configuration.proxy) as response:
        return await response.read()
