import unittest
import asyncio

import canopy


class RequestWithRetryTest(unittest.TestCase):

    def test_it_should_return_result_if_no_error(self):
        request = DummyRequest(0)
        result = canopy.run(canopy.request_with_retry(lambda: request.execute('abc'), 'request', True))
        self.assertEqual(result, 'abc')

    def test_it_should_return_result_if_one_error(self):
        request = DummyRequest(1)
        result = canopy.run(canopy.request_with_retry(lambda: request.execute('abc'), 'request', True))
        self.assertEqual(result, 'abc')

    def test_it_should_raise_error_if_two_errors(self):
        request = DummyRequest(2)
        try:
            canopy.run(canopy.request_with_retry(lambda: request.execute('abc'), 'request', True))
            self.fail()
        except asyncio.TimeoutError:
            pass

    def test_it_should_return_none_if_two_errors_and_suppressed(self):
        request = DummyRequest(2)
        result = canopy.run(canopy.request_with_retry(lambda: request.execute('abc'), 'request', False))
        self.assertIsNone(result)


class DummyRequest:

    def __init__(self, error_count: int):
        self.error_count = error_count

    async def execute(self, result: str) -> str:
        self.error_count -= 1
        await asyncio.sleep(0.1)
        if self.error_count >= 0:
            raise asyncio.TimeoutError('Timed out')
        else:
            return result
