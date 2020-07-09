from typing import Optional

import os
import canopy
import integration_tests
import uuid
import logging

logger = logging.getLogger(__name__)

_python_data_version = '1'


class EnvironmentLoader:
    _data: Optional[integration_tests.EnvironmentData] = None

    @staticmethod
    async def load() -> integration_tests.EnvironmentData:
        if EnvironmentLoader._data is None:
            credentials_key = 'CANOPY_PYTHON_INTEGRATION_TEST_CREDENTIALS'
            credentials = os.environ.get(credentials_key)

            if credentials is None:
                raise RuntimeError(f'Test credentials not found. Please create an environment variable "{credentials_key}"="client_id|client_secret|user_name|tenant_name|password"')

            client_id, client_secret, username, tenant_name, password = credentials.split('|')

            if client_id is None:
                raise RuntimeError('Client ID not found.')
            if client_secret is None:
                raise RuntimeError('Client Secret not found.')
            if username is None:
                raise RuntimeError('Username not found.')
            if tenant_name is None:
                raise RuntimeError('Tenant Name not found.')
            if password is None:
                raise RuntimeError('Password not found.')

            authentication_data = canopy.AuthenticationData(
                client_id=client_id,
                client_secret=client_secret,
                username=username,
                tenant_name=tenant_name,
                password=password)

            if username == 'master' and tenant_name == 'test':
                authentication_data = await EnvironmentLoader.create_test_user(authentication_data)

            EnvironmentLoader._data = integration_tests.EnvironmentData(
                authentication_data)

        return EnvironmentLoader._data

    @staticmethod
    async def create_test_user(master: canopy.AuthenticationData) -> canopy.AuthenticationData:
        username = 'u-' + str(uuid.uuid4()).replace('-', '')[0:18]
        password = str(uuid.uuid4())
        async with canopy.Session(authentication_data=master) as session:
            session.authentication.authenticate()

            api = canopy.openapi.MembershipApi(session.async_client)
            await api.membership_post_registration(
                registration_data=canopy.openapi.RegistrationData(
                    session.authentication.tenant_id,
                    username + '@testing.canopysimulations.com',
                    username,
                    password))

            logger.info('Created test user: {}'.format(username))

            return canopy.AuthenticationData(
                master.client_id,
                master.client_secret,
                username,
                master.tenant_name,
                password)
