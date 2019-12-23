from urllib.error import HTTPError

import pandas as pd


def load_vector_metadata(job_url, sas, sim_type):
    file_name = ''.join([sim_type, '_VectorMetadata.csv'])
    try:
        vector_metadata_url = ''.join([job_url, file_name, sas])
        vector_metadata = pd.read_csv(vector_metadata_url, index_col=False)
        vector_metadata.set_index(['name'], inplace=True)
        return vector_metadata
    except HTTPError:
        print('Not found: ' + file_name)
        return None

