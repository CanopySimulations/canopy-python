from typing import Dict, Any, Optional

import canopy


class DynamicDictToObject:
    def __init__(self, data: Dict[str, Dict]):
        self._data = data

    def __getattr__(self, name: str):
        result: Optional[Any] = None
        if name in self._data:
            result = canopy.dict_to_object(self._data[name])

        setattr(self, name, result)
        return result
