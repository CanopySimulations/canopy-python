from typing import Optional
from urllib.error import HTTPError

import canopy
import pandas as pd
import logging

logger = logging.getLogger(__name__)


# We're making this async for future backwards compatibility if we convert read_csv into something which
# supports asyncio.
async def load_study_job_scalar_results(
        job_access_information: canopy.swagger.BlobAccessInformation,
        sim_type: str) -> Optional[pd.DataFrame]:
    file_name = ''.join([sim_type, '_ScalarResults.csv'])
    try:
        scalar_results_url = ''.join([job_access_information.url, file_name, job_access_information.access_signature])
        scalar_results = pd.read_csv(scalar_results_url, index_col=False)
        scalar_results.set_index(['name'], inplace=True)
        return scalar_results
    except HTTPError:
        logger.warning('Not found: %s', file_name)
        return None

