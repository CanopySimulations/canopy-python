# canopy.swagger.AccountSettingsApi

All URIs are relative to *https://localhost:44300*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_settings_get**](AccountSettingsApi.md#account_settings_get) | **GET** /account-settings/{tenantId}/{userId} | 
[**account_settings_put**](AccountSettingsApi.md#account_settings_put) | **PUT** /account-settings/{tenantId}/{userId} | 


# **account_settings_get**
> GetAccountSettingsResult account_settings_get(tenant_id, user_id)



### Example
```python
from __future__ import print_function
import time
import canopy.swagger
from canopy.swagger.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = canopy.swagger.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = canopy.swagger.AccountSettingsApi(canopy.swagger.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_settings_put**
> account_settings_put(tenant_id, user_id, updated_account_settings_data)



### Example
```python
from __future__ import print_function
import time
import canopy.swagger
from canopy.swagger.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = canopy.swagger.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = canopy.swagger.AccountSettingsApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
updated_account_settings_data = canopy.swagger.UpdatedAccountSettings() # UpdatedAccountSettings | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

