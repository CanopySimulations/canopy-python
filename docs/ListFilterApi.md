# swagger_client.ListFilterApi

All URIs are relative to *https://api.canopysimulations.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_filter_upgrade_list_filter**](ListFilterApi.md#list_filter_upgrade_list_filter) | **GET** /list-filters/upgrade | 


# **list_filter_upgrade_list_filter**
> ListFilter list_filter_upgrade_list_filter(filter=filter)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ListFilterApi(swagger_client.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

