from typing import Optional

import canopy
import getpass
import datetime


class Authentication(object):
    _client: canopy.openapi.ApiClient

    def __init__(
            self,
            client: canopy.openapi.ApiClient,
            client_id: Optional[str] = None,
            client_secret: Optional[str] = None,
            username: Optional[str] = None,
            tenant_name: Optional[str] = None,
            password: Optional[str] = None):
        self._client = client
        self._client_id = client_id
        self._client_secret = client_secret
        self._username = username
        self._tenant_name = tenant_name
        self._password = password
        self._identity = None
        self._expires: datetime.datetime = datetime.datetime.min

    def authenticate(self):
        if self._identity is None or self._expires is None:
            self.sign_in()
        elif datetime.datetime.now() >= self._expires:
            self.refresh_access_token()

    def sign_in(self):
        authentication_data = canopy.prompt_for_authentication(
            client_id=self._client_id,
            client_secret=self._client_secret,
            username=self._username,
            tenant_name=self._tenant_name,
            password=self._password)

        self._client_id = authentication_data.client_id
        self._client_secret = authentication_data.client_secret
        self._username = authentication_data.username
        self._tenant_name = authentication_data.tenant_name
        self._password = authentication_data.password

        post_params = {
            'grant_type': 'password',
            'username': self._username,
            'tenant': self._tenant_name,
            'password': self._password,
            'client_id': self._client_id,
            'client_secret': self._client_secret,
        }

        header_params = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        token_result = self._client.call_api(
            '/token',
            'POST',
            post_params=post_params,
            header_params=header_params,
            response_type=object)

        self._identity = token_result[0]
        self.__update_from_identity()

    def refresh_access_token(self):
        if self._identity is None:
            raise RuntimeError('You must call authenticate before refreshing the access token.')

        post_params = {
            'grant_type': 'refresh_token',
            'refresh_token': self._identity['refresh_token'],
            'tenant': self._identity['tenant_id'],
            'client_id': self._client_id,
            'client_secret': self._client_secret,
        }

        header_params = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        token_result = self._client.call_api(
            '/token',
            'POST',
            post_params=post_params,
            header_params=header_params,
            response_type=object)

        self._identity = token_result[0]
        self.__update_from_identity()

    def __update_from_identity(self):
        self._client.configuration.access_token = self._identity['access_token']
        expires_delta = datetime.timedelta(seconds=self._identity['expires_in'])
        self._expires = datetime.datetime.now() + expires_delta

    @property
    def tenant_id(self) -> str:
        if self._identity is None:
            raise RuntimeError('You must call authenticate before requesting tenant ID.')

        return self._identity['tenant_id']

    @property
    def user_id(self) -> str:
        if self._identity is None:
            raise RuntimeError('You must call authenticate before requesting user ID.')

        return self._identity['user_id']
