from typing import Sequence, Union, Optional, Any

import canopy

_definition_key = 'definition'
_sim_types_key = 'simTypes'
_sim_config_key = 'simConfig'


class StudyResult:
    _sim_types: Optional[Sequence[str]] = None
    _inputs: Optional[canopy.DynamicDictToObject] = None

    def __init__(
            self,
            session: canopy.Session,
            study_result: Optional[canopy.swagger.GetStudyQueryResult],
            jobs: Optional[Sequence[canopy.StudyJobResult]],
            document: Optional[canopy.swagger.CanopyDocument] = None,
            scalar_results: Optional[canopy.StudyScalarResults] = None):
        self._session = session
        self._study_result = study_result
        self._scalar_results = scalar_results
        self._document: canopy.swagger.CanopyDocument = document if document is not None else study_result.study

        if self._document is None:
            raise RuntimeError('Study document not provided.')

        self._data = canopy.get_study_document(self._session, self._document)
        self._jobs = jobs

        if self._data is not None and self._data.definition is not None:
            definition = canopy.ensure_dict(self._data.definition)
            self._sim_types = definition[_sim_types_key]
            self._inputs = canopy.DynamicDictToObject(canopy.ensure_dict(definition[_sim_config_key]))

    @property
    def result(self) -> canopy.swagger.GetStudyQueryResult:
        return self._study_result

    @property
    def document(self) -> canopy.swagger.CanopyDocument:
        return self._document

    @property
    def data(self) -> canopy.swagger.StudyDocument:
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
