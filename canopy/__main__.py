from __future__ import absolute_import

import canopy


def run():
    session = canopy.Session(
        client_id='canopy',
        user_name='james.thurley')

    study_job_data = canopy.load_study_job_data(session, 'd08403aec32847de974af1008cef86cc', 'DynamicLap', ['sRun', 'vCar', 'blah'], 0)
    print(study_job_data.job.name)

    study_data = canopy.load_study_data(session, 'd08403aec32847de974af1008cef86cc', 'DynamicLap', ['sRun', 'vCar', 'blah'])
    print(study_data.study.name)
    print(len(study_data.jobs))


if __name__ == "__main__":
    run()
