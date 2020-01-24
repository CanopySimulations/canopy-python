from typing import Sequence, Union, Optional

import canopy


class StudyResult:
    _data: Optional[canopy.swagger.StudyDocument] = None

    def __init__(
            self,
            session: canopy.Session,
            study_result: Optional[canopy.swagger.GetStudyQueryResult],
            jobs: Sequence[canopy.StudyJobResult],
            document: Optional[canopy.swagger.CanopyDocument] = None):
        self._session = session
        self._study_result = study_result
        self._document: canopy.swagger.CanopyDocument = document if document is not None else study_result.study
        self._jobs = jobs

    @property
    def result(self) -> canopy.swagger.GetStudyQueryResult:
        return self._study_result

    @property
    def document(self) -> canopy.swagger.CanopyDocument:
        return self._document

    @property
    def data(self) -> canopy.swagger.StudyDocument:
        if self._data is None:
            self._data = canopy.get_study_document(self._session, self._document)
        return self._data

    @property
    def jobs(self) -> Sequence[canopy.StudyJobResult]:
        return self._jobs
