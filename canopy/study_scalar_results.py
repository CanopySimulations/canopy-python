from typing import Optional

import pandas as pd


class StudyScalarResults:
    def __init__(
            self,
            scalar_inputs: Optional[pd.DataFrame],
            scalar_inputs_metadata: Optional[pd.DataFrame],
            scalar_results: Optional[pd.DataFrame],
            scalar_results_metadata: Optional[pd.DataFrame]):

        self._scalar_inputs = scalar_inputs
        self._scalar_inputs_metadata = scalar_inputs_metadata
        self._scalar_results = scalar_results
        self._scalar_results_metadata = scalar_results_metadata

    @property
    def inputs(self) -> pd.DataFrame:
        return self._scalar_inputs

    @property
    def inputs_metadata(self) -> pd.DataFrame:
        return self._scalar_inputs_metadata

    @property
    def results(self) -> pd.DataFrame:
        return self._scalar_results

    @property
    def results_metadata(self) -> pd.DataFrame:
        return self._scalar_results_metadata
