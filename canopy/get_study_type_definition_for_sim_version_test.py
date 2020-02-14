import unittest
import canopy


class GetStudyTypeDefinitionForSimVersionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.study_type_definition = canopy.openapi.StudyTypeDefinition(
            'dynamicLap',
            'Dynamic Lap',
            ['DynamicLap'],
            ['car', 'track', 'weather'],
            previous_definitions=[
                canopy.openapi.IPreviousDefinitionStudyTypeDefinition(
                    sim_version='1.50',
                    definition=canopy.openapi.StudyTypeDefinition(
                        'dynamicLap',
                        'Dynamic Lap 50',
                        ['DynamicLap'],
                        ['car', 'track'])),
                canopy.openapi.IPreviousDefinitionStudyTypeDefinition(
                    sim_version='1.100',
                    definition=canopy.openapi.StudyTypeDefinition(
                        'dynamicLap',
                        'Dynamic Lap 100',
                        ['DynamicLap'],
                        ['car', 'track'])),
            ])

    def test_it_should_return_root_definition_when_no_sim_version(self):
        self.assertEqual(
            canopy.get_study_type_definition_for_sim_version(self.study_type_definition),
            self.study_type_definition)

    def test_it_should_return_old_version_when_required(self):
        self.assertEqual(
            canopy.get_study_type_definition_for_sim_version(self.study_type_definition, '1.84'),
            self.study_type_definition.previous_definitions[1].definition)
        self.assertEqual(
            canopy.get_study_type_definition_for_sim_version(self.study_type_definition, '1.50'),
            self.study_type_definition.previous_definitions[0].definition)

    def test_it_should_return_latest_version_when_required(self):
        self.assertEqual(
            canopy.get_study_type_definition_for_sim_version(self.study_type_definition, '1.123'),
            self.study_type_definition)
