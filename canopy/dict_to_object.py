from typing import Dict, Union
from collections import namedtuple
from munch import Munch


def dict_to_object(data: Union[Dict, object], deep: bool = True):
    if deep:
        return Munch.fromDict(data)
    else:
        return namedtuple('Struct', data.keys())(*data.values())
