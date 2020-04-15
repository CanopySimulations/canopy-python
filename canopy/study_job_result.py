from typing import Mapping, Optional, Dict

import canopy
import pandas as pd
import numpy as np
import json


class StudyJobResult:
    def __init__(
            self,
            session: canopy.Session,
            job_result: Optional[canopy.openapi.GetStudyJobQueryResult],
            job: canopy.openapi.CanopyDocument,
            vector_metadata: Optional[pd.DataFrame],
            vector_data: pd.DataFrame,
            vector_units: Mapping[str, str],
            scalar_data: Mapping[str, float],
            scalar_units: Mapping[str, str],
            inputs: Optional[Dict[str, Dict]]):
        self._session = session
        self._job_result = job_result
        self._job = job
        self._vector_metadata = vector_metadata
        self._vector_data = vector_data
        self._vector_units = vector_units
        self._inputs = canopy.DynamicDictToObject(inputs) if inputs is not None else None
        self._scalar_data = scalar_data
        self._scalar_units = scalar_units

    @property
    def result(self) -> canopy.openapi.GetStudyJobQueryResult:
        return self._job_result

    @property
    def document(self) -> canopy.openapi.CanopyDocument:
        return self._job

    @property
    def vector_metadata(self) -> Optional[pd.DataFrame]:
        return self._vector_metadata

    @property
    def vector_data(self) -> pd.DataFrame:
        return self._vector_data

    @property
    def vector_units(self) -> Mapping[str, str]:
        return self._vector_units

    @property
    def scalar_data(self) -> Mapping[str, float]:
        return self._scalar_data

    @property
    def scalar_units(self) -> Mapping[str, str]:
        return self._scalar_units

    @property
    def inputs(self) -> Optional[canopy.DynamicDictToObject]:
        return self._inputs

    def vector_as(self, channel_name: str, target_units: Optional[str] = None, always_return_copy: bool = False) -> Optional[pd.Series]:
        if target_units is None:
            target_units = self._session.user_settings.get_channel_units(channel_name)

        result: Optional[pd.Series] = None

        if self._vector_data is not None and channel_name in self._vector_data.columns:
            result = self._vector_data[channel_name]

        if result is None:
            return None

        if target_units is None:
            return result.copy() if always_return_copy else result

        source_units = ''
        if channel_name in self._vector_units:
            source_units = self._vector_units[channel_name]

        return self._session.units.convert_series_between_units(
            result,
            source_units,
            target_units,
            inplace=False,
            always_return_copy=always_return_copy)

    def scalar_as(self, channel_name: str, target_unit: Optional[str] = None) -> float:
        if target_unit is None:
            target_unit = self._session.user_settings.get_channel_units(channel_name)

        if channel_name not in self._scalar_data:
            return np.NaN

        result = self._scalar_data[channel_name]

        if target_unit is None:
            return result

        source_unit = ''
        if channel_name in self._scalar_units:
            source_unit = self._scalar_units[channel_name]

        return self._session.units.convert_value_between_units(
            result,
            source_unit,
            target_unit)

    def to_dict(self):
        return {
            'job_result': self._job_result,
            'job': self._job
        }

    def __repr__(self):
        return 'canopy.StudyJobResult(%r,%r)' % \
               (self._job_result, self._job)

    def __str__(self):
        return json.dumps(self.to_dict(), indent=2, default=str)