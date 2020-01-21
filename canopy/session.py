from typing import Optional, Coroutine

import canopy
import aiohttp
import asyncio


class Session(object):
    _sync_client: canopy.swagger.ApiClient
    _async_client: canopy.swagger_asyncio.ApiClient

    def __init__(
            self,
            authentication_data: Optional[canopy.AuthenticationData] = None,
            client_id: Optional[str] = None,
            client_secret: Optional[str] = None,
            username: Optional[str] = None,
            tenant_name: Optional[str] = None,
            password: Optional[str] = None):
        self._configuration = canopy.swagger.Configuration()
        self._configuration.host = 'https://api.canopysimulations.com/'
        self._sync_client = canopy.swagger.ApiClient(configuration=self._configuration)
        self._async_client = canopy.swagger_asyncio.ApiClient(configuration=self._configuration)

        if authentication_data is not None:
            client_id = authentication_data.client_id
            client_secret = authentication_data.client_secret
            username = authentication_data.username
            tenant_name = authentication_data.tenant_name
            password = authentication_data.password

        self._authentication = canopy.Authentication(
            self._sync_client,
            client_id,
            client_secret,
            username,
            tenant_name,
            password)
        self._user_settings = canopy.UserSettingsManager(self._sync_client, self._authentication)
        self._units = canopy.Units()
        self._tenant_users = canopy.TenantUsersManager(self._sync_client, self._authentication)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        canopy.run(self.__aexit__(exc_type, exc, tb))

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
    def sync_client(self) -> canopy.swagger.ApiClient:
        return self._sync_client

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
    def tenant_users(self) -> canopy.TenantUsersManager:
        return self._tenant_users

    @property
    def units(self) -> canopy.Units:
        return self._units
