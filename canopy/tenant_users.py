from typing import Sequence, Optional

import canopy


class TenantUsers:
    def __init__(
            self,
            result: canopy.openapi.GetTenantUsersQueryResult):
        self._list = result.users
        self._by_user_id = {item.user_id: item for item in result.users}
        self._by_username = {item.username: item for item in result.users}

    @property
    def list(self) -> Sequence[canopy.openapi.GetTenantUsersQueryResultUserItem]:
        return self._list

    def get_by_user_id(self, user_id: str) -> Optional[canopy.openapi.GetTenantUsersQueryResultUserItem]:
        if user_id in self._by_user_id:
            return self._by_user_id[user_id]
        else:
            raise canopy.NotFoundError('Unknown user ID ' + user_id)

    def get_by_username(self, username: str) -> Optional[canopy.openapi.GetTenantUsersQueryResultUserItem]:
        if username in self._by_username:
            return self._by_username[username]
        else:
            raise canopy.NotFoundError('Unknown username ' + username)
