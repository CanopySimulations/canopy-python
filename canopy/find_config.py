from typing import Optional, List, Dict

import canopy
import json


async def find_config(
        session: canopy.Session,
        config_type: str,
        name: Optional[str] = None,
        owner_username: Optional[str] = None,
        custom_properties: Dict[str, str] = None,
        parent_worksheet_id: Optional[str] = None,
        sub_tree_path: Optional[str] = None,
        tenant_id: Optional[str] = None,
        sim_version: Optional[str] = None) -> canopy.ConfigResult:

    session.authentication.authenticate()

    if tenant_id is None:
        tenant_id = session.authentication.tenant_id

    config_api = canopy.openapi.ConfigApi(session.async_client)

    filter_ = canopy.create_list_filter(
        session,
        is_study=False,
        name=name,
        items_per_page=1,
        owner_username=owner_username,
        custom_properties=custom_properties,
        parent_worksheet_id=parent_worksheet_id,
        tenant_id=tenant_id)

    metadata_result: canopy.openapi.GetConfigsQueryResult = await config_api.config_get_configs(
        tenant_id,
        config_type,
        **canopy.defined_kwargs(
            filter=filter_.serialize(),
            sub_tree_path=sub_tree_path))

    documents: List[canopy.openapi.CanopyDocument] = metadata_result.query_results.documents
    if len(documents) == 0:
        raise canopy.NotFoundError('No config found matching the specified criteria.')

    document = documents[0]
    return await canopy.load_config(
        session,
        document.document_id,
        tenant_id=tenant_id,
        sub_tree_path=sub_tree_path,
        sim_version=sim_version)
