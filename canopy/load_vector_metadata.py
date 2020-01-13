from typing import Optional
from urllib.error import HTTPError

import pandas as pd
import logging

logger = logging.getLogger(__name__)


def load_vector_metadata(job_url: str, sas: str, sim_type: str) -> Optional[pd.DataFrame]:
    file_name = ''.join([sim_type, '_VectorMetadata.csv'])
    try:
        vector_metadata_url = ''.join([job_url, file_name, sas])
        vector_metadata = pd.read_csv(vector_metadata_url, index_col=False)
        vector_metadata.set_index(['name'], inplace=True)
        return vector_metadata
    except HTTPError:
        logger.warning('Not found: %s', file_name)
        return None

