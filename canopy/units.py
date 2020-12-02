import math
import pandas as pd
import numpy as np
from typing import Optional, Union


class UnitDefinition:
    def __init__(self, target_unit: str, si_unit: str, factor: float = 1, offset: float = 0):
        self.target_unit = target_unit
        self.si_unit = si_unit
        self.factor = factor
        self.offset = offset


class ConversionBetweenUnits:
    def __init__(
          self,
          factor_to_si: float,
          offset_to_si: float,
          factor_from_si: float,
          offset_from_si: float,
          is_conversion_required: bool):
        self.factor_to_si = factor_to_si
        self.offset_to_si = offset_to_si
        self.factor_from_si = factor_from_si
        self.offset_from_si = offset_from_si
        self.is_conversion_required = is_conversion_required


def create_default_units():
    units_list = [
        # list SI ones first so they are always at the top of the suggested list
        UnitDefinition('()', '()', factor=1, offset=0),
        UnitDefinition('m', 'm', factor=1, offset=0),
        UnitDefinition('kg', 'kg', factor=1, offset=0),
        UnitDefinition('N', 'N', factor=1, offset=0),
        UnitDefinition('m/s', 'm/s', factor=1, offset=0),
        UnitDefinition('rad', 'rad', factor=1, offset=0),
        UnitDefinition('Pa', 'Pa', factor=1, offset=0),
        UnitDefinition('rad/s', 'rad/s', factor=1, offset=0),
        UnitDefinition('Nm', 'Nm', factor=1, offset=0),
        UnitDefinition('m/s2', 'm/s2', factor=1, offset=0),
        UnitDefinition('W', 'W', factor=1, offset=0),
        UnitDefinition('J', 'J', factor=1, offset=0),
        UnitDefinition('s', 's', factor=1, offset=0),
        UnitDefinition('K', 'K', factor=1, offset=0),
        UnitDefinition('N/rad', 'N/rad', factor=1, offset=0),
        UnitDefinition('Nm/rad', 'Nm/rad', factor=1, offset=0),
        UnitDefinition('N/m', 'N/m', factor=1, offset=0),
        UnitDefinition('rad/s2', 'rad/s2', factor=1, offset=0),
        UnitDefinition('kg/s', 'kg/s', factor=1, offset=0),
        UnitDefinition('Ns/m', 'Ns/m', factor=1, offset=0),

        # now start listing all the horrible non-SI ones that people like
        UnitDefinition('', '()', factor=1, offset=0),
        UnitDefinition('%', '()', factor=0.01, offset=0),
        UnitDefinition('pt', '()', factor=0.01, offset=0),
        UnitDefinition('e-3', '()', factor=1e-3, offset=0),
        UnitDefinition('e-6', '()', factor=1e-6, offset=0),

        UnitDefinition('N/m2', 'Pa', factor=1, offset=0),
        UnitDefinition('bar', 'Pa', factor=1e5, offset=0),
        UnitDefinition('mbar', 'Pa', factor=1e5 * 0.001, offset=0),
        UnitDefinition('psi', 'Pa', factor=6894.76, offset=0),
        UnitDefinition('inHg', 'Pa', factor=3386.39, offset=0),

        UnitDefinition('gm', 'kg', factor=0.001, offset=0),
        UnitDefinition('lbm', 'kg', factor=0.45359237, offset=0),
        UnitDefinition('st', 'kg', factor=6.35029318, offset=0),

        UnitDefinition('lbf', 'N', factor=4.448222, offset=0),
        UnitDefinition('kN', 'N', factor=1e3, offset=0),
        UnitDefinition('MN', 'N', factor=1e6, offset=0),
        UnitDefinition('GN', 'N', factor=1e9, offset=0),

        UnitDefinition('ms', 's', factor=0.001, offset=0),
        UnitDefinition('ks', 's', factor=1000, offset=0),

        UnitDefinition('mm', 'm', factor=0.001, offset=0),
        UnitDefinition('cm', 'm', factor=0.01, offset=0),
        UnitDefinition('km', 'm', factor=1000, offset=0),
        UnitDefinition('miles', 'm', factor=1609.344, offset=0),
        UnitDefinition('in', 'm', factor=0.0254, offset=0),
        UnitDefinition('ft', 'm', factor=0.3048, offset=0),
        UnitDefinition('yd', 'm', factor=0.9144, offset=0),

        UnitDefinition('kph', 'm/s', factor=1 / 3.6, offset=0),
        UnitDefinition('mph', 'm/s', factor=0.44704, offset=0),
        UnitDefinition('mm/s', 'm/s', factor=0.001, offset=0),
        UnitDefinition('kn', 'm/s', factor=0.514444, offset=0),
        UnitDefinition('in/s', 'm/s', factor=0.0254, offset=0),

        UnitDefinition('g', 'm/s2', factor=9.80665, offset=0),

        UnitDefinition('deg', 'rad', factor=math.pi / 180, offset=0),
        UnitDefinition('°', 'rad', factor=math.pi / 180, offset=0),

        UnitDefinition('rpm', 'rad/s', factor=math.pi / 30, offset=0),
        UnitDefinition('deg/s', 'rad/s', factor=math.pi / 180, offset=0),
        UnitDefinition('°/s', 'rad/s', factor=math.pi / 180, offset=0),

        UnitDefinition('Nm/deg', 'Nm/rad', factor=180 / math.pi, offset=0),

        UnitDefinition('kW', 'W', factor=1e3, offset=0),
        UnitDefinition('MW', 'W', factor=1e6, offset=0),
        UnitDefinition('GW', 'W', factor=1e9, offset=0),

        UnitDefinition('kJ', 'J', factor=1e3, offset=0),
        UnitDefinition('MJ', 'J', factor=1e6, offset=0),
        UnitDefinition('GJ', 'J', factor=1e9, offset=0),
        UnitDefinition('kWh', 'J', factor=1e3 * 60 * 60, offset=0),

        UnitDefinition('kPa', 'Pa', factor=1e3, offset=0),
        UnitDefinition('MPa', 'Pa', factor=1e6, offset=0),
        UnitDefinition('GPa', 'Pa', factor=1e9, offset=0),

        UnitDefinition('kNm', 'Nm', factor=1e3, offset=0),
        UnitDefinition('MNm', 'Nm', factor=1e6, offset=0),
        UnitDefinition('GNm', 'Nm', factor=1e9, offset=0),

        UnitDefinition('C', 'K', factor=1, offset=273.15),
        UnitDefinition('°C', 'K', factor=1, offset=273.15),
        UnitDefinition('F', 'K', factor=5 / 9, offset=459.67 * 5 / 9),

        UnitDefinition('N/mm', 'N/m', factor=1000, offset=0),
        UnitDefinition('lbf/in', 'N/m', factor=175.127, offset=0),

        UnitDefinition('lbfs/in', 'Ns/m', factor=175.127, offset=0),
    ]

    return {units_list[i].target_unit: units_list[i] for i in range(0, len(units_list))}


