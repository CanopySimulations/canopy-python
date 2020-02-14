from typing import Optional

import canopy


async def delete_study(
        session: canopy.Session,
        study_id: str,
        tenant_id: Optional[str] = None,
        undelete: Optional[bool] = False) -> None:

    session.authentication.authenticate()

    if tenant_id is None:
        tenant_id = session.authentication.tenant_id

    study_api = canopy.openapi.StudyApi(session.async_client)
    await study_api.study_delete_study(
        tenant_id,
        study_id,
        **canopy.defined_kwargs(
            undelete=undelete))
