import pytest
import integration_tests


@pytest.fixture(scope='session')
async def environment() -> integration_tests.Environment:
    async with integration_tests.Environment() as e:
        yield e
