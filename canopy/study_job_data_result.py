from struct import Struct
from typing import Mapping, Any, Optional, Dict

import canopy
import pandas as pd
import numpy as np


class StudyJobDataResult:
    def __init__(
            self,
            session: canopy.Session,
            job: canopy.swagger.CanopyDocument,
            vector_data: pd.DataFrame,
            vector_data_units: Mapping[str, str],
            scalar_data: Mapping[str, float],
            scalar_data_units: Mapping[str, str],
            inputs: Optional[Dict[str, Dict]]):
        self._session = session
        self._job = job
        self._vector_data = vector_data
        self._vector_data_units = vector_data_units
        self._inputs = canopy.DynamicDictToObject(inputs) if inputs is not None else None
        self._scalar_data = scalar_data
        self._scalar_data_units = scalar_data_units

    @property
    def document(self) -> canopy.swagger.CanopyDocument:
        return self._job

    @property
    def vector_data(self) -> pd.DataFrame:
        return self._vector_data

    @property
    def vector_data_units(self) -> Mapping[str, str]:
        return self._vector_data_units

    @property
    def scalar_data(self) -> Mapping[str, float]:
        return self._scalar_data

    @property
    def scalar_data_units(self) -> Mapping[str, str]:
        return self._scalar_data_units

    @property
    def inputs(self) -> Optional[canopy.DynamicDictToObject]:
        return self._inputs

    def vector_as(self, channel_name: str, units: Optional[str] = None, always_return_copy: bool = False) -> Optional[pd.Series]:
        if units is None:
            units = self._session.user_settings.get_channel_units(channel_name)

        result = self._vector_data[channel_name]
        if result is None:
            return None

        if units is None:
            return result.copy() if always_return_copy else result

        return self._session.units.convert_series_from_si(
            result,
            units,
            inplace=False,
            always_return_copy=always_return_copy)

    def scalar_as(self, channel_name: str, units: Optional[str] = None) -> float:
        if units is None:
            units = self._session.user_settings.get_channel_units(channel_name)

        if channel_name not in self._scalar_data:
            return np.NaN

        result = self._scalar_data[channel_name]

        if units is None:
            return result

        return self._session.units.convert_value_from_si(
            result,
            units)
