from typing import Optional, List, Mapping

import canopy


class UserSettingsCache(object):

    def __init__(self, client: canopy.openapi.ApiClient, authentication: canopy.Authentication):
        self._client = client
        self._authentication = authentication
        self._data: Optional[canopy.openapi.UserSettings] = None
        self._units: Optional[Mapping[str, str]] = None

    def reload(self):
        user_settings_api = canopy.openapi.UserSettingsApi(self._client)
        user_settings_result: canopy.openapi.GetUserSettingsQueryResult = user_settings_api.user_settings_get_user_settings(
            self._authentication.tenant_id,
            self._authentication.user_id)

        user_settings: canopy.openapi.UserSettings = user_settings_result.settings
        self._data = user_settings
        channels: List[canopy.openapi.ChannelSettings] = user_settings.channels
        self._units = {item.name: item.units for item in channels}

    def load_if_required(self):
        if self._data is None:
            self.reload()

    @property
    def data(self) -> canopy.openapi.UserSettings:
        if self._data is None:
            self.reload()

        if self._data is None:
            raise RuntimeError('User settings not found.')

        return self._data

    def get_channel_units(self, channel_name: str) -> Optional[str]:
        if self._units is None:
            self.reload()

        if self._units is None:
            raise RuntimeError('User settings not found.')

        if channel_name in self._units:
            return self._units[channel_name]

        return None
