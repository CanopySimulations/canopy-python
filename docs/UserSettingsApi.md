# canopy.openapi.UserSettingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_settings_get_user_settings**](UserSettingsApi.md#user_settings_get_user_settings) | **GET** /user-settings/{tenantId}/{userId} | Gets the specified user settings.
[**user_settings_put_user_settings**](UserSettingsApi.md#user_settings_put_user_settings) | **PUT** /user-settings/{tenantId}/{userId} | Updates the specified user settings.


# **user_settings_get_user_settings**
> GetUserSettingsQueryResult user_settings_get_user_settings(tenant_id, user_id)

Gets the specified user settings.

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
    api_instance = canopy.openapi.UserSettingsApi(api_client)
    tenant_id = 'tenant_id_example' # str | The tenant ID of the user.
user_id = 'user_id_example' # str | The user ID.

    try:
        # Gets the specified user settings.
        api_response = api_instance.user_settings_get_user_settings(tenant_id, user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserSettingsApi->user_settings_get_user_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID of the user. | 
 **user_id** | **str**| The user ID. | 

### Return type

[**GetUserSettingsQueryResult**](GetUserSettingsQueryResult.md)

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

# **user_settings_put_user_settings**
> str user_settings_put_user_settings(tenant_id, user_id, user_settings_put_user_settings_request)

Updates the specified user settings.

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
    api_instance = canopy.openapi.UserSettingsApi(api_client)
    tenant_id = 'tenant_id_example' # str | The tenant ID of the user.
user_id = 'user_id_example' # str | The user ID.
user_settings_put_user_settings_request = canopy.openapi.UserSettingsPutUserSettingsRequest() # UserSettingsPutUserSettingsRequest | The updated user settings, including the ETag returned when the settings were requested.

    try:
        # Updates the specified user settings.
        api_response = api_instance.user_settings_put_user_settings(tenant_id, user_id, user_settings_put_user_settings_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserSettingsApi->user_settings_put_user_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID of the user. | 
 **user_id** | **str**| The user ID. | 
 **user_settings_put_user_settings_request** | [**UserSettingsPutUserSettingsRequest**](UserSettingsPutUserSettingsRequest.md)| The updated user settings, including the ETag returned when the settings were requested. | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

