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
    # We group channels by their x-domain to load from the correct parquet files.
    parquet_results = {}
    
    channels_by_x_domain = {}
    for name in channel_names:
        if name in vector_metadata.index:
            x_domain = vector_metadata.at[name, 'xDomainName']
            if pd.isna(x_domain) or not x_domain:
                continue
            
            if x_domain not in channels_by_x_domain:
                channels_by_x_domain[x_domain] = []
            channels_by_x_domain[x_domain].append(name)

    # Try loading from parquet for each x-domain
    for x_domain, domain_channels in channels_by_x_domain.items():
        loaded_from_parquet = await _try_load_channels_from_parquet(
            job_access_information,
            sim_type,
            x_domain,
            domain_channels,
            vector_metadata)
        
        if loaded_from_parquet:
            for channel in loaded_from_parquet:
                if channel is not None:
                    parquet_results[channel.name] = channel

    async def _load_channel(channel_name: str) -> Optional[canopy.LoadedChannel]:
        if channel_name in parquet_results:
            return parquet_results[channel_name]

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

async def _try_load_channels_from_parquet(
        job_access_information: canopy.openapi.BlobAccessInformation,
        sim_type: str,
        x_domain: str,
        channel_names: List[str],
        vector_metadata: pd.DataFrame) -> Optional[List[Optional[canopy.LoadedChannel]]]:
    file_name = f'{sim_type}_{x_domain}_VectorResults.parquet'
    url = f'{job_access_information.url}{file_name}{job_access_information.access_signature}'

    try:
        # We'll use a single scan for all requested channels that exist in metadata.
        valid_channels = [name for name in channel_names if name in vector_metadata.index]
        if not valid_channels:
            return None

        lf = pl.scan_parquet(url, storage_options={ "max_retries": 1, "retry_timeout_ms": 100 })
        
        # Check which columns actually exist in the parquet
        schema = await asyncio.to_thread(lf.collect_schema)
        available_columns = schema.names()
        requested_available = [name for name in valid_channels if name in available_columns]
        
        if not requested_available:
            return None

        # Fetch all required columns in one go
        df: pl.DataFrame = await lf.select(requested_available).collect_async()
        
        results: List[Optional[canopy.LoadedChannel]] = []
        for name in channel_names:
            if name in requested_available:
                data: np.ndarray = df.get_column(name).to_numpy()
                units: str = str(vector_metadata.at[name, 'units'])
                results.append(canopy.LoadedChannel(name, units, data))
            else:
                results.append(None)
        
        return results
    except Exception as e:
        logger.debug(f"Failed to load channels from parquet {file_name}: {e}")
        return None
