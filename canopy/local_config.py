from typing import Any, Dict, Optional

import canopy


class LocalConfig(object):
    _converted_data: Optional[Any] = None

    def __init__(
            self,
            config_type: str,
            name: str,
            data: Any,
            properties: Optional[Dict[str, str]] = None,
            notes: Optional[str] = None,
            user_id: Optional[str] = None,
            config_id: Optional[str] = None,
            is_edited: bool = False):

        self._config_type = config_type
        self.name = name
        self._data = data
        self.properties = properties
        self.notes = notes
        self.user_id = user_id
        self.config_id = config_id
        self.is_edited = is_edited

    @property
    def config_type(self) -> str:
        return self._config_type

    @property
    def data(self) -> Any:
        if self._converted_data is None:
            if self._config_type == canopy.Constants.config_sub_tree_document_type:
                self._converted_data = canopy.dict_to_object(self._data['definition'])
            else:
                self._converted_data = canopy.dict_to_object(self._data)
        return self._converted_data

    @property
    def is_data_converted(self) -> bool:
        return self._converted_data is not None

    @property
    def raw_data(self) -> Any:
        return self._converted_data if self.is_data_converted else self._data
