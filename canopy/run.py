from typing import Coroutine
import asyncio


def run(coroutine: Coroutine):
    return asyncio.get_event_loop().run_until_complete(coroutine)
