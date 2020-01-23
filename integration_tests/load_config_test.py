import aiounittest

import canopy
import integration_tests


class LoadConfigTest(aiounittest.AsyncTestCase):
    async def test_it_should_be_able_to_load_a_config_by_id(self):
        environment = await integration_tests.Environment.load()
        async with environment.create_session() as session:
            car = await canopy.load_config(session, environment.car.config.document_id)
            self.assertEqual(car.config.document_id, environment.car.config.document_id)
