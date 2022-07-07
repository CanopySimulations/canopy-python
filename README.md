# Installation

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
See the [Canopy Python Examples](https://github.com/CanopySimulations/canopy-python-examples) repository for example usage.

## Introduction

This package is designed for customers of [Canopy Simulations](https://www.canopysimulations.com/) who would like
to access the Canopy API from Python, for example using Jupyter Notebooks.

Currently the library is split into two parts:

 - The client generated using the OpenAPI toolset is located in the "canopy/openapi" folder.
   We don't have a great deal of control over how this code looks, but it should give a fairly complete interface to the main API.

 - One folder up from that in the "canopy" folder we are adding helper functions which wrap common use cases in simple functions.
   You can also use these functions as a reference to using the OpenAPI generated code.

When using the library you generally start by creating a `canopy.Session` object. 
The session object manages authentication, and the caching of user settings.
Calling `session.authentication.authenticate()` before calling OpenAPI generated client functions ensures that you are
authenticated and that any expired access tokens are refreshed.
Our helper functions will handle calling `authenticate` before making any calls, so if you are only using our
helper functions you won't need to call it yourself.

The `session` should generally be created once per application. It will automatically dispose itself when the application
shuts down. Alternatively you can enclose it in an `async with` or a `with` block if you need to create multiple sessions,
as shown in the examples below. 

If you are using the OpenAPI generated code then you can pass the `session.async_client` or `session.sync_client` into the OpenAPI 
generated API client instance as the `api_client` parameter as shown below. Passing in `async_client` will cause it to use
`asyncio`, and you will need to `await` the calls. Passing in `sync_client` will cause the calls to complete synchronously.

Our helper functions all use `asyncio` for efficient parallelisation of downloads, and must therefore be awaited.

The following example shows how to create a session and request some output channels from a study using our helper function:

```python
import canopy
import asyncio

async with canopy.Session(client_id='<your_client_id>', username='<your_username>') as session:
    study_data = await canopy.load_study(session, '<study_id>', 'DynamicLap', ['sRun', 'vCar'])

    # Using the OpenAPI generated client directly:
    study_api = canopy.openapi.StudyApi(session.async_client)
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
You can pass `session.sync_client` into the OpenAPI client classes instead of `session.async_client` to make them 
return results synchronously.

```python
import canopy

with canopy.Session(client_id='<your_client_id>', username='<your_username>') as session:
    # Note we are using canopy.run(..) to force the async method to run synchronously.
    # This is a wrapper for asyncio.get_event_loop().run_until_complete(..).
    study_data = canopy.run(canopy.load_study(session, '<study_id>', 'DynamicLap', ['sRun', 'vCar']))

    # Using the OpenAPI generated client synchronously by passing in sync_client:
    study_api = canopy.openapi.StudyApi(session.sync_client)
    job_result = study_api.study_get_study_job_metadata(
        session.authentication.tenant_id,
        '<study_id>',
        0)

    # You can still run synchronous OpenAPI client methods asynchronously using threads if you need to:
    job_result_thread = study_api.study_get_study_job_metadata(
        session.authentication.tenant_id,
        '<study_id>',
        0,
        async_req=True)

    job_result_2 = job_result_thread.get()
```

## Proxy Servers

You can configure your proxy server by passing in a `proxy` argument to the `canopy.Session` object:
```python
async with canopy.Session(authentication_data, proxy=canopy.ProxyConfiguration('http://some.proxy.com', 'user', 'pass')) as session:
``` 

# Updating the OpenAPI Client

This needs to be tidied up, improved, and automated.

Additional options can be found here: https://openapi-generator.tech/docs/generators/openapi/
 - e.g. enumUnknownDefaultCase could be useful if the remaining exposed enums change in future. 

You can use the Dockerfile in this repository to create a docker image to generate the new API stubs:

```sh
docker image build -t canopy-python-gen:1 .
docker container run -i -t --mount type=bind,src='<path>/<to>/canopy/canopy-python',dst=/canopy/repo canopy-python-gen:1 /bin/bash
```

```sh
java -jar openapi-generator-cli.jar generate -g python-legacy -i https://api.canopysimulations.com/swagger/v1/swagger.json -o ./gen --package-name "canopy.openapi"
rm -r repo/canopy/openapi
rm -r repo/docs
cp -r gen/canopy/openapi repo/canopy
cp -r gen/docs repo
cp -r gen/README.md repo/OPENAPI_README.md
```

To regenerate the `asyncio` files execute:
```sh
rm -r gen
java -jar openapi-generator-cli.jar generate -g python-legacy -i https://api.canopysimulations.com/swagger/v1/swagger.json -o ./gen --package-name "canopy.openapi" --library asyncio
mv gen/canopy/openapi gen/canopy/openapi_asyncio
rm -r gen/canopy/openapi_asyncio/api
rm -r gen/canopy/openapi_asyncio/models
rm gen/canopy/openapi_asyncio/configuration.py
rm gen/canopy/openapi_asyncio/exceptions.py
sed -i 's/from canopy\.openapi import rest/from canopy.openapi_asyncio import rest/g' gen/canopy/openapi_asyncio/api_client.py
sed -i '/from canopy.*/d' gen/canopy/openapi_asyncio/__init__.py
sed -i '/# import /d' gen/canopy/openapi_asyncio/__init__.py
echo 'from canopy.openapi_asyncio.api_client import ApiClient' >> gen/canopy/openapi_asyncio/__init__.py
cp -r gen/canopy/openapi_asyncio repo/canopy
```

Note: The `openapi/configuration.py` file will need to be manually modified to add the default API host URL.
Note: The `openapi_asyncio/rest.py` file will need to be manually modified to support proxy servers after generation. 
Note: The `openapi_asyncio/client_api.py` and `openapi/client_api.py` files will need to be manually modified to 
support numpy array serialization after generation. 

## Documentation for OpenAPI Generated Client

OpenAPI generated documentation can be found [here](OPENAPI_README.md).
