from typing import Optional

import canopy
import json


async def load_default_config(
        session: canopy.Session,
        config_type: str,
        name: str,
        sim_version: Optional[str] = None) -> canopy.LocalConfig:

    session.authentication.authenticate()

    document_path = canopy.get_default_config_path(session, config_type, name)

    if sim_version is None:
        sim_version = session.tenant_sim_version.get()

    api = canopy.openapi.SimVersionApi(session.async_client)
    document_result: canopy.openapi.GetSimVersionDocumentQueryResult = await api.sim_version_get_document(sim_version, document_path)

    config_data = json.loads(document_result.document.content)

    return canopy.LocalConfig(
        config_type,
        name,
        config_data)
