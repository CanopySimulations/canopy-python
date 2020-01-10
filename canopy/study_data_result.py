from __future__ import absolute_import

from typing import List, Sequence

import swagger_client
import canopy


class StudyDataResult:
    def __init__(self, study: swagger_client.CanopyDocument, jobs: Sequence[canopy.StudyJobDataResult]):
        self._study = study
        self._jobs = jobs

    @property
    def study(self) -> swagger_client.CanopyDocument:
        return self._study

    @property
    def jobs(self) -> Sequence[canopy.StudyJobDataResult]:
        return self._jobs
