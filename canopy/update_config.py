from typing import Optional, Any, List

import canopy


async def update_config(
        session: canopy.Session,
        config: canopy.openapi.CanopyDocument,
        config_data: Optional[Any]):

    config_api = canopy.openapi.ConfigApi(session.async_client)

    properties_list = canopy.properties_dict_to_list(config.properties)
    updated_config_data = canopy.openapi.UpdatedConfigData(
        config.name,
        config.sub_type,
        properties_list,
        config_data if config_data is not None else config.data,
        config.notes,
        config.sim_version)

    await config_api.config_put_config(
        config.tenant_id,
        config.document_id,
        updated_config_data,
        **canopy.defined_kwargs(
            sub_tree_path=config.data['path'] if config.type == canopy.Constants.config_sub_tree_document_type else None))
