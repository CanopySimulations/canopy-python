from typing import Optional

import canopy
import datetime
import json
import base64
import urllib3
import certifi


_TOKEN_URL = 'https://identity.canopysimulations.com/connect/token'


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
        self._access_token: Optional[str] = None
        self._refresh_token: Optional[str] = None
        self._tenant_id: Optional[str] = None
        self._user_id: Optional[str] = None
        self._expires: datetime.datetime = datetime.datetime.min

    def authenticate(self):
        if self._access_token is None:
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

        token_response = self._request_token({
            'grant_type': 'password',
            'username': self._username,
            'password': self._password,
            'client_id': self._client_id,
            'client_secret': self._client_secret,
            'tenant': self._tenant_name,
        })

        claims = self._decode_jwt_payload(token_response['access_token'])
        self._tenant_id = claims.get('tenant')
        self._user_id = claims.get('sub')
        self._refresh_token = token_response.get('refresh_token')
        self._apply_token_response(token_response)

    def refresh_access_token(self):
        if self._refresh_token is None:
            raise RuntimeError('You must call authenticate before refreshing the access token.')

        token_response = self._request_token({
            'grant_type': 'refresh_token',
            'refresh_token': self._refresh_token,
            'client_id': self._client_id,
            'client_secret': self._client_secret,
        })

        self._apply_token_response(token_response)

    def _request_token(self, fields: dict) -> dict:
        proxy = self._client.configuration.proxy
        ca_certs = self._client.configuration.ssl_ca_cert or certifi.where()
        if proxy:
            http = urllib3.ProxyManager(
                proxy,
                proxy_headers=self._client.configuration.proxy_headers,
                ca_certs=ca_certs)
        else:
            http = urllib3.PoolManager(ca_certs=ca_certs)

        response = http.request(
            'POST',
            _TOKEN_URL,
            fields=fields,
            encode_multipart=False)

        if response.status != 200:
            raise RuntimeError(
                f'Token endpoint returned HTTP {response.status}: {response.data.decode("utf-8")}')

        return json.loads(response.data.decode('utf-8'))

    def _apply_token_response(self, token_response: dict):
        self._access_token = token_response['access_token']
        self._client.configuration.access_token = self._access_token
        self._expires = datetime.datetime.now() + datetime.timedelta(
            seconds=token_response['expires_in'])

    @staticmethod
    def _decode_jwt_payload(token: str) -> dict:
        payload = token.split('.')[1]
        payload += '=' * (-len(payload) % 4)
        return json.loads(base64.urlsafe_b64decode(payload))

    @property
    def tenant_id(self) -> str:
        if self._tenant_id is None:
            raise RuntimeError('You must call authenticate before requesting tenant ID.')
        return self._tenant_id

    @property
    def user_id(self) -> str:
        if self._user_id is None:
            raise RuntimeError('You must call authenticate before requesting user ID.')
        return self._user_id
