import unittest
import canopy
from munch import Munch


class DictToObjectTest(unittest.TestCase):

    def test_it_should_perform_deep_conversion(self):
        data = {
            'a': 1,
            'b': {
                'c': 2
            },
            'd': 3
        }

        output = canopy.dict_to_object(data)

        self.assertTrue(isinstance(output.b, Munch))
        self.assertEqual(output.b.c, 2)

    def test_it_should_not_perform_conversion_twice(self):
        data = {
            'a': 1,
            'b': {
                'c': 2
            },
            'd': 3
        }

        output = canopy.dict_to_object(data)
        output2 = canopy.dict_to_object(output)

        self.assertIs(output, output2)
        self.assertIs(output.b, output2.b)

