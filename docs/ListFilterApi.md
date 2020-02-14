# canopy.openapi.ListFilterApi

All URIs are relative to *https://api.canopysimulations.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_filter_upgrade_list_filter**](ListFilterApi.md#list_filter_upgrade_list_filter) | **GET** /list-filters/upgrade | 


# **list_filter_upgrade_list_filter**
> ListFilter list_filter_upgrade_list_filter(filter=filter)



### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import canopy.openapi
from canopy.openapi.rest import ApiException
from pprint import pprint
configuration = canopy.openapi.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.canopysimulations.com
configuration.host = "https://api.canopysimulations.com"

# Enter a context with an instance of the API client
with canopy.openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = canopy.openapi.ListFilterApi(api_client)
    filter = 'filter_example' # str |  (optional)

    try:
        api_response = api_instance.list_filter_upgrade_list_filter(filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ListFilterApi->list_filter_upgrade_list_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**|  | [optional] 

### Return type

[**ListFilter**](ListFilter.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

