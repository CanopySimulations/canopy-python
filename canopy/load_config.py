from typing import Optional

import canopy


async def load_config(
        session: canopy.Session,
        config_id: str,
        tenant_id: Optional[str] = None,
        sub_tree_path: Optional[str] = None,
        sim_version: Optional[str] = None) -> canopy.ConfigResult:

    session.authentication.authenticate()

    if tenant_id is None:
        tenant_id = session.authentication.tenant_id

    config_api = canopy.openapi.ConfigApi(session.async_client)
    config_result: canopy.openapi.GetConfigQueryResult = await config_api.config_get_config(
        tenant_id,
        config_id,
        **canopy.defined_kwargs(
            sim_version=sim_version,
            sub_tree_path=sub_tree_path))

    return canopy.ConfigResult(config_result.config, config_result.user_information)
