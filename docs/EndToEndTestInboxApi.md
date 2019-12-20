# swagger_client.EndToEndTestInboxApi

All URIs are relative to *https://api.canopysimulations.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**end_to_end_test_inbox_get_latest_message_and_clear_mailbox**](EndToEndTestInboxApi.md#end_to_end_test_inbox_get_latest_message_and_clear_mailbox) | **GET** /test-mailboxes/{mailboxName} | 


# **end_to_end_test_inbox_get_latest_message_and_clear_mailbox**
> object end_to_end_test_inbox_get_latest_message_and_clear_mailbox(mailbox_name)



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
api_instance = swagger_client.EndToEndTestInboxApi(swagger_client.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

