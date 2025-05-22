from authlib.integrations.requests_client import OAuth2Session
from http.server import HTTPServer, BaseHTTPRequestHandler
from secrets import token_urlsafe
from typing import Optional

import canopy
import datetime
import requests
import threading
import time
import webbrowser

class Authentication(object):
    _client: canopy.openapi.ApiClient
    _identity: canopy.openapi.models.GrantTypeHandlerResponse

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

    def authenticate_with_browser(self):
        if self._identity is None or self._expires is None:
            self.sign_in_with_browser()
        elif datetime.datetime.now() >= self._expires:
            self.refresh_access_token()

    def sign_in_with_browser(self):
        client_id, client_secret = canopy.prompt_for_authentication_browser()
        # === Configuration ===
        DISCOVERY_URL = 'https://identity.canopysimulations.com' + '/.well-known/openid-configuration'
        REDIRECT_URI_HOST = 'http://localhost'
        SCOPE = "openid profile canopy_api IdentityServerApi offline_access"

        config = requests.get(DISCOVERY_URL, verify=False).json()
        AUTHORIZATION_ENDPOINT = config['authorization_endpoint']
        TOKEN_ENDPOINT = config['token_endpoint']
        USERINFO_ENDPOINT = config['userinfo_endpoint']

        # === Local server to capture callback ===
        class CallbackHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                self.server.path = self.path
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'Login complete. You can close this window.')

        authorization_response = None
        port = None
        def start_callback_server():
            server = HTTPServer(('0.0.0.0', 0), CallbackHandler)
            global port
            port = server.server_port
            server.handle_request()
            global authorization_response
            authorization_response = server.path

        # === Main OIDC flow with discovery ===
        server_thread = threading.Thread(target=start_callback_server, daemon=True)
        server_thread.start()

        while(port == None):
            time.sleep(0.1)

        client = OAuth2Session(client_id=client_id, client_secret=client_secret, redirect_uri=REDIRECT_URI_HOST + ':' + str(port), scope=SCOPE, code_challenge_method='S256')

        code_verifier = token_urlsafe(48)
        # Generate auth URL
        auth_url, _ = client.create_authorization_url(AUTHORIZATION_ENDPOINT, code_verifier=code_verifier)

        # Open browser
        webbrowser.open(auth_url)

        server_thread.join()

        # Exchange code for token
        token_result = client.fetch_token(
            TOKEN_ENDPOINT,
            authorization_response=authorization_response,
            code_verifier=code_verifier,
            verify=False,
        )

        userinfo = client.get(USERINFO_ENDPOINT).json()

        #Map results to legacy object
        self._identity.expires_in = token_result['expires_in']
        self._identity.access_token = token_result['access_token']
        self._identity.refresh_token = token_result['refresh_token']
        self._identity.expires = token_result['expires_at']
        self._identity.token_type = token_result['token_type']
        self._identity.tenant_id = userinfo['tenant']
        self._identity.user_id = userinfo['sub']
        self._identity.username = userinfo['name']
        self._identity.roles = ', '.join(userinfo['roles'])
        
        self.__update_from_identity()


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

        token_api = canopy.openapi.TokenApi(self._client)

        token_result = token_api.token_post_token(
            grant_type = 'password',
            username = self._username,
            tenant = self._tenant_name,
            password = self._password,
            client_id = self._client_id,
            client_secret = self._client_secret)

        self._identity = token_result
        self.__update_from_identity()

    def refresh_access_token(self):
        if self._identity is None:
            raise RuntimeError('You must call authenticate before refreshing the access token.')

        token_api = canopy.openapi.TokenApi(self._client)

        token_result = token_api.token_post_token(
            grant_type = 'refresh_token',
            refresh_token = self._identity.refresh_token,
            client_id = self._client_id,
            client_secret = self._client_secret)

        self._identity.access_token = token_result.access_token
        self._identity.expires_in = token_result.expires_in
        self.__update_from_identity()

    def __update_from_identity(self):
        self._client.configuration.access_token = self._identity.access_token
        expires_delta = datetime.timedelta(seconds=self._identity.expires_in)
        self._expires = datetime.datetime.now() + expires_delta

    @property
    def tenant_id(self) -> str:
        if self._identity is None:
            raise RuntimeError('You must call authenticate before requesting tenant ID.')

        return self._identity.tenant_id

    @property
    def user_id(self) -> str:
        if self._identity is None:
            raise RuntimeError('You must call authenticate before requesting user ID.')

        return self._identity.user_id
