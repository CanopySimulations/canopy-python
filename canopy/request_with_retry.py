import asyncio
from typing import TypeVar, Callable, Awaitable
import logging
from aiohttp.client_exceptions import ClientResponseError, ClientConnectionError, ServerTimeoutError, \
    ServerConnectionError

logger = logging.getLogger(__name__)

TResult = TypeVar('TResult')      # Declare type variable


async def request_with_retry(call: Callable[[], Awaitable[TResult]], error_subject: str, throw_error: bool) -> TResult:
    try:
        try:
            return await call()
        except (asyncio.TimeoutError, ClientConnectionError, ServerConnectionError):
            # We'll retry once.
            logger.warning(f'Retrying {error_subject}')
            return await call()
    except (asyncio.TimeoutError, ServerTimeoutError):
        logger.warning(f'Timed out loading {error_subject}')
        if throw_error:
            raise
    except ClientConnectionError:
        logger.warning(f'Connection error loading {error_subject}')
        if throw_error:
            raise
    except ClientResponseError as e:
        logger.warning(f'Response error loading {error_subject} ({e.message})')
        if throw_error:
            raise

    return None
