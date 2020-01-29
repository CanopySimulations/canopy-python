from typing import Optional, Sequence

import pandas as pd
import logging

logger = logging.getLogger(__name__)

units_column_names = ['units']


def process_data_frame(
        data_frame: Optional[pd.DataFrame],
        index_column_name: Optional[str] = None,
        empty_string_valid_column_names: Optional[Sequence[str]] = None) -> Optional[pd.DataFrame]:

    if data_frame is None:
        return

    if index_column_name is not None:
        data_frame.set_index([index_column_name], inplace=True)

    columns = data_frame.columns

    empty_string_valid_column_names_set = set(units_column_names)
    if empty_string_valid_column_names is not None:
        empty_string_valid_column_names_set.update(empty_string_valid_column_names)

    # When using pandas.read_csv it will set empty strings to NaN, so here we
    # force them to empty strings if requested.
    for column_name in empty_string_valid_column_names_set:
        if column_name in columns:
            data_frame[column_name] = data_frame[column_name].fillna('')

    for column_name in units_column_names:
        if column_name in columns:
            data_frame[column_name] = data_frame[column_name].replace('()', '')

    return data_frame
