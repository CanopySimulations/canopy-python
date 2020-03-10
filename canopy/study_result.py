from typing import Sequence, Optional

import canopy
import pandas as pd
import json

_definition_key = 'definition'
_sim_types_key = 'simTypes'
_sim_config_key = 'simConfig'


class StudyResult:
    _sim_types: Optional[Sequence[str]] = None
    _inputs: Optional[canopy.DynamicDictToObject] = None

    def __init__(
            self,
            session: canopy.Session,
            study_result: Optional[canopy.openapi.GetStudyQueryResult],
            jobs: Optional[Sequence[canopy.StudyJobResult]],
            document: Optional[canopy.openapi.CanopyDocument] = None,
            scalar_results: Optional[canopy.StudyScalarResults] = None):
        self._session = session
        self._study_result = study_result
        self._scalar_results = scalar_results
        self._document: canopy.openapi.CanopyDocument = document if document is not None else study_result.study

        if self._document is None:
            raise RuntimeError('Study document not provided.')

        self._data = canopy.get_study_document(self._session, self._document)
        self._jobs = jobs

        if self._data is not None and self._data.definition is not None:
            definition = canopy.ensure_dict(self._data.definition)
            self._sim_types = definition[_sim_types_key]
            self._inputs = canopy.DynamicDictToObject(canopy.ensure_dict(definition[_sim_config_key]))

    @property
    def result(self) -> canopy.openapi.GetStudyQueryResult:
        return self._study_result

    @property
    def document(self) -> canopy.openapi.CanopyDocument:
        return self._document

    @property
    def study_id(self) -> str:
        return self._document.document_id

    @property
    def data(self) -> canopy.openapi.StudyDocument:
        return self._data

    @property
    def sim_types(self) -> Optional[Sequence[str]]:
        return self._sim_types

    @property
    def inputs(self) -> Optional[canopy.DynamicDictToObject]:
        return self._inputs

    @property
    def jobs(self) -> Optional[Sequence[canopy.StudyJobResult]]:
        return self._jobs

    @property
    def scalar_results(self) -> Optional[canopy.StudyScalarResults]:
        return self._scalar_results

    @property
    def simulation_count(self) -> int:
        if self._data.job_count == 1:
            return 1

        # If there is more than one job then the final job will be the post-processing task.
        return self._data.job_count - 1

    @property
    def succeeded_simulation_count(self) -> int:
        return self._data.succeeded_simulation_count

    def scalar_as(self, channel_name: str, target_unit: Optional[str] = None, always_return_copy: bool = False) -> Optional[pd.Series]:
        if self._scalar_results is None:
            return None

        scalar_results = self._scalar_results
        if target_unit is None:
            target_unit = self._session.user_settings.get_channel_units(channel_name)

        result: Optional[pd.Series] = None
        if scalar_results.inputs is not None and channel_name in scalar_results.inputs.columns:
            result = scalar_results.inputs[channel_name]
        elif scalar_results.results is not None and channel_name in scalar_results.results.columns:
            result = scalar_results.results[channel_name]

        if result is None:
            return None

        if target_unit is None:
            return result.copy() if always_return_copy else result

        source_unit = ''
        if channel_name in self._scalar_results.units:
            source_unit = self._scalar_results.units[channel_name]

        return self._session.units.convert_series_between_units(
            result,
            source_unit,
            target_unit,
            inplace=False,
            always_return_copy=always_return_copy)

    def to_dict(self):
        return {
            'study_id': self.study_id,
            'sim_types': self._sim_types,
            'simulation_count': self.simulation_count,
            'study_result': self._study_result,
            'document': self.document
        }

    def __repr__(self):
        return 'canopy.StudyResult(%r,%r,%r)' % \
               (self.study_id, self._sim_types, self.simulation_count)

    def __str__(self):
        return json.dumps(self.to_dict(), indent=2, default=str)