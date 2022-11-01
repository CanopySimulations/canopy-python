from typing import Coroutine
import asyncio


def run(coroutine: Coroutine):
    return asyncio.run(coroutine)
