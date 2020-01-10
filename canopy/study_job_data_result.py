from typing import Mapping

import swagger_client
import pandas as pd


class StudyJobDataResult:
    def __init__(self, job: swagger_client.CanopyDocument, data: pd.DataFrame, units: Mapping[str, str]):
        self._job = job
        self._data = data
        self._units = units

    @property
    def job(self) -> swagger_client.CanopyDocument:
        return self._job

    @property
    def data(self) -> pd.DataFrame:
        return self._data

    @property
    def units(self) -> Mapping[str, str]:
        return self._units
