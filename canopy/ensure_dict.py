from typing import Dict, Union


def ensure_dict(value: Union[Dict, object]) -> Dict:
    if isinstance(value, dict):
        return value

    return vars(value)