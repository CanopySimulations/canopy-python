# canopy.openapi.EndToEndTestInboxApi

All URIs are relative to *https://api.canopysimulations.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**end_to_end_test_inbox_get_latest_message_and_clear_mailbox**](EndToEndTestInboxApi.md#end_to_end_test_inbox_get_latest_message_and_clear_mailbox) | **GET** /test-mailboxes/{mailboxName} | 


# **end_to_end_test_inbox_get_latest_message_and_clear_mailbox**
> object end_to_end_test_inbox_get_latest_message_and_clear_mailbox(mailbox_name)



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
    api_instance = canopy.openapi.EndToEndTestInboxApi(api_client)
    mailbox_name = 'mailbox_name_example' # str | 

    try:
        api_response = api_instance.end_to_end_test_inbox_get_latest_message_and_clear_mailbox(mailbox_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EndToEndTestInboxApi->end_to_end_test_inbox_get_latest_message_and_clear_mailbox: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox_name** | **str**|  | 

### Return type

**object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

