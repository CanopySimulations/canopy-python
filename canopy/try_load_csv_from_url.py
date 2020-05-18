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

    text: Optional[str] = await session.try_load_text(url, file_name)
    if text is None:
        return None

    data_frame = pd.read_csv(StringIO(text), index_col=False)
    canopy.process_data_frame(data_frame, index_column_name, empty_string_valid_column_names)
    return data_frame
