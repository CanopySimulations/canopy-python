import base64
import hashlib
from http.server import BaseHTTPRequestHandler, HTTPServer
import random
import string
from typing import Any, Dict
from urllib import parse
import webbrowser
import requests
from oauthlib.oauth2 import WebApplicationClient

CONFIG = {
    'port': 9000,
    'client_id': 'angular_client',
    'username': 'test',
    'tenant': 'canopy',
    'password': 'password',
    'redirect_uri': 'http://localhost:9000',
    'scopes': [ 'openid', 'profile', 'canopy_api', 'offline_access' ]
}

ISSUER = 'https://localhost:5001'

class OAuthHttpServer(HTTPServer):
    def __init__(self, *args, **kwargs):
        print('init http server')
        HTTPServer.__init__(self, *args, **kwargs)
        self.allow_reuse_address = True
        self.authorization_code = ''

class OAuthHttpHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        BaseHTTPRequestHandler.__init__(self, *args, **kwargs)
        self.close_connection = True
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write('<script type=\"application/javascript\">window.close();</script>'.encode('UTF-8'))
        
        parsed = parse.urlparse(self.path)
        qs = parse.parse_qs(parsed.query)
        
        self.server.authorization_code = qs['code'][0]

class OpenIDConnect(object):
    _instance = None
    _code_verifier = None
    _code_challenge = None
    _discovery_document = None
    _auth_code = None
    _access_token = None
    _refresh_token = None
    _expires_in = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OpenIDConnect, cls).__new__(cls)
            cls._instance._code_verifier = cls.get_code_verifier(cls._instance)
            cls._instance._code_challenge = cls.generate_code_challenge(cls._instance)

        return cls._instance

    def get_discovery_document(self) -> dict[str, str]:
        if not self._discovery_document:
            discovery_uri = ISSUER + '/.well-known/openid-configuration'
            try:
                response = requests.get(discovery_uri, verify=False)
                self._discovery_document = response.json()
            except Exception as exc:
                self._discovery_document = None
                raise ValueError('Could not obtain discovery document for the specified issuer.') from exc
        
        return self._discovery_document
            
    def get_authorization_code(self) -> str:
        if not self._auth_code:
            if not self._discovery_document:
                self.get_discovery_document()

            try:
                with OAuthHttpServer(('', CONFIG['port']), OAuthHttpHandler) as httpd:
                    client = WebApplicationClient(CONFIG['client_id'])

                    rand = random.SystemRandom()
                    state = ''.join(rand.choices(string.ascii_letters + string.digits, k=64))
                    
                    auth_uri = client.prepare_request_uri(
                        self._discovery_document['authorization_endpoint'],
                        redirect_uri=CONFIG['redirect_uri'],
                        scope=CONFIG['scopes'],
                        state=state,
                        code_challenge=self._code_challenge,
                        code_challenge_method='S256')

                    webbrowser.open_new(auth_uri)

                    httpd.handle_request()

                    self._auth_code = httpd.authorization_code
            except Exception as exc:
                self._auth_code = None
                raise ValueError('Could not obtain authorization code for the specified client.') from exc

        return self._auth_code

    def get_access_token(self) -> str:
        if not self._access_token:
            if not self._auth_code:
                self.get_authorization_code()

            data = {
                'code': self._auth_code,
                'client_id': CONFIG['client_id'],
                'grant_type': 'authorization_code',
                'scopes': CONFIG['scopes'],
                'redirect_uri': CONFIG['redirect_uri'],
                'code_verifier': self._code_verifier
            }

            if not self._discovery_document:
                self.get_discovery_document()

            try:
                response = requests.post(self._discovery_document['token_endpoint'], data=data, verify=False)
                response_json = response.json()

                self._access_token = response_json['access_token']
                self._refresh_token = response_json['refresh_token']
                self._expires_in = response_json['expires_in']
            except Exception as exc:
                self._access_token = None
                self._refresh_token = None
                self._expires_in = None
                raise ValueError('Could not obtain access token for the specified client.') from exc

        return self._access_token, self._expires_in

    def get_access_token_cc(self) -> str:
        if not self._access_token:

            data = {
                'client_id': CONFIG['client_id'],
                'client_secret': CONFIG['client_secret'],
                'grant_type': 'client_credentials',
                'scopes': CONFIG['scopes'],
            }

            if not self._discovery_document:
                self.get_discovery_document()

            try:
                response = requests.post(self._discovery_document['token_endpoint'], data=data, verify=False)
                response_json = response.json()

                self._access_token = response_json['access_token']
                self._refresh_token = None
                self._expires_in = response_json['expires_in']
            except Exception as exc:
                self._access_token = None
                self._refresh_token = None
                self._expires_in = None
                raise ValueError('Could not obtain access token for the specified client.') from exc

        return self._access_token, self._expires_in
    
    def get_access_token_pw(self) -> str:
        if not self._access_token:

            data = {
                'client_id': CONFIG['client_id'],
                'client_secret': CONFIG['client_secret'],
                'username': CONFIG['username'],
                'tenant': CONFIG['tenant'],
                'password': CONFIG['password'],
                'grant_type': 'password',
                'scopes': CONFIG['scopes'],
            }

            if not self._discovery_document:
                self.get_discovery_document()

            try:
                response = requests.post(self._discovery_document['token_endpoint'], data=data, verify=False)
                response_json = response.json()

                print(response_json)

                self._access_token = response_json['access_token']
                self._refresh_token = None
                self._expires_in = response_json['expires_in']
            except Exception as exc:
                self._access_token = None
                self._refresh_token = None
                self._expires_in = None
                raise ValueError('Could not obtain access token for the specified client.') from exc
            
        return self._access_token, self._expires_in
    
    def get_refresh_access_token(self) -> str:
        if not self._refresh_token:
            raise ValueError('Could not find refresh token. Please call get_access_token() first.')

        data = {
            'grant_type': 'refresh_token',
            'client_id': CONFIG['client_id'],
            'refresh_token': self._refresh_token
        }

        if not self._discovery_document:
            self.get_discovery_document()

        try:
            response = requests.post(self._discovery_document['token_endpoint'], data=data, verify=False)
            response_json = response.json()

            self._access_token = response_json['access_token']
            self._refresh_token = response_json['refresh_token']
            self._expires_in = response_json['expires_in']
        except Exception as exc:
            self._access_token = None
            self._refresh_token = None
            self._expires_in = None
            raise ValueError('Could not refresh access token for the specified client.') from exc

        return self._access_token, self._expires_in
    
    def get_user_info(self) -> Dict[str, Any]:
        if not self._access_token:
            raise ValueError('Could not find access token. Please call get_access_token() first.')

        if not self._discovery_document:
            self.get_discovery_document()

        headers = {
            'Authorization': 'Bearer ' + self._access_token
        }

        try:
            response = requests.get(self._discovery_document['userinfo_endpoint'], headers=headers, verify=False)
            return response.json()
        except Exception as exc:
            raise ValueError('Could not obtain user info for the specified client.') from exc

    def get_code_verifier(self) -> str:
        if not self._code_verifier:
            rand = random.SystemRandom()
            self._code_verifier = ''.join(rand.choices(string.ascii_letters + string.digits, k=128))
        
        return self._code_verifier
        
    def generate_code_challenge(self) -> str:
        if not self._code_challenge:
            code_sha_256 = hashlib.sha256(self._code_verifier.encode('utf-8')).digest()
            b64 = base64.urlsafe_b64encode(code_sha_256)
            self._code_challenge = b64.decode('utf-8').replace('=', '')
        
        return self._code_challenge