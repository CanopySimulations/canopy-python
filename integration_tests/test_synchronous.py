import canopy
import asyncio
import integration_tests

default_car_name = 'Canopy F1 Car 2019'


class TestSynchronous:

    def test_synchronous_call(self):
        asyncio.set_event_loop(asyncio.new_event_loop())
        with integration_tests.Environment() as environment:
            default_car = canopy.run(canopy.load_default_config(
                environment.session,
                'car',
                default_car_name))

            assert default_car is not None
            assert default_car_name == default_car.name
