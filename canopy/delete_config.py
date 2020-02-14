from typing import Optional

import canopy


async def delete_config(
        session: canopy.Session,
        config_id: str,
        tenant_id: Optional[str] = None,
        undelete: Optional[bool] = False) -> None:

    session.authentication.authenticate()

    if tenant_id is None:
        tenant_id = session.authentication.tenant_id

    config_api = canopy.openapi.ConfigApi(session.async_client)
    await config_api.config_delete_config(
        tenant_id,
        config_id,
        **canopy.defined_kwargs(
            undelete=undelete))
