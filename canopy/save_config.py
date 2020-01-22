from typing import Optional, Any

import canopy


async def save_config(
        session: canopy.Session,
        config: canopy.swagger.CanopyDocument,
        config_data: Optional[Any]):

    config_api = canopy.swagger.ConfigApi(session.async_client)

    updated_config_data = canopy.swagger.UpdatedConfigData(
        config.name,
        config.sub_type,
        config.properties,
        config_data if config_data is not None else config.data,
        config.notes,
        config.sim_version)

    await config_api.config_put_config(
        config.tenant_id,
        config.document_id,
        updated_config_data,
        **canopy.defined_kwargs(
            sub_tree_path=config.data['path'] if config.type == canopy.Constants.config_sub_tree_document_type else None))
