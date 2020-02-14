from typing import Optional, Sequence, Dict

import canopy
import pandas as pd
import logging
import asyncio

logger = logging.getLogger(__name__)


async def load_study_scalar_results(
        session: canopy.Session,
        study_access_information: canopy.openapi.StudyBlobAccessInformation) -> canopy.StudyScalarResults:

    inputs_task = asyncio.ensure_future(
        _load_file(session, 'scalar-inputs.csv', None, None, study_access_information))

    inputs_metadata_task = asyncio.ensure_future(
        _load_file(session, 'scalar-inputs-metadata.csv', 'inputName', ['units', 'description'], study_access_information))

    results_task = asyncio.ensure_future(
        _load_file(session, 'scalar-results.csv', None, None, study_access_information))

    results_metadata_task = asyncio.ensure_future(
        _load_file(session, 'scalar-metadata.csv', None, ['units', 'description'], study_access_information))

    inputs = await inputs_task
    inputs_metadata = await inputs_metadata_task
    results = await results_task
    results_metadata = await results_metadata_task

    if results_metadata is not None:
        results_metadata['fullName'] = results_metadata['name'] + ':' + results_metadata['simType']
        results_metadata.set_index(['fullName'], inplace=True)

    units: Dict[str, str] = {}
    if inputs_metadata is not None:
        for input_name in inputs_metadata.index:
            units[input_name] = inputs_metadata.loc[input_name]['units']
    if results_metadata is not None:
        for input_name in results_metadata.index:
            units[input_name] = results_metadata.loc[input_name]['units']

    return canopy.StudyScalarResults(
        inputs,
        inputs_metadata,
        results,
        results_metadata,
        units)


async def _load_file(
        session: canopy.Session,
        file_name: str,
        index_column_name: Optional[str],
        empty_string_valid_column_names: Optional[Sequence[str]],
        study_access_information: canopy.openapi.StudyBlobAccessInformation) -> Optional[pd.DataFrame]:

    url = ''.join([study_access_information.url, file_name, study_access_information.access_signature])
    return await canopy.try_load_csv_from_url(
        session,
        url,
        file_name,
        index_column_name=index_column_name,
        empty_string_valid_column_names=empty_string_valid_column_names)

