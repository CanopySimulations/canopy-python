import asyncio
import pytest
import integration_tests


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the session."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope='session')
async def environment() -> integration_tests.Environment:
    async with integration_tests.Environment() as e:
        yield e
