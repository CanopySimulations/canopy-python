from typing import Optional, List, Dict

import canopy


def create_list_filter(
        session: canopy.Session,
        is_study: bool,
        name: Optional[str] = None,
        items_per_page: Optional[int] = None,
        owner_username: Optional[str] = None,
        custom_properties: Dict[str, str] = None,
        parent_worksheet_id: Optional[str] = None,
        tenant_id: Optional[str] = None) -> canopy.SerializableValue[canopy.openapi.ListFilter]:

    conditions: List[canopy.openapi.ListFilterCondition] = []

    if name is not None:
        conditions.append(canopy.openapi.ListFilterCondition(
            source='metadata',
            name='name',
            operator='equals',
            value=name
        ))

    if owner_username is not None:
        tenant_users = session.tenant_users.get(tenant_id)
        author = tenant_users.get_by_username(owner_username)
        conditions.append(canopy.openapi.ListFilterCondition(
            source='metadata',
            name='userId',
            operator='equals',
            value=author.user_id
        ))

    if parent_worksheet_id is not None:
        conditions.append(canopy.openapi.ListFilterCondition(
            source='metadata',
            name='parentWorksheetId',
            operator='equals',
            value=parent_worksheet_id
        ))

    if custom_properties is not None:
        for key, value in custom_properties.items():
            conditions.append(canopy.openapi.ListFilterCondition(
                source='customProperty',
                name=key,
                operator='equals',
                value=value
            ))

    query: Optional[canopy.openapi.ListFilterGroup] = None
    if len(conditions) > 0:
        query = canopy.openapi.ListFilterGroup(
                operator='and',
                conditions=conditions)

    return canopy.SerializableValue(
        session,
        canopy.openapi.ListFilter(
            items_per_page=items_per_page,
            order_by_property='creationDate' if is_study else 'modifiedDate',
            order_by_descending=True,
            query=query,
            include_if_has_parent_worksheet=(parent_worksheet_id is not None)))
