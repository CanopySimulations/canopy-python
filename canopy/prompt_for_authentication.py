from typing import Optional

import canopy
import getpass


def prompt_for_authentication(
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        username: Optional[str] = None,
        tenant_name: Optional[str] = None,
        password: Optional[str] = None) -> canopy.AuthenticationData:

    if client_id is None:
        client_id = input('Client ID:')
    if client_secret is None:
        client_secret = getpass.getpass(prompt='Client Secret:')

    if username is None:
        username = input('Username:')
    if tenant_name is None:
        tenant_name = client_id

    if password is None:
        password = getpass.getpass(prompt='Password:')

    return canopy.AuthenticationData(
        client_id=client_id,
        client_secret=client_secret,
        username=username,
        tenant_name=tenant_name,
        password=password)
