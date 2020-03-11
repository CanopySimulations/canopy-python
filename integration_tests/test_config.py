from asyncio import Future
from typing import List, Optional

import asyncio
import pytest
import numpy as np

import canopy
import integration_tests

default_car_name = 'Canopy F1 Car 2019'
test_car_name = 'Python Automated Test Car'
test_car_name_2 = 'Python Automated Test Car 2'
test_car_property_key = 'python-automated-test'
test_car_property_value = 'true'
test_car_custom_properties = {
    test_car_property_key: test_car_property_value,
}


class State(object):
    configs_to_remove: List[str] = []
    default_car: Optional[canopy.LocalConfig] = None
    test_car_config_id: Optional[str] = None
    test_car_config_id_2: Optional[str] = None


@pytest.mark.asyncio
class TestConfig:

    @pytest.fixture(autouse=True, scope='class')
    def state(self) -> State:
        return State()

    async def test_0100_it_should_load_a_default_config(self, state: State):
        async with integration_tests.Environment() as environment:
            state.default_car = await canopy.load_default_config(
                environment.session,
                'car',
                default_car_name)

            assert state.default_car is not None
            assert default_car_name == state.default_car.name

    async def test_0200_it_should_create_a_config(self, state: State):

        async with integration_tests.Environment() as environment:
            state.test_car_config_id = await canopy.create_config(
                environment.session,
                'car',
                test_car_name,
                state.default_car.raw_data,
                test_car_custom_properties)

            assert state.test_car_config_id is not None

            state.configs_to_remove.append(state.test_car_config_id)

    async def test_0210_it_should_create_a_config_with_no_custom_properties(self, state: State):

        async with integration_tests.Environment() as environment:
            state.test_car_config_id_2 = await canopy.create_config(
                environment.session,
                'car',
                test_car_name_2,
                state.default_car.raw_data)

            assert state.test_car_config_id_2 is not None

            state.configs_to_remove.append(state.test_car_config_id_2)

    async def test_0220_it_should_create_a_config_containing_numpy_arrays(self, state: State):
        async with integration_tests.Environment() as environment:
            state.default_car.data.chassis.rUndertrayFront = np.array(state.default_car.data.chassis.rUndertrayFront)

            state.test_car_config_id = await canopy.create_config(
                environment.session,
                'car',
                test_car_name,
                state.default_car.raw_data,
                test_car_custom_properties)

            assert state.test_car_config_id is not None

            state.configs_to_remove.append(state.test_car_config_id)

    async def test_0300_it_should_find_a_config_by_name(self, state: State):
        async with integration_tests.Environment() as environment:
            car = await canopy.find_config(
                environment.session,
                'car',
                owner_username=environment.data.authentication.username,
                name=test_car_name)

            assert car.document.document_id == state.test_car_config_id

    async def test_0400_it_should_find_a_config_by_custom_properties(self, state: State):
        async with integration_tests.Environment() as environment:
            car = await canopy.find_config(
                environment.session,
                'car',
                owner_username=environment.data.authentication.username,
                custom_properties=test_car_custom_properties)

            assert car.document.document_id == state.test_car_config_id

    async def test_0500_it_should_find_a_config_by_multiple_criteria(self, state: State):
        async with integration_tests.Environment() as environment:
            car = await canopy.find_config(
                environment.session,
                'car',
                owner_username=environment.data.authentication.username,
                name=test_car_name,
                custom_properties=test_car_custom_properties)

            assert car.document.document_id == state.test_car_config_id

    async def test_0600_it_should_load_a_config_by_id(self, state: State):
        async with integration_tests.Environment() as environment:
            car = await canopy.load_config(
                environment.session,
                state.test_car_config_id)

            assert car.document.document_id == state.test_car_config_id

    async def test_0700_it_should_convert_configs_to_local_configs(self, state: State):
        async with integration_tests.Environment() as environment:
            car = await canopy.load_config(
                environment.session,
                state.test_car_config_id)
            local_car = car.to_local_config()

            assert car.document.document_id == state.test_car_config_id
            assert local_car.config_id == state.test_car_config_id

    async def test_0700_it_should_convert_configs_to_local_configs_with_no_custom_properties(self, state: State):
        async with integration_tests.Environment() as environment:
            car = await canopy.load_config(
                environment.session,
                state.test_car_config_id_2)
            local_car = car.to_local_config()

            assert car.document.document_id == state.test_car_config_id_2
            assert local_car.config_id == state.test_car_config_id_2

    async def test_9000_it_should_remove_configs(self, state: State):
        async with integration_tests.Environment() as environment:
            tasks: List[Future] = []
            for config_id in state.configs_to_remove:
                tasks.append(asyncio.ensure_future(canopy.delete_config(
                    environment.session,
                    config_id)))
            await asyncio.gather(*tasks)
