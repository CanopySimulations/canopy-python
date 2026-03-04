from typing import List, Optional
import numpy as np
import pandas as pd
import canopy
import logging
import asyncio

logger = logging.getLogger(__name__)


async def load_channels(
        session: canopy.Session,
        job_access_information: canopy.openapi.BlobAccessInformation,
        sim_type: str,
        channel_names: List[str],
        vector_metadata: Optional[pd.DataFrame] = None,
        semaphore: Optional[asyncio.Semaphore] = None) -> List[Optional[canopy.LoadedChannel]]:
    sim_type = canopy.ensure_sim_type_string(sim_type)

    if semaphore is None:
        semaphore = asyncio.Semaphore(session.default_blob_storage_concurrency)

    if vector_metadata is None:
        vector_metadata = await canopy.load_vector_metadata(session, job_access_information, sim_type)

    if vector_metadata is None:
        return [None] * len(channel_names)

    async def _load_channel(channel_name: str) -> Optional[canopy.LoadedChannel]:
        async with semaphore:
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

    tasks = [asyncio.ensure_future(_load_channel(name)) for name in channel_names]
    return await asyncio.gather(*tasks)


async def load_channel(
        session: canopy.Session,
        job_access_information: canopy.openapi.BlobAccessInformation,
        sim_type: str,
        channel_name: str,
        vector_metadata: Optional[pd.DataFrame] = None,
        semaphore: Optional[asyncio.Semaphore] = None) -> Optional[canopy.LoadedChannel]:
    results = await load_channels(
        session,
        job_access_information,
        sim_type,
        [channel_name],
        vector_metadata=vector_metadata,
        semaphore=semaphore)
    return results[0]
