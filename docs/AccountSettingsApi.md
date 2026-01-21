# canopy.openapi.AccountSettingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_settings_get**](AccountSettingsApi.md#account_settings_get) | **GET** /account-settings/{tenantId}/{userId} | Gets the account settings for the specified user.  This contains information such as their username, their email, and whether their email address  has been confirmed.
[**account_settings_put**](AccountSettingsApi.md#account_settings_put) | **PUT** /account-settings/{tenantId}/{userId} | Updates the account settings for the specified user.


# **account_settings_get**
> GetAccountSettingsResult account_settings_get(tenant_id, user_id)

Gets the account settings for the specified user.  This contains information such as their username, their email, and whether their email address  has been confirmed.

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
    api_instance = canopy.openapi.AccountSettingsApi(api_client)
    tenant_id = 'tenant_id_example' # str | The tenant ID of the user.
user_id = 'user_id_example' # str | The user ID of the user.

    try:
        # Gets the account settings for the specified user.  This contains information such as their username, their email, and whether their email address  has been confirmed.
        api_response = api_instance.account_settings_get(tenant_id, user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountSettingsApi->account_settings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID of the user. | 
 **user_id** | **str**| The user ID of the user. | 

### Return type

[**GetAccountSettingsResult**](GetAccountSettingsResult.md)

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

# **account_settings_put**
> account_settings_put(tenant_id, user_id, account_settings_put_request)

Updates the account settings for the specified user.

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
    api_instance = canopy.openapi.AccountSettingsApi(api_client)
    tenant_id = 'tenant_id_example' # str | The tenant ID of the user.
user_id = 'user_id_example' # str | The user ID of the user.
account_settings_put_request = canopy.openapi.AccountSettingsPutRequest() # AccountSettingsPutRequest | The updated account settings.  Only `NewUsername` and `NewEmail` are required, and they are only updated if they differ from the current username and email.

    try:
        # Updates the account settings for the specified user.
        api_instance.account_settings_put(tenant_id, user_id, account_settings_put_request)
    except ApiException as e:
        print("Exception when calling AccountSettingsApi->account_settings_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID of the user. | 
 **user_id** | **str**| The user ID of the user. | 
 **account_settings_put_request** | [**AccountSettingsPutRequest**](AccountSettingsPutRequest.md)| The updated account settings.  Only &#x60;NewUsername&#x60; and &#x60;NewEmail&#x60; are required, and they are only updated if they differ from the current username and email. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

