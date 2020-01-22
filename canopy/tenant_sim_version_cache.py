from typing import Optional, Dict

import canopy


class TenantSimVersionCache(object):

    def __init__(self, client: canopy.swagger.ApiClient, authentication: canopy.Authentication):
        self._client = client
        self._authentication = authentication
        self._data: Dict[str, str] = {}

    def reload(self, tenant_id: Optional[str] = None):
        if tenant_id is None:
            tenant_id = self._authentication.tenant_id

        api = canopy.swagger.TenantSettingsApi(self._client)
        result: canopy.swagger.GetTenantSettingsSimVersionQueryResult = api.tenant_settings_get_tenant_settings_sim_version(tenant_id)
        self._data[tenant_id] = result.sim_version

    def get(self, tenant_id: Optional[str] = None) -> str:
        if tenant_id is None:
            tenant_id = self._authentication.tenant_id

        if tenant_id not in self._data:
            self.reload(tenant_id)

        if tenant_id not in self._data:
            raise RuntimeError('Sim version for tenant ID not found.')

        return self._data[tenant_id]
