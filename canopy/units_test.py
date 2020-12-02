import unittest
import canopy
import pandas as pd
import numpy as np

temperatureK = 373.15
temperatureC = 100.0
temperatureF = 212.0
temperatureK2 = 473.15
temperatureC2 = 200.0
temperatureF2 = 392.0


class UnitsTest(unittest.TestCase):
    def setUp(self):
        self.units = canopy.Units()

    # Specific units.
    def test_specific_units(self):
        self.assertAlmostEqual(
            self.units.convert_value_between_units(1, 'inHg', 'Pa'),
            3386.39, delta=0.01);
        self.assertAlmostEqual(
            self.units.convert_value_between_units(1000, 'Pa', 'inHg'),
            0.2953, delta=0.0001);

    def test_try_get_conversion_to_si(self):
        existing = self.units.try_get_conversion_to_si('F')
        self.assertEqual(existing.factor, 5/9)
        self.assertEqual(existing.offset, 459.67 * 5 / 9)

        missing = self.units.try_get_conversion_to_si('blah')
        self.assertEqual(missing, None)

    def test_get_conversion_to_si(self):
        existing = self.units.get_conversion_to_si('F')
        self.assertEqual(existing.factor, 5/9)
        self.assertEqual(existing.offset, 459.67 * 5 / 9)

        with self.assertRaises(KeyError):
            self.units.get_conversion_to_si('blah')

    def test_get_conversion_to_si_or_default(self):
        existing = self.units.get_conversion_to_si_or_default('F')
        self.assertEqual(existing.factor, 5/9)
        self.assertEqual(existing.offset, 459.67 * 5 / 9)

        missing = self.units.get_conversion_to_si_or_default('blah')
        self.assertEqual(missing.factor, 1)
        self.assertEqual(missing.offset, 0)

    # FROM SI
    def test_convert_value_from_si(self):
        self.assertAlmostEqual(self.units.convert_value_from_si(temperatureK, 'C'), temperatureC, delta=0.01)
        self.assertAlmostEqual(self.units.convert_value_from_si(temperatureK, 'F'), temperatureF, delta=0.01)

        self.assertAlmostEqual(self.units.convert_value_from_si(temperatureK, 'C', True), temperatureK, delta=0.01)
        self.assertAlmostEqual(self.units.convert_value_from_si(temperatureK, 'F', True), temperatureK * 9 / 5, delta=0.01)

        self.assertEqual(self.units.convert_value_from_si(temperatureK, 'K'), temperatureK)

    def test_convert_array_from_si(self):
        data = np.array([temperatureK, temperatureK2])
        data_copy = np.copy(data)
        result = self.units.convert_array_from_si(data, 'F')
        self.assertIsNot(result, data)
        self.assertFalse(np.array_equal(result, data))
        self.assertTrue(np.array_equal(data, data_copy))
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0], temperatureF, delta=0.01)
        self.assertAlmostEqual(result[1], temperatureF2, delta=0.01)

    def test_convert_array_from_si_no_conversion_required(self):
        data = np.array([temperatureK, temperatureK2])
        result = self.units.convert_array_from_si(data, 'K')
        self.assertIs(result, data)

    def test_convert_array_from_si_always_return_copy(self):
        data = np.array([temperatureK, temperatureK2])
        result = self.units.convert_array_from_si(data, 'K', always_return_copy=True)
        self.assertIsNot(result, data)
        self.assertTrue(np.array_equal(result, data))

    def test_convert_array_from_si_inplace(self):
        data = np.array([temperatureK, temperatureK2])
        result = self.units.convert_array_from_si(data, 'F', inplace=True)
        self.assertIs(result, data)
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0], temperatureF, delta=0.01)
        self.assertAlmostEqual(result[1], temperatureF2, delta=0.01)

    def test_convert_series_from_si(self):
        data = pd.Series([temperatureK, temperatureK2])
        data_copy = data.copy()
        result = self.units.convert_series_from_si(data, 'F')
        self.assertIsNot(result, data)
        self.assertFalse(result.equals(data))
        self.assertTrue(data.equals(data_copy))
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0], temperatureF, delta=0.01)
        self.assertAlmostEqual(result[1], temperatureF2, delta=0.01)

    def test_convert_series_from_si_no_conversion_required(self):
        data = pd.Series([temperatureK, temperatureK2])
        result = self.units.convert_series_from_si(data, 'K')
        self.assertIs(result, data)

    def test_convert_series_from_si_always_return_copy(self):
        data = pd.Series([temperatureK, temperatureK2])
        result = self.units.convert_series_from_si(data, 'K', always_return_copy=True)
        self.assertIsNot(result, data)
        self.assertTrue(result.equals(data))

    def test_convert_series_from_si_inplace(self):
        data = pd.Series([temperatureK, temperatureK2])
        result = self.units.convert_series_from_si(data, 'F', inplace=True)
        self.assertIs(result, data)
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0], temperatureF, delta=0.01)
        self.assertAlmostEqual(result[1], temperatureF2, delta=0.01)

    # TO SI
    def test_convert_value_to_si(self):
        self.assertAlmostEqual(self.units.convert_value_to_si(temperatureC, 'C'), temperatureK, delta=0.01)
        self.assertAlmostEqual(self.units.convert_value_to_si(temperatureF, 'F'), temperatureK, delta=0.01)
        self.assertEqual(self.units.convert_value_to_si(3, 'e-3'), 0.003)
        self.assertEqual(self.units.convert_value_to_si(3, 'e-6'), 0.000003)

        self.assertAlmostEqual(self.units.convert_value_to_si(temperatureC, 'C', True), temperatureC, delta=0.01)
        self.assertAlmostEqual(self.units.convert_value_to_si(temperatureF, 'F', True), temperatureF * 5 / 9, delta=0.01)

        self.assertEqual(self.units.convert_value_to_si(temperatureK, 'K'), temperatureK)

    def test_convert_array_to_si(self):
        data = np.array([temperatureF, temperatureF2])
        data_copy = np.copy(data)
        result = self.units.convert_array_to_si(data, 'F')
        self.assertIsNot(result, data)
        self.assertFalse(np.array_equal(result, data))
        self.assertTrue(np.array_equal(data, data_copy))
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0], temperatureK, delta=0.01)
        self.assertAlmostEqual(result[1], temperatureK2, delta=0.01)

    def test_convert_array_to_si_no_conversion_required(self):
        data = np.array([temperatureK, temperatureK2])
        result = self.units.convert_array_to_si(data, 'K')
        self.assertIs(result, data)

    def test_convert_array_to_si_always_return_copy(self):
        data = np.array([temperatureK, temperatureK2])
        result = self.units.convert_array_to_si(data, 'K', always_return_copy=True)
        self.assertIsNot(result, data)
        self.assertTrue(np.array_equal(result, data))

    def test_convert_array_to_si_inplace(self):
        data = np.array([temperatureF, temperatureF2])
        result = self.units.convert_array_to_si(data, 'F', inplace=True)
        self.assertIs(result, data)
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0], temperatureK, delta=0.01)
        self.assertAlmostEqual(result[1], temperatureK2, delta=0.01)

    def test_convert_series_to_si(self):
        data = pd.Series([temperatureF, temperatureF2])
        data_copy = data.copy()
        result = self.units.convert_series_to_si(data, 'F')
        self.assertIsNot(result, data)
        self.assertFalse(result.equals(data))
        self.assertTrue(data.equals(data_copy))
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0], temperatureK, delta=0.01)
        self.assertAlmostEqual(result[1], temperatureK2, delta=0.01)

    def test_convert_series_to_si_no_conversion_required(self):
        data = pd.Series([temperatureK, temperatureK2])
        result = self.units.convert_series_to_si(data, 'K')
        self.assertIs(result, data)

    def test_convert_series_to_si_always_return_copy(self):
        data = pd.Series([temperatureK, temperatureK2])
        result = self.units.convert_series_to_si(data, 'K', always_return_copy=True)
        self.assertIsNot(result, data)
        self.assertTrue(result.equals(data))

    def test_convert_series_to_si_inplace(self):
        data = pd.Series([temperatureF, temperatureF2])
        result = self.units.convert_series_to_si(data, 'F', inplace=True)
        self.assertIs(result, data)
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0], temperatureK, delta=0.01)
        self.assertAlmostEqual(result[1], temperatureK2, delta=0.01)

    # BETWEEN UNITS
    def test_convert_value_between_units(self):
        self.assertAlmostEqual(self.units.convert_value_between_units(temperatureC, 'C', 'F'), temperatureF, delta=0.01)

    def test_convert_array_between_units(self):
        data = np.array([temperatureC, temperatureC2])
        data_copy = np.copy(data)
        result = self.units.convert_array_between_units(data, 'C', 'F')
        self.assertIsNot(result, data)
        self.assertFalse(np.array_equal(result, data))
        self.assertTrue(np.array_equal(data, data_copy))
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0], temperatureF, delta=0.01)
        self.assertAlmostEqual(result[1], temperatureF2, delta=0.01)

        # It should convert between non-si units when only factor
        data = np.array([1000.0, 2000.0])
        result = self.units.convert_array_between_units(data, 'mm', 'km')
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 0.001)
        self.assertEqual(result[1], 0.002)

    def test_convert_array_between_units_no_conversion_required(self):
        data = np.array([temperatureC, temperatureC2])
        result = self.units.convert_array_between_units(data, 'C', 'C')
        self.assertIs(result, data)

    def test_convert_array_between_units_always_return_copy(self):
        data = np.array([temperatureC, temperatureC2])
        result = self.units.convert_array_between_units(data, 'C', 'C', always_return_copy=True)
        self.assertIsNot(result, data)
        self.assertTrue(np.array_equal(result, data))

    def test_convert_array_between_units_inplace(self):
        data = np.array([temperatureC, temperatureC2])
        result = self.units.convert_array_between_units(data, 'C', 'F', inplace=True)
        self.assertIs(result, data)
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0], temperatureF, delta=0.01)
        self.assertAlmostEqual(result[1], temperatureF2, delta=0.01)

    def test_convert_series_between_units(self):
        data = pd.Series([temperatureC, temperatureC2])
        data_copy = data.copy()
        result = self.units.convert_series_between_units(data, 'C', 'F')
        self.assertIsNot(result, data)
        self.assertFalse(result.equals(data))
        self.assertTrue(data.equals(data_copy))
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0], temperatureF, delta=0.01)
        self.assertAlmostEqual(result[1], temperatureF2, delta=0.01)

        # It should convert between non-si units when only factor
        data = pd.Series([1000.0, 2000.0])
        result = self.units.convert_series_between_units(data, 'mm', 'km')
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 0.001)
        self.assertEqual(result[1], 0.002)

    def test_convert_series_between_units_no_conversion_required(self):
        data = pd.Series([temperatureC, temperatureC2])
        result = self.units.convert_series_between_units(data, 'C', 'C')
        self.assertIs(result, data)

    def test_convert_series_between_units_always_return_copy(self):
        data = pd.Series([temperatureC, temperatureC2])
        result = self.units.convert_series_between_units(data, 'C', 'C', always_return_copy=True)
        self.assertIsNot(result, data)
        self.assertTrue(result.equals(data))

    def test_convert_series_between_units_inplace(self):
        data = pd.Series([temperatureC, temperatureC2])
        result = self.units.convert_series_between_units(data, 'C', 'F', inplace=True)
        self.assertIs(result, data)
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0], temperatureF, delta=0.01)
        self.assertAlmostEqual(result[1], temperatureF2, delta=0.01)

    def test_is_conversion_required(self):
        self.assertTrue(self.units.get_conversion_between_units('mm', 'km').is_conversion_required)
        self.assertTrue(self.units.get_conversion_between_units('m', 'km').is_conversion_required)
        self.assertTrue(self.units.get_conversion_between_units('km', 'm').is_conversion_required)
        self.assertTrue(self.units.get_conversion_between_units('C', 'F').is_conversion_required)
        self.assertFalse(self.units.get_conversion_between_units('F', 'F').is_conversion_required)
        self.assertFalse(self.units.get_conversion_between_units('m', 'm').is_conversion_required)
        self.assertFalse(self.units.get_conversion_between_units('mm', 'mm').is_conversion_required)
