# 4.0 Release
## New Features
 - An optional `sim_version` parameter can now be passed into `load_study_data` and `load_study_job_data`.
 - Helper functions for finding and loading configs and studies.
 - Helper function for saving changes to a loaded config.
 - Helper functions for creating configs and studies.
  
## Breaking Changes
### Automatic conversion of study inputs to objects.
When loading the inputs of a study, the objects are deserialized as nested dictionaries by default.
It is generally more convenient to access these inputs as a set of nested objects, but the conversion can be expensive
for large configs such as tracks. Therefore performing this conversion previously required the user
to call the `dict_to_object` helper function as needed.

Now these inputs are automatically lazily converted to nested objects when first accessed.

Before:
```python
car_dict = job_data.inputs.car
print(car_dict['chassis']['hRideFSetup'])
car = canopy.dict_to_object(car_dict)
print(car.chassis.hRideFSetup)
```
  
After:
```python
car = job_data.inputs.car
print(car.chassis.hRideFSetup)
```

### Other Breaking Changes
 - The `dict_to_object` helper function now defaults to performing a deep conversion.
 - The `Session` object can now take an `AuthenticationData` argument, and the arguments have been re-ordered
to make this the first argument.  
 - Arguments and properties called `user_name` have been renamed to `username` for consistency with data returned
 from the API.

# 3.0 Release
## New Features
 - Scalar results can now be loaded via optional parameters to `load_study_data` and `load_study_job_data`.
 
 - Simulation input configs can now be loaded via optional parameters to `load_study_data` and `load_study_job_data`.
 
 - More unit conversion options around whether conversions are done in place, and whether copies should always be returned.

## Breaking Changes
 - Some vector data properties have been renamed for consistency with scalar data properties.

 - Refactor of how units are handled. 
Units are no longer converted to the user's preferred units automatically.
Instead, functions have been added to enable the user to easily convert to their preferred units for display.
  
# 2.0 Release
## New Features
 - Job results and channel data results are now loaded with a degree of parallelism for improved performance.
 
## Breaking Changes
 - Moved helper functions to `asyncio`, and added an `asyncio` option for 
the swagger generated client. 

# 1.0 Release
 - Initial release of this library.
 - Basic helper functions for quickly loading channel data from studies and jobs. 