from typing import Any, Optional

import canopy


class ConfigResult:
    _config_data: Optional[Any] = None

    def __init__(self, document: canopy.swagger.CanopyDocument, user_information: canopy.swagger.DocumentUserInformation):
        self._document = document
        self._user_information = user_information

    @property
    def document(self) -> canopy.swagger.CanopyDocument:
        return self._document

    @property
    def config_data(self) -> Any:
        if self._config_data is None:
            if self._document.sub_type == canopy.Constants.config_sub_tree_document_type:
                self._config_data = canopy.dict_to_object(self._document.data['definition'], deep=True)
            else:
                self._config_data = canopy.dict_to_object(self._document.data, deep=True)
        return self._config_data

    @property
    def is_config_data_converted(self) -> bool:
        return self._config_data is not None

    @property
    def user_information(self) -> canopy.swagger.DocumentUserInformation:
        return self._user_information

    def to_local_config(self):
        return canopy.LocalConfig(
            self.document.sub_type,
            self.document.name,
            self.config_data if self.is_config_data_converted else self.document.data,
            properties=canopy.ensure_dict(self.document.properties),
            notes=self.document.notes,
            config_id=self.document.document_id,
            user_id=self.document.user_id,
            is_edited=False)