class Units(object):
    def __init__(self):
        self.to_si_table = create_default_units()

    def try_get_conversion_to_si(self, unit: str) -> Optional[UnitDefinition]:
        if unit in self.to_si_table:
            return self.to_si_table[unit]

        return None

    def get_conversion_to_si(self, unit: str) -> UnitDefinition:
        return self.to_si_table[unit]

    def get_conversion_to_si_or_default(self, unit: str) -> UnitDefinition:
        result = self.try_get_conversion_to_si(unit)
        if result is None:
            return UnitDefinition(unit, unit, 1, 0)

        return result

    def convert_value_to_si(self, value: float, source_unit: str, apply_factor_only: bool = False) -> float:
        conversion_to_si = self.get_conversion_to_si(source_unit)
        factor = conversion_to_si.factor
        offset = 0 if apply_factor_only else conversion_to_si.offset
        return value * factor + offset

    def convert_value_from_si(self, value: float, target_unit: str, apply_factor_only: bool = False) -> float:
        conversion_to_si = self.get_conversion_to_si(target_unit)
        factor = conversion_to_si.factor
        offset = 0 if apply_factor_only else conversion_to_si.offset
        return (value - offset) / factor

    def convert_value_between_units(self, value: float, source_unit: str, target_unit: str, apply_factor_only: bool = False) -> float:
        return self.convert_value_from_si(self.convert_value_to_si(value, source_unit, apply_factor_only), target_unit, apply_factor_only)

    def _convert_values_to_si(self, values: Union[np.array, pd.Series], source_unit: str, inplace: bool = False) -> Union[np.array, pd.Series]:
        if values is None:
            return None

        conversion_to_si = self.get_conversion_to_si(source_unit)
        factor = conversion_to_si.factor
        offset = conversion_to_si.offset

        result = values

        if inplace:
            if factor != 1:
                result *= factor

            if offset != 0:
                result += offset
        else:
            if factor != 1:
                result = result * factor

            if offset != 0:
                result = result + offset

        return result

    def convert_array_to_si(self, values: np.array, source_unit: str, inplace: bool = False, always_return_copy: bool = False) -> np.array:
        result = self._convert_values_to_si(values, source_unit, inplace=inplace)
        return np.copy(result) if result is not None and result is values and always_return_copy else result

    def convert_series_to_si(self, values: pd.Series, source_unit: str, inplace: bool = False, always_return_copy: bool = False) -> pd.Series:
        result = self._convert_values_to_si(values, source_unit, inplace=inplace)
        return result.copy() if result is not None and result is values and always_return_copy else result

    def _convert_values_from_si(self, values: Union[np.array, pd.Series], target_unit: str, inplace: bool = False) -> Union[np.array, pd.Series]:
        if values is None:
            return None

        conversion_to_si = self.get_conversion_to_si(target_unit)
        factor = conversion_to_si.factor
        offset = conversion_to_si.offset

        result = values

        if inplace:
            if offset != 0:
                result -= offset

            if factor != 1:
                result /= factor
        else:
            if offset != 0:
                result = result - offset

            if factor != 1:
                result = result / factor

        return result

    def convert_array_from_si(self, values: np.array, target_unit: str, inplace: bool = False, always_return_copy: bool = False) -> np.array:
        result = self._convert_values_from_si(values, target_unit, inplace=inplace)
        return np.copy(result) if result is not None and result is values and always_return_copy else result

    def convert_series_from_si(self, values: pd.Series, target_unit: str, inplace: bool = False, always_return_copy: bool = False) -> pd.Series:
        result = self._convert_values_from_si(values, target_unit, inplace=inplace)
        return result.copy() if result is not None and result is values and always_return_copy else result

    def _convert_values_between_units(self, values: Union[np.array, pd.Series], source_unit: str, target_unit: str, inplace: bool = False) -> Union[np.array, pd.Series]:
        if values is None:
            return None

        conversion = self.get_conversion_between_units(source_unit, target_unit)

        result = values

        if not conversion.is_conversion_required:
            return result

        combined_offset = conversion.offset_to_si - conversion.offset_from_si

        if inplace:
            if conversion.factor_to_si != 1:
                result *= conversion.factor_to_si

            if combined_offset != 0:
                result += combined_offset

            if conversion.factor_from_si != 1:
                result /= conversion.factor_from_si
        else:
            if conversion.factor_to_si != 1:
                result = result * conversion.factor_to_si

            if combined_offset != 0:
                result = result + combined_offset

            if conversion.factor_from_si != 1:
                result = result / conversion.factor_from_si

        return result

    def convert_array_between_units(self, values: np.array, source_unit: str, target_unit: str, inplace: bool = False, always_return_copy: bool = False) -> np.array:
        result = self._convert_values_between_units(values, source_unit, target_unit, inplace=inplace)
        return np.copy(result) if result is not None and result is values and always_return_copy else result

    def convert_series_between_units(self, values: pd.Series, source_unit: str, target_unit: str, inplace: bool = False, always_return_copy: bool = False) -> pd.Series:
        result = self._convert_values_between_units(values, source_unit, target_unit, inplace=inplace)
        return result.copy() if result is not None and result is values and always_return_copy else result

    def get_conversion_between_units(self, source_unit: str, target_unit: str) -> ConversionBetweenUnits:
        conversion_from_source_to_si = self.get_conversion_to_si(source_unit)
        factor_to_si = conversion_from_source_to_si.factor
        offset_to_si = conversion_from_source_to_si.offset

        conversion_from_target_to_si = self.get_conversion_to_si(target_unit)
        factor_from_si = conversion_from_target_to_si.factor
        offset_from_si = conversion_from_target_to_si.offset

        conversion_required = True

        combined_offset = offset_to_si - offset_from_si
        if combined_offset == 0:
            combined_factor = factor_to_si / factor_from_si

            if combined_factor == 1:
                conversion_required = False

        return ConversionBetweenUnits(factor_to_si, offset_to_si, factor_from_si, offset_from_si, conversion_required)
