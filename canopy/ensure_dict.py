from typing import Dict, Union, Optional


def ensure_dict(value: Optional[Union[Dict, object]]) -> Optional[Dict]:
    if value is None:
        return value

    if isinstance(value, dict):
        return value

    return vars(value)
