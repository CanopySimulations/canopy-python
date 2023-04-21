from asyncio import get_event_loop
import pytest
import integration_tests


@pytest.fixture(scope="session")
def event_loop():
    loop = get_event_loop()
    yield loop

@pytest.fixture(scope='session')
async def environment() -> integration_tests.Environment:
    async with integration_tests.Environment() as e:
        yield e
