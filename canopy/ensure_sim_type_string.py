from typing import Optional


def ensure_sim_type_string(value: Optional[str]) -> Optional[str]:
    if value is None or len(value) == 0 or value[0].isupper():
        return value

    return value[0].upper() + value[1:]
