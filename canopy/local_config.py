from typing import Any, Dict, Optional


class LocalConfig(object):
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
        self.data = data
        self.properties = properties
        self.notes = notes
        self.user_id = user_id
        self.config_id = config_id
        self.is_edited = is_edited

    @property
    def config_type(self) -> str:
        return self._config_type
