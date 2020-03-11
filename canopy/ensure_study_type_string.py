from typing import Optional


def ensure_study_type_string(value: Optional[str]) -> Optional[str]:
    if value is None or len(value) == 0 or value[0].islower():
        return value

    return value[0].lower() + value[1:]