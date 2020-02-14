from typing import Optional, Dict, Any, List

import canopy


async def create_config(
        session: canopy.Session,
        config_type: str,
        name: str,
        config_data: Any,
        properties: Optional[Dict[str, str]] = None,
        notes: Optional[str] = None,
        sim_version: Optional[str] = None,
        sub_tree_path: Optional[str] = None) -> str:

    session.authentication.authenticate()
    tenant_id = session.authentication.tenant_id

    properties_list: List[canopy.openapi.DocumentCustomPropertyData] = canopy.properties_dict_to_list(properties)

    config_api = canopy.openapi.ConfigApi(session.async_client)
    config_id = await config_api.config_post_config(
        tenant_id,
        canopy.openapi.NewConfigData(
            name=name,
            config_type=config_type,
            properties=properties_list,
            config=config_data,
            notes=notes,
            sim_version=sim_version),
        **canopy.defined_kwargs(
            sub_tree_path=sub_tree_path))

    return config_id
