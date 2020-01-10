import numpy as np


class LoadedChannel:
    def __init__(self, name: str, units: str, data: np.array):
        self._name = name
        self._units = units
        self._data = data

    @property
    def name(self) -> str:
        return self._name

    @property
    def units(self) -> str:
        return self._units

    @property
    def data(self) -> np.array:
        return self._data
