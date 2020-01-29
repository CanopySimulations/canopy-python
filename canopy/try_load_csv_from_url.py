from typing import Optional, Sequence

from aiohttp.client_exceptions import ClientResponseError
import canopy
import pandas as pd
from io import StringIO
import logging

logger = logging.getLogger(__name__)

units_column_names = ['units']


async def try_load_csv_from_url(
        session: canopy.Session,
        url: str,
        file_name: str,
        index_column_name: Optional[str] = None,
        empty_string_valid_column_names: Optional[Sequence[str]] = None) -> Optional[pd.DataFrame]:
    try:
        async with session.async_client_session.get(url, raise_for_status=True) as response:
            text = await response.text()
            data_frame = pd.read_csv(StringIO(text), index_col=False)

            canopy.process_data_frame(data_frame, index_column_name, empty_string_valid_column_names)

            return data_frame
    except ClientResponseError as e:
        logger.warning('Failed to load file: {} ({})'.format(file_name, e.message))
        return None
