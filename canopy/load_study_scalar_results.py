from typing import Optional

import canopy
import pandas as pd
import logging
import asyncio

logger = logging.getLogger(__name__)


async def load_study_scalar_results(
        session: canopy.Session,
        study_access_information: canopy.swagger.StudyBlobAccessInformation) -> canopy.StudyScalarResults:

    scalar_inputs_task = asyncio.ensure_future(_load_file(session, 'scalar-inputs.csv', None, study_access_information))
    scalar_inputs_metadata_task = asyncio.ensure_future(_load_file(session, 'scalar-inputs-metadata.csv', 'inputName', study_access_information))
    scalar_results_task = asyncio.ensure_future(_load_file(session, 'scalar-results.csv', None, study_access_information))
    scalar_results_metadata_task = asyncio.ensure_future(_load_file(session, 'scalar-metadata.csv', 'name', study_access_information))

    scalar_inputs = await scalar_inputs_task
    scalar_inputs_metadata = await scalar_inputs_metadata_task
    scalar_results = await scalar_results_task
    scalar_results_metadata = await scalar_results_metadata_task

    return canopy.StudyScalarResults(
        scalar_inputs,
        scalar_inputs_metadata,
        scalar_results,
        scalar_results_metadata)


async def _load_file(
        session: canopy.Session,
        file_name: str,
        index_column_name: Optional[str],
        study_access_information: canopy.swagger.StudyBlobAccessInformation) -> Optional[pd.DataFrame]:

    url = ''.join([study_access_information.url, file_name, study_access_information.access_signature])
    return await canopy.try_load_csv_from_url(session, url, file_name, index_column_name)

