from typing import Optional

import datetime
import canopy
from canopy.open_id_connect import OpenIDConnect

class Authentication(object):
    _client: canopy.openapi.ApiClient
    _identity: canopy.openapi.models.GrantTypeHandlerResponse
    _open_id_connect = OpenIDConnect()

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
        access_token, expires_in = self._open_id_connect.get_access_token_pw()
        user_info = self._open_id_connect.get_user_info()
        self._identity = { 'tenant_id': user_info['tenant'], 'user_id': user_info['sub'], 'access_token': access_token, 'expires_in': expires_in }
        self.__update_from_identity()

    def refresh_access_token(self):
        if self._identity is None:
            raise RuntimeError('You must call authenticate before refreshing the access token.')
        
        access_token = self._open_id_connect.get_refresh_access_token()

        self._identity['access_token'] = access_token
        # self._identity['expires_in'] = expires_in
        self.__update_from_identity()

    def __update_from_identity(self):
        self._client.configuration.access_token = self._identity['access_token']
        expires_delta = datetime.timedelta(seconds=self._identity['expires_in'])
        self._expires = datetime.datetime.now() + expires_delta

    @property
    def tenant_id(self) -> str:
        if self._identity is None:
            raise RuntimeError('You must call authenticate before requesting tenant ID.')
        
        if self._identity['tenant_id'] is None:
            raise RuntimeError('You must authenticate as a user to request tenant ID.')

        return self._identity['tenant_id']

    @property
    def user_id(self) -> str:
        if self._identity is None:
            raise RuntimeError('You must call authenticate before requesting user ID.')
        
        if self._identity['user_id'] is None:
            raise RuntimeError('You must authenticate as a user to request user ID.')

        return self._identity['user_id']
