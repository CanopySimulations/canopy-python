# canopy.openapi.AvailabilityApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**availability_get**](AvailabilityApi.md#availability_get) | **GET** /availability | Tests the availability of the API.
[**availability_head**](AvailabilityApi.md#availability_head) | **HEAD** /availability | This method performs a simple &#x60;ping&#x60; test of the API, where the API responding is  considered a successful test.


# **availability_get**
> AvailabilityResult availability_get(full=full, ping=ping)

Tests the availability of the API.

### Example

```python
from __future__ import print_function
import time
import canopy.openapi
from canopy.openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = canopy.openapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with canopy.openapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = canopy.openapi.AvailabilityApi(api_client)
    full = False # bool | If true, a full test is performed, including running a simple simulation. (optional) (default to False)
ping = False # bool | If true, no internal tests are performed, and the API responding is the extent of the test.  This takes precedence over the `full` parameter if both are specified. (optional) (default to False)

    try:
        # Tests the availability of the API.
        api_response = api_instance.availability_get(full=full, ping=ping)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AvailabilityApi->availability_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full** | **bool**| If true, a full test is performed, including running a simple simulation. | [optional] [default to False]
 **ping** | **bool**| If true, no internal tests are performed, and the API responding is the extent of the test.  This takes precedence over the &#x60;full&#x60; parameter if both are specified. | [optional] [default to False]

### Return type

[**AvailabilityResult**](AvailabilityResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **availability_head**
> availability_head()

This method performs a simple `ping` test of the API, where the API responding is  considered a successful test.

### Example

```python
from __future__ import print_function
import time
import canopy.openapi
from canopy.openapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = canopy.openapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with canopy.openapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = canopy.openapi.AvailabilityApi(api_client)
    
    try:
        # This method performs a simple `ping` test of the API, where the API responding is  considered a successful test.
        api_instance.availability_head()
    except ApiException as e:
        print("Exception when calling AvailabilityApi->availability_head: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

