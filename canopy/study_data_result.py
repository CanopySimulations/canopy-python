from typing import Sequence, Union, Optional

import canopy


class StudyDataResult:
    def __init__(
            self,
            session: canopy.Session,
            study_result: Optional[canopy.swagger.GetStudyQueryResult],
            jobs: Sequence[canopy.StudyJobDataResult],
            document: Optional[canopy.swagger.CanopyDocument] = None):
        self._session = session
        self._study_result = study_result
        self._document: canopy.swagger.CanopyDocument = document if document is not None else study_result.study
        self._jobs = jobs

    @property
    def study_result(self) -> canopy.swagger.GetStudyQueryResult:
        return self._study_result

    @property
    def document(self) -> canopy.swagger.CanopyDocument:
        return self._document

    @property
    def study_document(self) -> canopy.swagger.StudyDocument:
        return canopy.get_study_document(self._session, self._document)

    @property
    def jobs(self) -> Sequence[canopy.StudyJobDataResult]:
        return self._jobs
