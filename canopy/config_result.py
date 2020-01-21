from typing import Any, Optional

import canopy


class ConfigResult:
    _config_data: Optional[Any]

    def __init__(self, config: canopy.swagger.CanopyDocument, user_information: canopy.swagger.DocumentUserInformation):
        self._config = config
        self._user_information = user_information

    @property
    def config(self) -> canopy.swagger.CanopyDocument:
        return self._config

    @property
    def config_data(self) -> Any:
        if self._config_data is None:
            if self._config.sub_type == canopy.Constants.config_sub_tree_config_type:
                self._config_data = canopy.dict_to_object(self._config.data['definition'], deep=True)
            else:
                self._config_data = canopy.dict_to_object(self._config.data, deep=True)
        return self._config_data

    @property
    def user_information(self) -> canopy.swagger.DocumentUserInformation:
        return self._user_information
