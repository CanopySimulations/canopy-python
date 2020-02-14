from typing import Optional, List, Dict

import canopy


async def find_study(
        session: canopy.Session,
        name: Optional[str] = None,
        owner_username: Optional[str] = None,
        custom_properties: Dict[str, str] = None,
        parent_worksheet_id: Optional[str] = None,
        tenant_id: Optional[str] = None) -> canopy.StudyResult:

    session.authentication.authenticate()

    if tenant_id is None:
        tenant_id = session.authentication.tenant_id

    study_api = canopy.openapi.StudyApi(session.async_client)

    filter_ = canopy.create_list_filter(
        session,
        is_study=True,
        name=name,
        items_per_page=1,
        owner_username=owner_username,
        custom_properties=custom_properties,
        parent_worksheet_id=parent_worksheet_id,
        tenant_id=tenant_id)

    metadata_result: canopy.openapi.GetConfigsQueryResult = await study_api.study_get_studies(
        tenant_id,
        **canopy.defined_kwargs(
            filter=filter_.serialize()))

    documents: List[canopy.openapi.CanopyDocument] = metadata_result.query_results.documents
    if len(documents) == 0:
        raise canopy.NotFoundError('No study found matching the specified criteria.')

    return canopy.StudyResult(
        session,
        None,
        None,
        document=documents[0])
