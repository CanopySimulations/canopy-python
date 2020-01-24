from asyncio import Future
from typing import List, Optional

import asyncio
import pytest
import logging

import canopy
import integration_tests

logger = logging.getLogger(__name__)

default_car_name = 'Canopy F1 Car 2019'
default_weather_name = '25 deg, dry'
test_car_name = 'Python Automated Test Car'
test_weather_name = 'Python Automated Test Weather'
test_study_name = 'Python Automated Test Study'
test_study_name_2 = 'Python Automated Test Study 2'
test_study_property_key = 'python-automated-test'
test_study_property_value = 'true'
test_custom_properties = {
    test_study_property_key: test_study_property_value,
}
test_passed_though_custom_properties = {
    'weather.' + test_study_property_key: test_study_property_value,
    'car.' + test_study_property_key: test_study_property_value,
}

class State(object):
    configs_to_remove: List[str] = []
    studies_to_remove: List[str] = []
    default_car: Optional[canopy.LocalConfig] = None
    default_weather: Optional[canopy.LocalConfig] = None
    study_id: Optional[str] = None
    study_id_2: Optional[str] = None


@pytest.mark.asyncio
class TestStudy:

    @pytest.fixture(autouse=True, scope='class')
    def state(self) -> State:
        return State()

    async def wait_for_and_verify_study(
            self,
            state: State,
            environment: integration_tests.Environment,
            study_id: str,
            expected_name: str) -> canopy.StudyDataResult:
        assert study_id is not None
        state.studies_to_remove.append(study_id)

        wait_result = await canopy.wait_for_study(
            environment.session,
            study_id,
            timeout_seconds=60)

        assert expected_name == wait_result.document.name
        assert wait_result.study_document.job_count > 0
        assert wait_result.study_document.job_count == wait_result.study_document.completed_job_count
        return wait_result

    async def test_0100_it_should_create_a_study_from_local_configs(self, state: State):
        async with integration_tests.Environment() as environment:
            state.default_car = await canopy.load_default_config(
                environment.session,
                'car',
                default_car_name)
            state.default_weather = await canopy.load_default_config(
                environment.session,
                'weather',
                default_weather_name)

            state.study_id = await canopy.create_study(
                environment.session,
                'apexSim',
                test_study_name,
                [
                    state.default_car,
                    state.default_weather,
                ],
                test_custom_properties)
            logger.info('Study ID is {}'.format(state.study_id))

            study = await self.wait_for_and_verify_study(state, environment, state.study_id, test_study_name)

            properties = canopy.ensure_dict(study.document.properties)
            assert test_study_property_value == properties[test_study_property_key]

    async def test_0200_it_should_create_a_study_from_references_and_loaded_configs(self, state: State):
        async with integration_tests.Environment() as environment:
            car_config_id = await canopy.create_config(
                environment.session,
                'car',
                test_car_name,
                state.default_car.data,
                test_custom_properties)
            weather_config_id = await canopy.create_config(
                environment.session,
                'weather',
                test_weather_name,
                state.default_weather.data,
                test_custom_properties)

            weather_config = await canopy.load_config(
                environment.session, weather_config_id)

            state.study_id_2 = await canopy.create_study(
                environment.session,
                'apexSim',
                test_study_name_2,
                [
                    car_config_id,
                    weather_config,
                ])
            logger.info('Study ID 2 is {}'.format(state.study_id_2))

            study = await self.wait_for_and_verify_study(state, environment, state.study_id_2, test_study_name_2)

            properties = canopy.ensure_dict(study.document.properties)
            assert test_study_property_value == properties['car.' + test_study_property_key]
            assert test_study_property_value == properties['weather.' + test_study_property_key]

    async def test_0300_it_should_find_a_study_by_name(self, state: State):
        async with integration_tests.Environment() as environment:
            study = await canopy.find_study(
                environment.session,
                owner_username=environment.data.authentication.username,
                name=test_study_name)

            assert study.document.document_id == state.study_id

    async def test_0400_it_should_find_a_study_by_custom_properties(self, state: State):
        async with integration_tests.Environment() as environment:
            study = await canopy.find_study(
                environment.session,
                owner_username=environment.data.authentication.username,
                custom_properties=test_passed_though_custom_properties)

            assert study.document.document_id == state.study_id_2
            assert 0 == len(study.jobs)

    async def test_0500_it_should_find_a_study_by_multiple_criteria(self, state: State):
        async with integration_tests.Environment() as environment:
            study = await canopy.find_study(
                environment.session,
                owner_username=environment.data.authentication.username,
                name=test_study_name_2,
                custom_properties=test_passed_though_custom_properties)

            assert study.document.document_id == state.study_id_2
            assert 0 == len(study.jobs)

    async def test_0600_it_should_load_a_study_by_id(self, state: State):
        async with integration_tests.Environment() as environment:
            study = await canopy.load_study(
                environment.session,
                state.study_id)

            assert study.document.document_id == state.study_id
            assert 1 == len(study.jobs)

            job = study.jobs[0]
            assert job.document is not None
            assert job.inputs is None
            assert 0 == len(job.scalar_data)
            assert 0 == len(job.vector_data.columns)
            assert 0 == len(job.vector_data)

    async def test_0700_it_should_load_a_study_by_id_with_data(self, state: State):
        async with integration_tests.Environment() as environment:
            study = await canopy.load_study(
                environment.session,
                state.study_id,
                sim_type='ApexSim',
                channel_names=[
                    'vCar',
                    'tLap', # This channel won't exist.
                    'hRideF',
                ],
                include_inputs=True,
                include_scalar_results=True)

            assert study.document.document_id == state.study_id
            assert 1 == len(study.jobs)

            job = study.jobs[0]
            assert job.document is not None
            assert job.inputs is not None
            assert len(job.scalar_data) > 0
            assert len(job.vector_data.columns) == 2
            assert len(job.vector_data) > 10

    async def test_9000_it_should_remove_configs(self, state: State):
        async with integration_tests.Environment() as environment:
            tasks: List[Future] = []
            for config_id in state.configs_to_remove:
                tasks.append(asyncio.ensure_future(canopy.delete_config(
                    environment.session,
                    config_id)))
            await asyncio.gather(*tasks)

    async def test_9100_it_should_remove_studies(self, state: State):
        async with integration_tests.Environment() as environment:
            tasks: List[Future] = []
            for study_id in state.studies_to_remove:
                tasks.append(asyncio.ensure_future(canopy.delete_study(
                    environment.session,
                    study_id)))
            await asyncio.gather(*tasks)
