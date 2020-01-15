from __future__ import absolute_import

from typing import Optional

import canopy
import getpass
import datetime


class Session(object):
    _client: canopy.swagger.ApiClient

    def __init__(
            self,
            client: Optional[canopy.swagger.ApiClient] = None,
            client_id: Optional[str] = None,
            client_secret: Optional[str] = None,
            user_name: Optional[str] = None,
            tenant_name: Optional[str] = None,
            password: Optional[str] = None):
        if client is None:
            configuration = canopy.swagger.Configuration()
            configuration.host = 'https://api.canopysimulations.com/'
            client = canopy.swagger.ApiClient(configuration=configuration)
        self._client = client
        self._authentication = canopy.Authentication(client, client_id, client_secret, user_name, tenant_name, password)
        self._user_settings = canopy.UserSettingsManager(client, self._authentication)
        self._units = canopy.Units()

    @property
    def client(self) -> canopy.swagger.ApiClient:
        return self._client

    @property
    def authentication(self) -> canopy.Authentication:
        return self._authentication

    @property
    def user_settings(self) -> canopy.UserSettingsManager:
        return self._user_settings

    @property
    def units(self) -> canopy.Units:
        return self._units
