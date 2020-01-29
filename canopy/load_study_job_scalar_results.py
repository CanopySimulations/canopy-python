from typing import Optional

import canopy
import pandas as pd
import logging

logger = logging.getLogger(__name__)


async def load_study_job_scalar_results(
        session: canopy.Session,
        job_access_information: canopy.swagger.BlobAccessInformation,
        sim_type: str) -> Optional[pd.DataFrame]:
    file_name = ''.join([sim_type, '_ScalarResults.csv'])
    url = ''.join([job_access_information.url, file_name, job_access_information.access_signature])
    return await canopy.try_load_csv_from_url(session, url, file_name, 'name')

