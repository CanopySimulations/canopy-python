# canopy.openapi.ListFilterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_filter_upgrade_list_filter**](ListFilterApi.md#list_filter_upgrade_list_filter) | **GET** /list-filters/upgrade | Upgrades a list filter from the old format to the new format.  This is used to upgrade list filters that were created before the new format,  supporting more complex queries, was introduced.


# **list_filter_upgrade_list_filter**
> ListFilter list_filter_upgrade_list_filter(filter=filter)

Upgrades a list filter from the old format to the new format.  This is used to upgrade list filters that were created before the new format,  supporting more complex queries, was introduced.

### Example

* OAuth Authentication (Bearer):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: Bearer
configuration = canopy.openapi.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with canopy.openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = canopy.openapi.ListFilterApi(api_client)
    filter = 'filter_example' # str | The serialized JSON representation of an old-style filter. (optional)

    try:
        # Upgrades a list filter from the old format to the new format.  This is used to upgrade list filters that were created before the new format,  supporting more complex queries, was introduced.
        api_response = api_instance.list_filter_upgrade_list_filter(filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ListFilterApi->list_filter_upgrade_list_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The serialized JSON representation of an old-style filter. | [optional] 

### Return type

[**ListFilter**](ListFilter.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

