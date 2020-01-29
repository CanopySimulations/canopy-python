from typing import Optional

from aiohttp.client_exceptions import ClientResponseError
import canopy
import pandas as pd
from io import StringIO
import logging

logger = logging.getLogger(__name__)


async def try_load_csv_from_url(
        session: canopy.Session,
        url: str,
        file_name: str,
        index_column_name: Optional[str]) -> Optional[pd.DataFrame]:
    try:
        async with session.async_client_session.get(url, raise_for_status=True) as response:
            text = await response.text()
            data_frame = pd.read_csv(StringIO(text), index_col=False)
            if index_column_name:
                data_frame.set_index([index_column_name], inplace=True)
            return data_frame
    except ClientResponseError as e:
        logger.warning('Failed to load file: {} ({})'.format(file_name, e.message))
        return None
