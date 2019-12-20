from __future__ import absolute_import

import canopy

api = canopy.Api(client_id='canopy', user_name='james.thurley')
api.authenticate()

canopy.load_study_data(api, 'd08403aec32847de974af1008cef86cc', 'DynamicLap', ['sRun', 'vCar', 'blah'], 0)
