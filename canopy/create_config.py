from typing import Optional, Dict, Any

import canopy


async def create_config(
        session: canopy.Session,
        config_type: str,
        name: str,
        config: Any,
        properties: Optional[Dict[str, str]] = None,
        notes: Optional[str] = None,
        sim_version: Optional[str] = None,
        sub_tree_path: Optional[str] = None) -> str:

    session.authentication.authenticate()
    tenant_id = session.authentication.tenant_id

    config_api = canopy.swagger.ConfigApi(session.async_client)
    config_id = await config_api.config_post_config(
        tenant_id,
        canopy.swagger.NewConfigData(
            name=name,
            config_type=config_type,
            properties=properties,
            config=config,
            notes=notes,
            sim_version=sim_version),
        **canopy.defined_kwargs(
            sub_tree_path=sub_tree_path))

    return config_id
