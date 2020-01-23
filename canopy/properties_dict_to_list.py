from typing import Optional, Dict, List, Union

import canopy


def properties_dict_to_list(properties: Optional[Union[Dict[str, str], object]]) -> List[canopy.swagger.DocumentCustomPropertyData]:
    properties_list: List[canopy.swagger.DocumentCustomPropertyData] = []
    if properties is not None:
        properties = canopy.ensure_dict(properties)
        for name, value in properties.items():
            properties_list.append(canopy.swagger.DocumentCustomPropertyData(
                name=name,
                value=value))

    return properties_list
