from typing import Optional


class AuthenticationData(object):
    def __init__(
            self,
            client_id: Optional[str] = None,
            client_secret: Optional[str] = None,
            username: Optional[str] = None,
            tenant_name: Optional[str] = None,
            password: Optional[str] = None):
        self._client_id = client_id
        self._client_secret = client_secret
        self._username = username
        self._tenant_name = tenant_name
        self._password = password

    @property
    def client_id(self) -> Optional[str]:
        return self._client_id

    @property
    def client_secret(self) -> Optional[str]:
        return self._client_secret

    @property
    def username(self) -> Optional[str]:
        return self._username

    @property
    def tenant_name(self) -> Optional[str]:
        return self._tenant_name

    @property
    def password(self) -> Optional[str]:
        return self._password
