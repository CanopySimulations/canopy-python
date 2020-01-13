# canopy.swagger.UserSettingsApi

All URIs are relative to *https://localhost:44300*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_settings_get_user_settings**](UserSettingsApi.md#user_settings_get_user_settings) | **GET** /user-settings/{tenantId}/{userId} | 
[**user_settings_put_user_settings**](UserSettingsApi.md#user_settings_put_user_settings) | **PUT** /user-settings/{tenantId}/{userId} | 


# **user_settings_get_user_settings**
> GetUserSettingsQueryResult user_settings_get_user_settings(tenant_id, user_id)



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
api_instance = canopy.swagger.UserSettingsApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    api_response = api_instance.user_settings_get_user_settings(tenant_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSettingsApi->user_settings_get_user_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**GetUserSettingsQueryResult**](GetUserSettingsQueryResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_settings_put_user_settings**
> str user_settings_put_user_settings(tenant_id, user_id, data)



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
api_instance = canopy.swagger.UserSettingsApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
data = canopy.swagger.UpdatedUserSettings() # UpdatedUserSettings | 

try:
    api_response = api_instance.user_settings_put_user_settings(tenant_id, user_id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserSettingsApi->user_settings_put_user_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **data** | [**UpdatedUserSettings**](UpdatedUserSettings.md)|  | 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

