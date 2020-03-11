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
default_exploration_name = 'Automated Test Monte Carlo'
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
exploration_notes = 'Exploration notes.'


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
            expected_name: str) -> canopy.StudyResult:
        assert study_id is not None
        state.studies_to_remove.append(study_id)

        wait_result = await canopy.wait_for_study(
            environment.session,
            study_id,
            timeout_seconds=120)

        assert expected_name == wait_result.document.name
        assert wait_result.data.job_count > 0
        assert wait_result.data.job_count == wait_result.data.completed_job_count
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
                'ApexSim',  # Intentionally wrong casing.
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
            assert study.simulation_count == 1
            assert study.succeeded_simulation_count == 1
            assert study.data.job_count == 1

    async def test_0200_it_should_create_a_study_from_references_and_loaded_configs(self, state: State):
        async with integration_tests.Environment() as environment:
            car_config_id = await canopy.create_config(
                environment.session,
                'car',
                test_car_name,
                state.default_car.raw_data,
                test_custom_properties)
            weather_config_id = await canopy.create_config(
                environment.session,
                'weather',
                test_weather_name,
                state.default_weather.raw_data,
                test_custom_properties)
            default_exploration = await canopy.load_default_config(
                environment.session,
                'exploration',
                default_exploration_name)

            default_exploration.data.design.numberOfPoints = 2
            default_exploration.properties = {
                'type': 'a'
            }
            default_exploration.notes = exploration_notes

            weather_config = await canopy.load_config(
                environment.session, weather_config_id)

            state.study_id_2 = await canopy.create_study(
                environment.session,
                'apexSim',
                test_study_name_2,
                [
                    car_config_id,
                    weather_config,
                    default_exploration,
                ])
            logger.info('Study ID 2 is {}'.format(state.study_id_2))

            study = await self.wait_for_and_verify_study(state, environment, state.study_id_2, test_study_name_2)

            properties = canopy.ensure_dict(study.document.properties)
            assert test_study_property_value == properties['car.' + test_study_property_key]
            assert test_study_property_value == properties['weather.' + test_study_property_key]
            assert 'a' == properties['exploration.type']
            assert study.simulation_count == 2
            assert study.succeeded_simulation_count == 2
            assert study.data.job_count == 3

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
            assert study.jobs is None

    async def test_0500_it_should_find_a_study_by_multiple_criteria(self, state: State):
        async with integration_tests.Environment() as environment:
            study = await canopy.find_study(
                environment.session,
                owner_username=environment.data.authentication.username,
                name=test_study_name_2,
                custom_properties=test_passed_though_custom_properties)

            assert study.document.document_id == state.study_id_2
            assert study.jobs is None

    async def test_0600_it_should_load_a_study_by_id(self, state: State):
        async with integration_tests.Environment() as environment:
            study = await canopy.load_study(
                environment.session,
                state.study_id)

            assert study.document.document_id == state.study_id
            assert study.inputs is None
            assert study.sim_types is None
            assert study.scalar_results is None

            assert study.jobs is None

    async def test_0610_it_should_load_a_study_by_id_with_data_when_no_study_scalar_results(self, state: State):
        async with integration_tests.Environment() as environment:
            study = await canopy.load_study(
                environment.session,
                state.study_id,
                include_study_full_document=True,
                include_study_scalar_results=True)

            assert study.document.document_id == state.study_id
            assert study.inputs is not None
            assert study.sim_types is not None
            assert study.scalar_results is not None
            assert study.scalar_results.results is None
            assert study.scalar_results.results_metadata is None
            assert study.scalar_results.inputs is None
            assert study.scalar_results.inputs_metadata is None

            assert study.scalar_as('hRideF200:ApexSim', 'mm') is None
            assert study.scalar_as('car.chassis.hRideFSetup+', 'mm') is None

            assert study.jobs is None

    async def test_0611_it_should_load_a_study_by_id_with_data_when_study_scalar_results_exist(self, state: State):
        async with integration_tests.Environment() as environment:
            study = await canopy.load_study(
                environment.session,
                state.study_id_2,
                include_study_full_document=True,
                include_study_scalar_results=True)

            assert study.document.document_id == state.study_id_2
            assert study.inputs is not None
            assert study.sim_types is not None
            assert study.scalar_results is not None
            assert study.scalar_results.results is not None
            assert study.scalar_results.results_metadata is not None
            assert study.scalar_results.inputs is not None
            assert study.scalar_results.inputs_metadata is not None

            assert len(study.scalar_as('hRideF200:ApexSim', 'mm')) == 2
            assert len(study.scalar_as('car.chassis.hRideFSetup+', 'mm')) == 2
            assert study.scalar_results.units['hRideF200:ApexSim'] == 'm'
            assert study.scalar_results.units['car.chassis.hRideFSetup+'] == 'm'

            # Notes are only loaded with the full study document.
            assert exploration_notes in study.document.notes

            assert study.jobs is None

    async def test_0620_it_should_load_a_study_by_id_with_job_metadata(self, state: State):
        async with integration_tests.Environment() as environment:
            study = await canopy.load_study(
                environment.session,
                state.study_id,
                include_job_metadata=True)

            assert study.document.document_id == state.study_id
            assert 1 == len(study.jobs)

            job = study.jobs[0]
            assert job.result is not None
            assert job.document is not None
            assert job.inputs is None
            assert 0 == len(job.scalar_data)
            assert 0 == len(job.vector_data.columns)
            assert 0 == len(job.vector_data)
            assert job.vector_metadata is None

    async def test_0700_it_should_load_a_study_by_id_with_data(self, state: State):
        async with integration_tests.Environment() as environment:
            study = await canopy.load_study(
                environment.session,
                state.study_id,
                sim_type='apexSim',  # Intentionally wrong casing.
                channel_names=[
                    'vCar',
                    'tLap',  # This channel won't exist.
                    'hRideF',
                ],
                include_job_inputs=True,
                include_job_scalar_results=True)

            assert study.document.document_id == state.study_id
            assert 1 == len(study.jobs)

            job = study.jobs[0]
            assert job.result is not None
            assert job.document is not None
            assert job.inputs is not None
            assert len(job.scalar_data) > 0
            assert len(job.vector_data.columns) == 2
            assert len(job.vector_data) > 10
            assert len(job.vector_metadata) > 0

            assert len(job.vector_as('vCar', 'kph')) > 0
            assert job.vector_units['vCar'] == 'm/s'

            assert job.scalar_as('hRideF200', 'mm') > 0
            assert job.scalar_units['hRideF200'] == 'm'

    async def test_0800_it_should_load_a_study_by_id_with_job_vector_metadata_only(self, state: State):
        async with integration_tests.Environment() as environment:
            study = await canopy.load_study(
                environment.session,
                state.study_id,
                sim_type='ApexSim',
                include_job_vector_metadata=True)

            assert study.document.document_id == state.study_id
            assert 1 == len(study.jobs)

            job = study.jobs[0]
            assert 0 == len(job.scalar_data)
            assert 0 == len(job.vector_data.columns)
            assert 0 == len(job.vector_data)
            assert len(job.vector_metadata) > 0

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
