from typing import Optional, Dict

import canopy


class TenantUsersCache(object):

    def __init__(self, client: canopy.openapi.ApiClient, authentication: canopy.Authentication):
        self._client = client
        self._authentication = authentication
        self._data: Dict[str, canopy.TenantUsers] = {}

    def reload(self, tenant_id: Optional[str] = None):
        if tenant_id is None:
            tenant_id = self._authentication.tenant_id

        api = canopy.openapi.TenancyApi(self._client)
        result: canopy.openapi.GetTenantUsersQueryResult = api.tenancy_get_tenant_users(tenant_id)
        self._data[tenant_id] = canopy.TenantUsers(result)

    def get(self, tenant_id: Optional[str] = None) -> canopy.TenantUsers:
        if tenant_id is None:
            tenant_id = self._authentication.tenant_id

        if tenant_id not in self._data:
            self.reload(tenant_id)

        if tenant_id not in self._data:
            raise RuntimeError('Users for tenant ID not found.')

        return self._data[tenant_id]
