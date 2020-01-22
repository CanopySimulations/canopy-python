import unittest
import canopy


class SimVersionToNumberTest(unittest.TestCase):

    def test_it_should_convert_to_number(self):
        self.assertEqual(canopy.sim_version_to_number('1.1234'), 1234)

    def test_it_can_be_used_to_compare_sim_versions(self):
        self.assertTrue(canopy.sim_version_to_number('1.1') == canopy.sim_version_to_number('1.1'))
        self.assertTrue(canopy.sim_version_to_number('1.1') < canopy.sim_version_to_number('1.2'))
        self.assertTrue(canopy.sim_version_to_number('1.2') < canopy.sim_version_to_number('1.10'))
        self.assertTrue(canopy.sim_version_to_number('1.10') < canopy.sim_version_to_number('1.100'))
        self.assertTrue(canopy.sim_version_to_number('1.20') < canopy.sim_version_to_number('1.1020'))

