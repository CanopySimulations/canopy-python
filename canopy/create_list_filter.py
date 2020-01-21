from typing import Optional, List, Dict

import canopy


def create_list_filter(
        session: canopy.Session,
        name: Optional[str] = None,
        items_per_page: Optional[int] = None,
        owner_username: Optional[str] = None,
        custom_properties: Dict[str, str] = None,
        parent_worksheet_id: Optional[str] = None,
        tenant_id: Optional[str] = None) -> Optional[canopy.SerializableValue[canopy.swagger.ListFilter]]:

    conditions: List[canopy.swagger.ListFilterCondition] = []

    if owner_username is not None:
        tenant_users = session.tenant_users.get(tenant_id)
        author = tenant_users.get_by_username(owner_username)
        conditions.append(canopy.swagger.ListFilterCondition(
            source='metadata',
            name='userId',
            operator='equals',
            value=author.user_id
        ))

    if parent_worksheet_id is not None:
        conditions.append(canopy.swagger.ListFilterCondition(
            source='metadata',
            name='parentWorksheetId',
            operator='equals',
            value=parent_worksheet_id
        ))

    if custom_properties is not None:
        for key, value in custom_properties.items():
            conditions.append(canopy.swagger.ListFilterCondition(
                source='customProperty',
                name=key,
                operator='equals',
                value=value
            ))

    if len(conditions) == 0:
        return None

    return canopy.SerializableValue(
        session,
        canopy.swagger.ListFilter(
            items_per_page=items_per_page,
            filter_name=name,
            query=canopy.swagger.ListFilterGroup(
                operator='and',
                conditions=conditions),
            include_if_has_parent_worksheet=(parent_worksheet_id is not None)))
