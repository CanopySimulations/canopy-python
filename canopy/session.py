from __future__ import absolute_import

from typing import Optional

from swagger_client.api_client import ApiClient
import getpass
import datetime


class Session(object):
    client: ApiClient

    def __init__(
            self,
            client: Optional[ApiClient] = None,
            client_id: Optional[str] = None,
            client_secret: Optional[str] = None,
            user_name: Optional[str] = None,
            tenant_name: Optional[str] = None):
        if client is None:
            client = ApiClient()
        self.client = client
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_name = user_name
        self.tenant_name = tenant_name
        self.identity = None
        self.expires: datetime.datetime = datetime.datetime.min

    def authenticate(self):
        if self.identity is None or self.expires is None:
            self.sign_in()
        elif datetime.datetime.now() >= self.expires:
            self.refresh_access_token()

    def sign_in(self):
        if self.client_id is None:
            self.client_id = input('Client ID:')
        if self.client_secret is None:
            self.client_secret = getpass.getpass(prompt='Client Secret:')
        
        if self.user_name is None:
            self.user_name = input('Username:')
        if self.tenant_name is None:
            self.tenant_name = self.client_id
        
        password = getpass.getpass(prompt='Password:')

        post_params = {
            'grant_type': 'password',
            'username': self.user_name,
            'tenant': self.tenant_name,
            'password': password,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }

        header_params = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        token_result = self.client.call_api('/token', 'POST', post_params=post_params, header_params=header_params, response_type=object)
        self.identity = token_result[0]
        self.__update_from_identity()

    def refresh_access_token(self):
        if self.identity is None:
            raise RuntimeError('You must call authenticate before refreshing the access token.')

        post_params = {
            'grant_type': 'refresh_token',
            'refresh_token': self.identity['refresh_token'],
            'tenant': self.identity['tenant_id'],
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }

        header_params = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        token_result = self.client.call_api('/token', 'POST', post_params=post_params, header_params=header_params, response_type=object)
        self.identity = token_result[0]
        self.__update_from_identity()

    def __update_from_identity(self):
        self.client.configuration.access_token = self.identity['access_token']
        expires_delta = datetime.timedelta(seconds=self.identity['expires_in'])
        self.expires = datetime.datetime.now() + expires_delta

    @property
    def tenant_id(self) -> str:
        if self.identity is None:
            raise RuntimeError('You must call authenticate before requesting tenant ID.')

        return self.identity['tenant_id']

    @property
    def user_id(self) -> str:
        if self.identity is None:
            raise RuntimeError('You must call authenticate before requesting user ID.')

        return self.identity['user_id']
