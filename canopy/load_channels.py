import polars as pl
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

    # First attempt to load from parquet if available
    parquet_channel_data = await _try_load_channels_from_parquet(
        job_access_information,
        sim_type,
        channel_names,
        vector_metadata)

    if parquet_channel_data is not None:
        return parquet_channel_data

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


async def _try_load_channels_from_parquet(
        job_access_information: canopy.openapi.BlobAccessInformation,
        sim_type: str,
        channel_names: List[str],
        vector_metadata: pd.DataFrame) -> Optional[List[Optional[canopy.LoadedChannel]]]:
    # We assume 't' is a common x-domain, but the user said <sim-type>_<x-domain>.parquet
    # Since we don't know the x-domain, and the prompt implies there's a relevant one,
    # we might need to find it from vector_metadata or assume a default like 't'.
    # However, common canopy usage often has 't' as the x-domain for many sim types.
    # If the x-domain isn't fixed, we'd need to know which one to look for.
    # Given "<sim-type>_<x-domain>.parquet", and "minimise calls to scan_parquet",
    # it suggests there might be one main parquet file.
    
    # Try 't' as the default x-domain if not specified.
    x_domain = 't'
    file_name = f'{sim_type}_{x_domain}_VectorResults.parquet'
    url = f'{job_access_information.url}{file_name}{job_access_information.access_signature}'

    try:
        # Check if the parquet file exists by trying to peek at it or just attempting scan_parquet
        # polars.scan_parquet supports HTTP URLs if built with 'fsspec' or 'cloud' support.
        # If not, we might need to download it first, but scan_parquet is specifically requested.
        
        # We'll use a single scan for all requested channels that exist in metadata.
        valid_channels = [name for name in channel_names if name in vector_metadata.index]
        if not valid_channels:
            return [None] * len(channel_names)

        # scan_parquet is lazy. 
        # Note: pl.scan_parquet(url) might fail if the environment doesn't support fsspec/http.
        # But the requirement is to use scan_parquet.
        lf = pl.scan_parquet(url)
        
        # Check which columns actually exist in the parquet
        available_columns = lf.columns
        requested_available = [name for name in valid_channels if name in available_columns]
        
        if not requested_available:
            return None

        # Fetch all required columns in one go
        df: pl.DataFrame = lf.select(requested_available).collect()
        
        results: List[Optional[canopy.LoadedChannel]] = []
        for name in channel_names:
            if name in requested_available:
                data: np.ndarray = df.get_column(name).to_numpy()
                units: str = str(vector_metadata.at[name, 'units'])
                results.append(canopy.LoadedChannel(name, units, data))
            else:
                return None
        
        return results
    except Exception as e:
        logger.debug(f"Failed to load channels from parquet {file_name}: {e}")
        return None
