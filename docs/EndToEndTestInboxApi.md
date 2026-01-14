# canopy.openapi.EndToEndTestInboxApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**end_to_end_test_inbox_get_latest_message_and_clear_mailbox**](EndToEndTestInboxApi.md#end_to_end_test_inbox_get_latest_message_and_clear_mailbox) | **GET** /test-mailboxes/{mailboxName} | Returns the latest message and clears the inbox.


# **end_to_end_test_inbox_get_latest_message_and_clear_mailbox**
> end_to_end_test_inbox_get_latest_message_and_clear_mailbox(mailbox_name)

Returns the latest message and clears the inbox.

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
    api_instance = canopy.openapi.EndToEndTestInboxApi(api_client)
    mailbox_name = 'mailbox_name_example' # str | The name of the mailbox, which is the portion of the email address before the @ symbol.

    try:
        # Returns the latest message and clears the inbox.
        api_instance.end_to_end_test_inbox_get_latest_message_and_clear_mailbox(mailbox_name)
    except ApiException as e:
        print("Exception when calling EndToEndTestInboxApi->end_to_end_test_inbox_get_latest_message_and_clear_mailbox: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox_name** | **str**| The name of the mailbox, which is the portion of the email address before the @ symbol. | 

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

