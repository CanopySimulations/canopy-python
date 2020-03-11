import canopy
import unittest


class EnsureSimTypeStringTest(unittest.TestCase):

    def test_sim_type_string(self):
        self.assertEqual('apexSim', canopy.ensure_study_type_string('ApexSim'))

    def test_study_type_string(self):
        self.assertEqual('apexSim', canopy.ensure_study_type_string('apexSim'))

    def test_short_strings(self):
        self.assertEqual('', canopy.ensure_study_type_string(''))
        self.assertEqual('a', canopy.ensure_study_type_string('A'))
        self.assertEqual('a', canopy.ensure_study_type_string('a'))
        self.assertEqual('ap', canopy.ensure_study_type_string('Ap'))
        self.assertEqual('ap', canopy.ensure_study_type_string('ap'))
