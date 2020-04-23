from typing import Optional, Mapping

import pandas as pd


class StudyScalarResults:
    def __init__(
            self,
            inputs: Optional[pd.DataFrame],
            inputs_metadata: Optional[pd.DataFrame],
            results: Optional[pd.DataFrame],
            results_metadata: Optional[pd.DataFrame],
            units: Mapping[str, str]):

        self._inputs = inputs
        self._inputs_metadata = inputs_metadata
        self._results = results
        self._results_metadata = results_metadata
        self._units = units

    @property
    def inputs(self) -> pd.DataFrame:
        return self._inputs

    @property
    def inputs_metadata(self) -> pd.DataFrame:
        return self._inputs_metadata

    @property
    def results(self) -> pd.DataFrame:
        return self._results

    @property
    def results_metadata(self) -> pd.DataFrame:
        return self._results_metadata

    @property
    def units(self) -> Mapping[str, str]:
        return self._units

    @property
    def merged(self) -> pd.DataFrame:
        return pd.merge(self._inputs, self._results, how='left', left_index=True, right_index=True)
