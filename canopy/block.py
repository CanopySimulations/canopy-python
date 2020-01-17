from typing import Coroutine
import asyncio


def block(coroutine: Coroutine):
    return asyncio.get_event_loop().run_until_complete(coroutine)
