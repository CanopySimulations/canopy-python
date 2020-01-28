from typing import Dict, Union
from munch import Munch


def dict_to_object(data: Union[Dict, object]):
    if isinstance(data, Munch):
        return data
    return Munch.fromDict(data)
