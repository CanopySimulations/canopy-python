from typing import Optional, Dict, List, Union

import canopy


def properties_dict_to_list(properties: Optional[Union[Dict[str, str], object]]) -> List[canopy.openapi.DocumentCustomPropertyData]:
    properties_list: List[canopy.openapi.DocumentCustomPropertyData] = []
    if properties is not None:
        properties = canopy.ensure_dict(properties)
        for name, value in properties.items():
            properties_list.append(canopy.openapi.DocumentCustomPropertyData(
                name=name,
                value=value))

    return properties_list
