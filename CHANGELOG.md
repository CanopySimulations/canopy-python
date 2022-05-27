# 8.28 Release
## New Features
 - Enums received from the API are not longer validated against a known list. This prevents otherwise innocuous updates to the API from breaking clients.

# 8.27 Release
## New Features
 - Add support for DragSimOptions config type.

# 8.23 Release
## New Features
 - Added TrackConverter study types and sim types.

# 8.17 Release
## New Features
 - Added 'inHg' unit conversion.

# 8.16 Release
## New Features
 - Added automatic retrying of calls made via `asyncio`.
 - Reduced concurrency from 10 to 5 parallel blob downloads per job to increase reliability. 

# 8.14 Release
## New Features
 - Do not throw exception for channels of different lengths within the same simulation. 

# 8.13 Release
## New Features
 - Register sessions with `atexit`, to avoid requiring session to always be inside a `with` statement. 

# 8.12 Release
## New Features
 - Add additional units.
 - Add `merged` scalar results property, which returns a DataFrame containing both the study inputs and scalar results.

# 8.11 Release
## New Features
 - Update OpenAPI generated code.

# 8.10 Release
## New Features
 - Add grams (`gm`) to units.

# 8.9 Release
## New Features
 - Numpy arrays can now be serialized as part of a config.

# 8.8 Release
## New Features
 - Helper methods will attempt to correct casing of `sim_type` and `study_type` parameters.

# 8.7 Release
## New Features
 - Added `__repr__()` and `__str__()` implementations for `StudyResult` and `StudyJobResult`.

## Bug Fixes
 - Use proxy configuration when downloading study data.

# 8.6 Release
## New Features
 - Added `__repr__()` and `__str__()` implementations for `LocalConfig` and `ConfigResult`.

# 8.5 Release
## New Features
 - Added `proxy` parameter to `Session` object for specifying proxy server configuration.
 - Added `openapi_configuration` parameter to `Session` for overriding the default configuration.

# 8.0 Release
## Breaking Changes
 - Migrated from using the [Swagger Generator](https://github.com/swagger-api/swagger-codegen) to the 
 [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) for the generated client code.
 - The namespace for the generated code has therefore changed from `canopy.swagger` to `canopy.openapi`.  

# 7.0 Release
## New Features
 - Added `scalar_as` helper function to `StudyResult` class.
 - Added `units` mapping to `StudyScalarResults` class.
 - Added `simulation_count` property to `StudyResult` class.
 
## Breaking Changes
 - Renamed `scalar_data_units` and `vector_data_units` to `scalar_units` and `vector_units` respectively in `StudyJobResult` class.

# 6.0 Release
## New Features
 - The `ConfigResult` and `LocalConfig` classes now expose a `raw_data` property for fetching the config data
 without conversion to an object.
 - The `dict_to_object` function will return the passed in data if it has already been converted to an object.
 - New helper function `load_study_scalar_results`.
 - The `load_study` helper function has been improved to support loading the aggregated study scalar results files
 and the study inputs files. Some existing optional parameters have been renamed to avoid confusion between loading job and
 study data; see Breaking Changes for more details.
 
## Breaking Changes
 - The `dict_to_object` function no longer supports shallow conversions. Use the `DynamicDictToObject` class instead.
 - When calling `find_study` the `jobs` property on the result is now set to `None` rather than an empty list.
 - Optional arguments to `load_study` have been renamed for clarity:
   - `include_inputs` is now `include_job_inputs`
   - `include_scalar_results` is now `include_job_scalar_results`
   - `include_vector_metadata` is now `include_job_vector_metadata`
   - `include_study_inputs` has been added
   - `include_study_scalar_results` has been added
 - The `data` property on `LocalConfig` will now convert the data dictionary to an object on first access, to match
 the behaviour of `ConfigResult`. A `raw_data` property has been added to allow access to the data without conversion.

# 5.3 Release
## New Features
 - Add standardised helper function to prompt for authentication information.
 
# 5.1 Release
## New Features
 - Expose vector metadata from `StudyJobResult`.
 - Add option to always load vector metadata even if no channel specified in `load_study_job` helper function.

# 5.0 Release
## Breaking Changes

 - In the `ConfigResult` class, renamed `config_data` to `data`.
 - Renamed `StudyDataResult` to `StudyResult` and `StudyJobDataResult` to `StudyJobResult`.
 - In the `StudyResult` class, renamed `study_document` to `data` and `study_result` to `result`. 

# 4.0 Release
## New Features
 - An optional `sim_version` parameter can now be passed into most helper functions which fetch or post data.
 - Helper functions for creating configs and studies.
 - Helper functions for finding and loading configs and studies.
 - Helper function for updating configs.
 - Helper function for deleting configs and studies.
  
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
 - Helper functions `load_study_data` and `load_study_job_data` have been renamed to `load_study` and `load_study_job`
 for consistency with other methods.

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