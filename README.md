# Installation & Usage

### Versioning

This library uses [SimVer](http://simver.org/) versioning, where a change in the major version number indicates a
breaking change and a change in the minor version number indicates a non-breaking change (such as an additional
feature or bug fix).

### Changelog

The changelog is available [here](CHANGELOG.md).

### Requirements.

This library has been tested on Python 3.6 and higher.

### pip install

```sh
pip install canopy
```

You may need to run `pip` with root permission: `sudo pip install canopy`.

From a Jupyter Notebook you can run `!pip install canopy`.

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

### Running Tests

Unit tests can be run with:
```
pytest canopy
```

Integration tests can be run with:
```
pytest integration_tests
```

To run the integration tests you'll need to ensure you have an environment variable called `CANOPY_PYTHON_INTEGRATION_TEST_CREDENTIALS`
containing the string `<client_id>|<client_secret>|<username>|<tenant_name>|<password>`.

# Getting Started

## Example Usage
See `canopy/integration_tests/test*.py` for example usage.

## Introduction

This package is designed for customers of [Canopy Simulations](https://www.canopysimulations.com/) who would like
to access the Canopy API from Python, for example using Jupyter Notebooks.

Currently the library is split into two parts:

 - The client generated using the Swagger toolset is located in the "canopy/swagger" folder.
   We don't have a great deal of control over how this code looks, but it should give a fairly complete interface to the main API.

 - One folder up from that in the "canopy" folder we are adding helper functions which wrap common use cases in simple functions.
   You can also use these functions as a reference to using the swagger generated code.

When using the library you generally start by creating a `canopy.Session` object. 
The session object manages authentication, and the caching of user settings.
Calling `session.authentication.authenticate()` before calling Swagger generated client functions ensures that you are
authenticated and that any expired access tokens are refreshed.
Our helper functions will generally handle calling authenticate before making any calls.

Once you have created a session you can pass the `session.async_client` or `session.sync_client` into the swagger 
generated client code as the `api_client` parameter as shown below.

The following example shows how to create a session and request some output channels from a study using our helper function:

```python
import canopy
import asyncio

async with canopy.Session(client_id='<your_client_id>', username='<your_username>') as session:
    study_data = await canopy.load_study(session, '<study_id>', 'DynamicLap', ['sRun', 'vCar'])

    # Using the swagger generated client directly:
    study_api = canopy.swagger.StudyApi(session.async_client)
    job_result = await study_api.study_get_study_job_metadata(
        session.authentication.tenant_id,
        '<study_id>',
        0)

    # Using asyncio.ensure_future() to enable us to perform multiple calls in parallel
    job_result_task = asyncio.ensure_future(study_api.study_get_study_job_metadata(
        session.authentication.tenant_id,
        '<study_id>',
        0))

    job_result_2 = await job_result_task

```

When running this code you will be prompted for your client secret and your password if 
it is the first time `session.authentication.authenticate()` has been called for this session instance. Alternatively
you can pass the client secret and password into the Session class (after fetching them from a secure location) to
avoid being prompted.

If you can't use `asyncio` and `async/await` you can instead instantiate the session object synchronously 
and use the `canopy.run` method when calling our async helper methods. 
You can pass `session.sync_client` into the swagger client classes instead of `session.async_client` to make them 
return results synchronously.

```python
import canopy

with canopy.Session(client_id='<your_client_id>', username='<your_username>') as session:
    # Note we are using canopy.run(..) to force the async method to run synchronously.
    # This is a wrapper for asyncio.get_event_loop().run_until_complete(..).
    study_data = canopy.run(canopy.load_study(session, '<study_id>', 'DynamicLap', ['sRun', 'vCar']))

    # Using the swagger generated client synchronously by passing in sync_client:
    study_api = canopy.swagger.StudyApi(session.sync_client)
    job_result = study_api.study_get_study_job_metadata(
        session.authentication.tenant_id,
        '<study_id>',
        0)

    # You can still run synchronous swagger client methods asynchronously using threads if you need to:
    job_result_thread = study_api.study_get_study_job_metadata(
        session.authentication.tenant_id,
        '<study_id>',
        0,
        async_req=True)

    job_result_2 = job_result_thread.get()
```

# Updating the Swagger Client

The Swagger generated part of this library may occasionally need to be regenerated as the Canopy API is updated.
Due to [a bug](https://github.com/swagger-api/swagger-codegen-generators/issues/462) in the python code generator
we cannot generate the client from the public API. Instead we can update the repository file `canopy-swagger-no-allof.json` to 
contain the latest swagger definition with the `allOf` references removed and generate from that.

Currently the easiest way to do this is with access to the Canopy source code, which is internal to Canopy.
Therefore if you believe the Swagger client requires updating you should ask us to update this library.
 
For Canopy employees: To remove `allOf` references, comment out the line `c.SchemaFilter<FixReadOnlyRefSchemaFilter>();` in 
`Canopy.Api.Swagger.SwaggerConfig`, run locally, copy the output of `https://localhost:44300/swagger/docs/v1`, and then discard
 the changes to `Canopy.Api.Swagger.SwaggerConfig`. 

Once you have an up to date `canopy-swagger-no-allof.json` file you can use the Dockerfile in this repository to 
create a docker image to generate the new API stubs:

```sh
docker image build -t canopy-python-gen:1 .
docker container run -i -t --mount type=bind,src='c:\dev\canopy\canopy-python',dst=/usr/src/app/repo canopy-python-gen:1 /bin/bash

java -jar swagger-codegen-cli.jar generate -l python -i ./repo/canopy-swagger-no-allof.json -o ./gen -DpackageName="canopy.swagger"
rsync -av gen/canopy.swagger/ gen/canopy/swagger/
rm -r repo/canopy/swagger
rm -r repo/docs
cp -r gen/canopy/swagger repo/canopy
cp -r gen/docs repo
cp -r gen/README.md repo/SWAGGER_README.md

```

To regenerate the `asyncio` files first execute:
```sh
rm -r gen
java -jar swagger-codegen-cli.jar generate -l python -i ./canopy-swagger-no-allof.json -o ./gen -DpackageName="canopy.swagger" --library asyncio
rsync -av gen/canopy.swagger/ gen/canopy/swagger/
```

Then manually remove all the files which are duplicates of the non-async versions and copy into `canopy/swagger_asyncio`.

## Documentation for Swagger Generated Client

Swagger generated documentation can be found [here](SWAGGER_README.md).
