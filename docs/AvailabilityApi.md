# canopy.openapi.AvailabilityApi

All URIs are relative to *https://api.canopysimulations.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**availability_get**](AvailabilityApi.md#availability_get) | **GET** /Availability | 
[**availability_head**](AvailabilityApi.md#availability_head) | **HEAD** /Availability | 


# **availability_get**
> AvailabilityResult availability_get(full=full, ping=ping)



### Example

```python
from __future__ import print_function
import time
import canopy.openapi
from canopy.openapi.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with canopy.openapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = canopy.openapi.AvailabilityApi(api_client)
    full = True # bool |  (optional)
ping = True # bool |  (optional)

    try:
        api_response = api_instance.availability_get(full=full, ping=ping)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AvailabilityApi->availability_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full** | **bool**|  | [optional] 
 **ping** | **bool**|  | [optional] 

### Return type

[**AvailabilityResult**](AvailabilityResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **availability_head**
> object availability_head()



### Example

```python
from __future__ import print_function
import time
import canopy.openapi
from canopy.openapi.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with canopy.openapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = canopy.openapi.AvailabilityApi(api_client)
    
    try:
        api_response = api_instance.availability_head()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AvailabilityApi->availability_head: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

