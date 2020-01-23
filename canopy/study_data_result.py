from typing import Sequence

import canopy


class StudyDataResult:
    def __init__(self, study_result: canopy.swagger.GetStudyQueryResult, jobs: Sequence[canopy.StudyJobDataResult]):
        self._study_result = study_result
        self._study: canopy.swagger.CanopyDocument = study_result.study
        self._jobs = jobs

    @property
    def study_result(self) -> canopy.swagger.GetStudyQueryResult:
        return self._study_result

    @property
    def study(self) -> canopy.swagger.CanopyDocument:
        return self._study

    @property
    def jobs(self) -> Sequence[canopy.StudyJobDataResult]:
        return self._jobs
