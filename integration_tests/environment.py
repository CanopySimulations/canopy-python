from typing import Optional

import os
import canopy
import integration_tests
import getpass


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
                # Find a study and a car for testing.
                try:
                    car = await canopy.find_config(
                        session,
                        'car',
                        custom_properties={
                            'python-automated-test': 'true'
                        })
                except canopy.NotFoundError:
                    raise RuntimeError('Test car not found. Please create a car with the custom property "python-automated-test" set to "true".')

                try:
                    study = await canopy.find_study(
                        session,
                        custom_properties={
                            'car.python-automated-test': 'true'
                        })
                except canopy.NotFoundError:
                    raise RuntimeError('Test study not found. Please create an ApexSim study using the test car.')

            Environment._data = integration_tests.EnvironmentData(
                authentication_data,
                car,
                study)

        return Environment._data
