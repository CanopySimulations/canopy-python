import canopy


class EnvironmentData(object):
    def __init__(
            self,
            authentication: canopy.AuthenticationData):
        self._authentication = authentication

    @property
    def authentication(self) -> canopy.AuthenticationData:
        return self._authentication

    def create_session(self) -> canopy.Session:
        return canopy.Session(self._authentication)
        # return canopy.Session(self._authentication, proxy=canopy.ProxyConfiguration('http://localhost:8888', '1', '1'))
