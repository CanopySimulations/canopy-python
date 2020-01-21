import canopy


class EnvironmentData(object):
    def __init__(
            self,
            authentication: canopy.AuthenticationData,
            car: canopy.ConfigResult,
            study: canopy.swagger.CanopyDocument):
        self._authentication = authentication
        self._car = car
        self._study = study

    @property
    def authentication(self) -> canopy.AuthenticationData:
        return self._authentication

    @property
    def car(self) -> canopy.ConfigResult:
        return self._car

    @property
    def study(self) -> canopy.swagger.CanopyDocument:
        return self._study

    def create_session(self) -> canopy.Session:
        return canopy.Session(self._authentication)
