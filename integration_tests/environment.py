from typing import Optional

import os
import canopy
import integration_tests
import logging

logger = logging.getLogger(__name__)

_python_data_version = '1'


class Environment:
    _data: Optional[integration_tests.EnvironmentData] = None

    @staticmethod
    async def load() -> integration_tests.EnvironmentData:
        if Environment._data is None:
            credentials = os.environ.get('CANOPY_TEST_CREDENTIALS')

            if credentials is None:
                raise RuntimeError('Test credentials not found. Please create an environment variable "CANOPY_TEST_CREDENTIALS"="client_id|client_secret|user_name|tenant_name|password"')

            client_id, client_secret, user_name, tenant_name, password = credentials.split('|')

            if client_id is None:
                raise RuntimeError('Client ID not found.')
            if client_secret is None:
                raise RuntimeError('Client Secret not found.')
            if user_name is None:
                raise RuntimeError('Username not found.')
            if tenant_name is None:
                raise RuntimeError('Tenant Name not found.')
            if password is None:
                raise RuntimeError('Password not found.')

            authentication_data = canopy.AuthenticationData(
                client_id=client_id,
                client_secret=client_secret,
                username=user_name,
                tenant_name=tenant_name,
                password=password)

            async with canopy.Session(authentication_data) as session:
                car = await Environment._load_test_car(session)
                study = await Environment._load_test_study(session, car)

            Environment._data = integration_tests.EnvironmentData(
                authentication_data,
                car,
                study)

        return Environment._data

    @staticmethod
    async def _load_test_car(session: canopy.Session) -> canopy.ConfigResult:
        custom_properties = {
            'python-automated-test': 'true',
            'python-data-version': _python_data_version
        }
        try:
            car = await canopy.find_config(session, 'car', custom_properties=custom_properties)
            logger.info('Found test car.')
        except canopy.NotFoundError:
            logger.info('Creating test car.')
            try:
                default_car = await canopy.load_default_config(session, 'car', 'Canopy F1 Car 2019')
                await canopy.create_config(session, 'car', 'Python Automated Test Car', default_car.data, custom_properties)
                car = await canopy.find_config(session, 'car', custom_properties=custom_properties)
            except Exception as e:
                raise RuntimeError('Failed to create test car.', ) from e

        return car

    @staticmethod
    async def _load_test_study(session: canopy.Session, car: canopy.ConfigResult) -> canopy.swagger.CanopyDocument:
        custom_properties = {
            'python-automated-test': 'true',
            'python-data-version': _python_data_version
        }
        try:
            study = await canopy.find_study(session, custom_properties=custom_properties)
            logger.info('Found test study.')
        except canopy.NotFoundError:
            logger.info('Creating test study.')
            try:
                default_weather = await canopy.load_default_config(session, 'weather', '25 deg, dry')
                study_id = await canopy.create_study(
                    session,
                    'apexSim',
                    'Python Automated Test Study',
                    [
                        car,
                        default_weather,
                    ],
                    custom_properties)
                wait_result = await canopy.wait_for_study(session, study_id, timeout_seconds=60)
                study = wait_result.study
            except Exception as e:
                raise RuntimeError('Failed to create test study.') from e

        return study
