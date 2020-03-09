from typing import Optional, Dict
from urllib3 import make_headers


class ProxyConfiguration(object):
    def __init__(
            self,
            url: str,
            username: Optional[str] = None,
            password: Optional[str] = None):

        self._url = url
        self._username = username
        self._password = password

        if '://' not in url:
            raise RuntimeError('Proxy URL must contain scheme such as "http://" or "https://".')

        headers = None
        auth_url = url
        if username is not None and password is not None:
            auth_string = f'{username}:{password}'
            headers = make_headers(proxy_basic_auth=auth_string)
            auth_url = url.replace('://', f'://{auth_string}@')

        self._headers = headers
        self._auth_url = auth_url

    @property
    def url(self) -> str:
        return self._url

    @property
    def username(self) -> Optional[str]:
        return self._username

    @property
    def password(self) -> Optional[str]:
        return self._password

    @property
    def auth_url(self) -> str:
        return self._auth_url

    @property
    def headers(self) -> Dict[str, str]:
        return self._headers
