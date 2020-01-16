from typing import Optional, Coroutine

import canopy
import aiohttp
import asyncio


class Session(object):
    _client: canopy.swagger.ApiClient
    _async_client: canopy.swagger_asyncio.ApiClient

    def __init__(
            self,
            client_id: Optional[str] = None,
            client_secret: Optional[str] = None,
            user_name: Optional[str] = None,
            tenant_name: Optional[str] = None,
            password: Optional[str] = None):
        self._configuration = canopy.swagger.Configuration()
        self._configuration.host = 'https://api.canopysimulations.com/'
        self._client = canopy.swagger.ApiClient(configuration=self._configuration)
        self._async_client = canopy.swagger_asyncio.ApiClient(configuration=self._configuration)

        self._authentication = canopy.Authentication(self._client, client_id, client_secret, user_name, tenant_name, password)
        self._user_settings = canopy.UserSettingsManager(self._client, self._authentication)
        self._units = canopy.Units()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.async_client_session.close()

    @property
    def default_api_concurrency(self) -> int:
        return 5

    @property
    def default_blob_storage_concurrency(self) -> int:
        return 10

    @property
    def configuration(self) -> canopy.swagger.Configuration:
        return self._configuration

    @property
    def client(self) -> canopy.swagger.ApiClient:
        return self._client

    @property
    def async_client(self) -> canopy.swagger_asyncio.ApiClient:
        return self._async_client

    @property
    def async_client_session(self) -> aiohttp.ClientSession:
        return self._async_client.rest_client.pool_manager

    @property
    def authentication(self) -> canopy.Authentication:
        return self._authentication

    @property
    def user_settings(self) -> canopy.UserSettingsManager:
        return self._user_settings

    @property
    def units(self) -> canopy.Units:
        return self._units
