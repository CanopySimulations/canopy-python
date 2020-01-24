from typing import Optional

import canopy
import integration_tests


class Environment(object):
    _session: Optional[canopy.Session] = None
    _environment_data: Optional[integration_tests.EnvironmentData] = None

    async def __aenter__(self):
        self._environment_data = await integration_tests.EnvironmentLoader.load()
        self._session = self._environment_data.create_session()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self._session is not None:
            await self._session.__aexit__(exc_type, exc, tb)

    def __enter__(self):
        canopy.run(self.__aenter__())
        return self

    def __exit__(self, exc_type, exc, tb):
        canopy.run(self.__aexit__(exc_type, exc, tb))

    @property
    def session(self) -> canopy.Session:
        if self._session is None:
            raise RuntimeError('Session not created.')

        return self._session

    @property
    def data(self) -> integration_tests.EnvironmentData:
        if self._environment_data is None:
            raise RuntimeError('Environment data not created.')

        return self._environment_data
