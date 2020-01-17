import canopy
import asyncio
import logging


async def main_asynchronous():
    async with canopy.Session(client_id='canopy', user_name='james.thurley') as session:
        study_job_data = await canopy.load_study_job_data(
            session,
            'd08403aec32847de974af1008cef86cc',
            'DynamicLap',
            ['sRun', 'vCar', 'tRun', 'hRideF'],
            0)
        print(study_job_data.job.name)

        study_data = await canopy.load_study_data(
            session,
            'd08403aec32847de974af1008cef86cc',
            'DynamicLap',
            ['sRun', 'vCar', 'blah', 'tRun', 'hRideF'])
        print(study_data.study.name)
        print(len(study_data.jobs))


def main_synchronous():
    with canopy.Session(client_id='canopy', user_name='james.thurley') as session:
        study_job_data = canopy.run(canopy.load_study_job_data(
            session,
            'd08403aec32847de974af1008cef86cc',
            'DynamicLap',
            ['sRun', 'vCar', 'tRun', 'hRideF'],
            0))
        print(study_job_data.job.name)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main_synchronous()
    asyncio.get_event_loop().run_until_complete(main_asynchronous())
