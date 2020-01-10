from __future__ import absolute_import

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


class TestUnits(unittest.TestCase):
    def setUp(self):
        self.units = canopy.Units()

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

    def test_convert_value_from_si(self):
        self.assertAlmostEqual(self.units.convert_value_from_si(temperatureK, 'C'), temperatureC, delta=0.01)
        self.assertAlmostEqual(self.units.convert_value_from_si(temperatureK, 'F'), temperatureF, delta=0.01)

        self.assertAlmostEqual(self.units.convert_value_from_si(temperatureK, 'C', True), temperatureK, delta=0.01)
        self.assertAlmostEqual(self.units.convert_value_from_si(temperatureK, 'F', True), temperatureK * 9 / 5, delta=0.01)

        self.assertEqual(self.units.convert_value_from_si(temperatureK, 'K'), temperatureK)

    def test_convert_values_from_si(self):
        data = np.array([temperatureK, temperatureK2])
        self.units.convert_values_from_si(data, 'F')
        self.assertEqual(len(data), 2)
        self.assertAlmostEqual(data[0], temperatureF, delta=0.01)
        self.assertAlmostEqual(data[1], temperatureF2, delta=0.01)

    def test_convert_column_from_si(self):
        data = pd.DataFrame({'temp': [temperatureK, temperatureK2]})
        self.units.convert_column_from_si(data, 'temp', 'F')
        self.assertEqual(len(data.temp), 2)
        self.assertAlmostEqual(data.temp[0], temperatureF, delta=0.01)
        self.assertAlmostEqual(data.temp[1], temperatureF2, delta=0.01)

    def test_convert_value_to_si(self):
        self.assertAlmostEqual(self.units.convert_value_to_si(temperatureC, 'C'), temperatureK, delta=0.01)
        self.assertAlmostEqual(self.units.convert_value_to_si(temperatureF, 'F'), temperatureK, delta=0.01)
        self.assertEqual(self.units.convert_value_to_si(3, 'e-3'), 0.003)
        self.assertEqual(self.units.convert_value_to_si(3, 'e-6'), 0.000003)

        self.assertAlmostEqual(self.units.convert_value_to_si(temperatureC, 'C', True), temperatureC, delta=0.01)
        self.assertAlmostEqual(self.units.convert_value_to_si(temperatureF, 'F', True), temperatureF * 5 / 9, delta=0.01)

        self.assertEqual(self.units.convert_value_to_si(temperatureK, 'K'), temperatureK)

    def test_convert_values_to_si(self):
        data = np.array([temperatureF, temperatureF2])
        self.units.convert_values_to_si(data, 'F')
        self.assertEqual(len(data), 2)
        self.assertAlmostEqual(data[0], temperatureK, delta=0.01)
        self.assertAlmostEqual(data[1], temperatureK2, delta=0.01)

    def test_convert_column_to_si(self):
        data = pd.DataFrame({'temp': [temperatureF, temperatureF2]})
        self.units.convert_column_to_si(data, 'temp', 'F')
        self.assertEqual(len(data.temp), 2)
        self.assertAlmostEqual(data.temp[0], temperatureK, delta=0.01)
        self.assertAlmostEqual(data.temp[1], temperatureK2, delta=0.01)

    def test_convert_value_between_units(self):
        self.assertAlmostEqual(self.units.convert_value_between_units(temperatureC, 'C', 'F'), temperatureF, delta=0.01)

    def test_convert_values_between_units(self):
        data = np.array([temperatureC, temperatureC2])
        self.units.convert_values_between_units(data, 'C', 'F')
        self.assertEqual(len(data), 2)
        self.assertAlmostEqual(data[0], temperatureF, delta=0.01)
        self.assertAlmostEqual(data[1], temperatureF2, delta=0.01)

        # It should convert between non-si units when only factor
        data = np.array([1000.0, 2000.0])
        self.units.convert_values_between_units(data, 'mm', 'km')
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0], 0.001)
        self.assertEqual(data[1], 0.002)

    def test_convert_column_between_units(self):
        data = pd.DataFrame({'temp': [temperatureC, temperatureC2]})
        self.units.convert_column_between_units(data, 'temp', 'C', 'F')
        self.assertEqual(len(data.temp), 2)
        self.assertAlmostEqual(data.temp[0], temperatureF, delta=0.01)
        self.assertAlmostEqual(data.temp[1], temperatureF2, delta=0.01)

        # It should convert between non-si units when only factor
        data = pd.DataFrame({'temp': [1000.0, 2000.0]})
        self.units.convert_column_between_units(data, 'temp', 'mm', 'km')
        self.assertEqual(len(data.temp), 2)
        self.assertEqual(data.temp[0], 0.001)
        self.assertEqual(data.temp[1], 0.002)

    def test_is_conversion_required(self):
        self.assertTrue(self.units.get_conversion_between_units('mm', 'km').is_conversion_required)
        self.assertTrue(self.units.get_conversion_between_units('m', 'km').is_conversion_required)
        self.assertTrue(self.units.get_conversion_between_units('km', 'm').is_conversion_required)
        self.assertTrue(self.units.get_conversion_between_units('C', 'F').is_conversion_required)
        self.assertFalse(self.units.get_conversion_between_units('F', 'F').is_conversion_required)
        self.assertFalse(self.units.get_conversion_between_units('m', 'm').is_conversion_required)
        self.assertFalse(self.units.get_conversion_between_units('mm', 'mm').is_conversion_required)
