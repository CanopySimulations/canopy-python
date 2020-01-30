import canopy
import unittest
import pandas as pd
import numpy as np


class ProcessDataFrameTest(unittest.TestCase):

    def test_it_should_do_nothing(self):
        data_frame = pd.DataFrame({
            'a': [1, 2, 3],
            'b': [4, 5, 6],
            'c': [7, 8, 9],
        })

        copy = data_frame.copy()
        canopy.process_data_frame(data_frame)
        self.assertTrue(data_frame.equals(copy))

    def test_it_should_set_index(self):
        data_frame = pd.DataFrame({
            'a': [1, 2, 3],
            'b': [4, 5, 6],
            'c': [7, 8, 9],
        })

        canopy.process_data_frame(data_frame, index_column_name='b')
        self.assertTrue(np.array_equal(np.array(data_frame.index), np.array([4, 5, 6])))

    def test_it_should_standardise_no_units_and_allow_empty_strings_for_units(self):
        data_frame = pd.DataFrame({
            'a': [1, 2, 3],
            'units': ['m/s', '()', np.nan],
        })

        canopy.process_data_frame(data_frame)

        self.assertTrue(
            data_frame.equals(
                pd.DataFrame({
                    'a': [1, 2, 3],
                    'units': ['m/s', '', ''],
                })))

    def test_it_should_allow_empty_strings(self):
        data_frame = pd.DataFrame({
            'a': ['1', np.nan, '3'],
            'b': ['4', np.nan, np.nan],
            'c': [np.nan, '8', '9'],
        })

        canopy.process_data_frame(data_frame, empty_string_valid_column_names=['a', 'b'])

        self.assertTrue(
            data_frame.equals(
                pd.DataFrame({
                    'a': ['1', '', '3'],
                    'b': ['4', '', ''],
                    'c': [np.nan, '8', '9'],
                })))
