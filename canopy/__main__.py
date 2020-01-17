import canopy
import asyncio
import logging
from getpass import getpass


async def main_asynchronous(client_secret: str, password: str):
    async with canopy.Session(client_id='canopy', user_name='james.thurley', client_secret=client_secret, password=password) as session:
        study_job_data = await canopy.load_study_job_data(
            session,
            'd08403aec32847de974af1008cef86cc',
            'DynamicLap',
            ['sRun', 'vCar', 'tRun', 'hRideF'],
            0,
            include_inputs=True,
            include_scalar_results=True)
        print(study_job_data.job.name)
        weather = canopy.dict_to_object(study_job_data.inputs.weather)
        print('Air Temperature: {}C'.format(weather.TAir))
        t_lap_total = study_job_data.scalar_as('tLapTotal', 's')
        print('tLapTotal: {}s'.format(t_lap_total))
        v_car = study_job_data.vector_data['vCar']
        v_car_kph = study_job_data.vector_as('vCar', 'kph')
        print('vCar at zero: {}m/s / {}kph'.format(v_car[0], v_car_kph[0]))

        study_data = await canopy.load_study_data(
            session,
            'd08403aec32847de974af1008cef86cc',
            'DynamicLap',
            ['sRun', 'vCar', 'blah', 'tRun', 'hRideF'])
        print(study_data.study.name)
        print(len(study_data.jobs))


def main_synchronous(client_secret: str, password: str):
    with canopy.Session(client_id='canopy', user_name='james.thurley', client_secret=client_secret, password=password) as session:
        study_job_data = canopy.run(canopy.load_study_job_data(
            session,
            'd08403aec32847de974af1008cef86cc',
            'DynamicLap',
            ['sRun', 'vCar', 'tRun', 'hRideF'],
            0))
        print(study_job_data.job.name)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    client_secret = getpass('Client Secret:')
    password = getpass('Password:')
    main_synchronous(client_secret, password)
    asyncio.get_event_loop().run_until_complete(main_asynchronous(client_secret, password))
