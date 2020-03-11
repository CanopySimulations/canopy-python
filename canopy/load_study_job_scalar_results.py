from typing import Optional

import canopy
import pandas as pd
import logging

logger = logging.getLogger(__name__)


async def load_study_job_scalar_results(
        session: canopy.Session,
        job_access_information: canopy.openapi.BlobAccessInformation,
        sim_type: str) -> Optional[pd.DataFrame]:

    sim_type = canopy.ensure_sim_type_string(sim_type)

    file_name = ''.join([sim_type, '_ScalarResults.csv'])
    url = ''.join([job_access_information.url, file_name, job_access_information.access_signature])

    return await canopy.try_load_csv_from_url(
        session,
        url,
        file_name,
        index_column_name='name',
        empty_string_valid_column_names=['units', 'description', 'constraintParameterPath'])

