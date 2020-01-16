from typing import Optional
from urllib.error import HTTPError

import canopy
import pandas as pd
import logging

logger = logging.getLogger(__name__)


# We're making this async for future backwards compatibility if we convert read_csv into something which
# supports asyncio.
async def load_vector_metadata(
        job_access_information: canopy.swagger.BlobAccessInformation,
        sim_type: str) -> Optional[pd.DataFrame]:
    file_name = ''.join([sim_type, '_VectorMetadata.csv'])
    try:
        vector_metadata_url = ''.join([job_access_information.url, file_name, job_access_information.access_signature])
        vector_metadata = pd.read_csv(vector_metadata_url, index_col=False)
        vector_metadata.set_index(['name'], inplace=True)
        return vector_metadata
    except HTTPError:
        logger.warning('Not found: %s', file_name)
        return None

