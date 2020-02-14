# canopy.openapi.AccountSettingsApi

All URIs are relative to *https://api.canopysimulations.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_settings_get**](AccountSettingsApi.md#account_settings_get) | **GET** /account-settings/{tenantId}/{userId} | 
[**account_settings_put**](AccountSettingsApi.md#account_settings_put) | **PUT** /account-settings/{tenantId}/{userId} | 


# **account_settings_get**
> GetAccountSettingsResult account_settings_get(tenant_id, user_id)



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
    api_instance = canopy.openapi.AccountSettingsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 

    try:
        api_response = api_instance.account_settings_get(tenant_id, user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountSettingsApi->account_settings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**GetAccountSettingsResult**](GetAccountSettingsResult.md)

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

# **account_settings_put**
> account_settings_put(tenant_id, user_id, updated_account_settings_data)



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
    api_instance = canopy.openapi.AccountSettingsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
updated_account_settings_data = canopy.openapi.UpdatedAccountSettings() # UpdatedAccountSettings | 

    try:
        api_instance.account_settings_put(tenant_id, user_id, updated_account_settings_data)
    except ApiException as e:
        print("Exception when calling AccountSettingsApi->account_settings_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **updated_account_settings_data** | [**UpdatedAccountSettings**](UpdatedAccountSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

