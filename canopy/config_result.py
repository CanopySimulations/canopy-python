from typing import Any, Optional

import canopy
import json


class ConfigResult:
    _converted_data: Optional[Any] = None

    def __init__(self, document: canopy.openapi.CanopyDocument, user_information: canopy.openapi.DocumentUserInformation):
        self._document = document
        self._user_information = user_information

    @property
    def document(self) -> canopy.openapi.CanopyDocument:
        return self._document

    @property
    def config_id(self) -> str:
        return self._document.document_id

    @property
    def data(self) -> Any:
        if self._converted_data is None:
            self._converted_data = canopy.dict_to_object(self._get_raw_data())
        return self._converted_data

    @property
    def is_data_converted(self) -> bool:
        return self._converted_data is not None

    @property
    def raw_data(self) -> Any:
        return self._converted_data if self.is_data_converted else self.document.data

    @property
    def user_information(self) -> canopy.openapi.DocumentUserInformation:
        return self._user_information

    def to_local_config(self):
        return canopy.LocalConfig(
            self.document.sub_type,
            self.document.name,
            self.raw_data,
            properties=canopy.ensure_dict(self.document.properties),
            notes=self.document.notes,
            config_id=self.document.document_id,
            user_id=self.document.user_id,
            is_edited=False)

    def _get_raw_data(self):
        if self._document.sub_type == canopy.Constants.config_sub_tree_document_type:
            return self._document.data['definition']
        else:
            return self._document.data

    def to_dict(self):
        return {
            'config_id': self.config_id,
            'document': self._document.to_dict(),
            'user_information': self._user_information.to_dict(),
            'is_data_converted': self.is_data_converted,
            'data': self.raw_data
        }

    def __repr__(self):
        return 'canopy.ConfigResult(%r,%r)' % \
               (self._document, self._user_information)

    def __str__(self):
        return json.dumps(self.to_dict(), indent=2, default=str)
