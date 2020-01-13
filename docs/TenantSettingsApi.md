# canopy.swagger.TenantSettingsApi

All URIs are relative to *https://localhost:44300*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenant_settings_get_admin_tenant_settings**](TenantSettingsApi.md#tenant_settings_get_admin_tenant_settings) | **GET** /tenant-settings/admin/{tenantId} | 
[**tenant_settings_get_tenant_channel_import_mappings**](TenantSettingsApi.md#tenant_settings_get_tenant_channel_import_mappings) | **GET** /tenant-settings/channel-import-mappings/{tenantId} | 
[**tenant_settings_get_tenant_default_custom_property_names**](TenantSettingsApi.md#tenant_settings_get_tenant_default_custom_property_names) | **GET** /tenant-settings/default-custom-property-names/{tenantId} | 
[**tenant_settings_get_tenant_settings_sim_version**](TenantSettingsApi.md#tenant_settings_get_tenant_settings_sim_version) | **GET** /tenant-settings/sim-version/{tenantId} | 
[**tenant_settings_get_tenant_worksheet_label_definitions**](TenantSettingsApi.md#tenant_settings_get_tenant_worksheet_label_definitions) | **GET** /tenant-settings/worksheet-label-definitions/{tenantId} | 
[**tenant_settings_put_admin_tenant_settings**](TenantSettingsApi.md#tenant_settings_put_admin_tenant_settings) | **PUT** /tenant-settings/admin/{tenantId} | 
[**tenant_settings_put_tenant_channel_import_mappings**](TenantSettingsApi.md#tenant_settings_put_tenant_channel_import_mappings) | **PUT** /tenant-settings/channel-import-mappings/{tenantId} | 
[**tenant_settings_put_tenant_default_custom_property_names**](TenantSettingsApi.md#tenant_settings_put_tenant_default_custom_property_names) | **PUT** /tenant-settings/default-custom-property-names/{tenantId} | 
[**tenant_settings_put_tenant_settings_sim_version**](TenantSettingsApi.md#tenant_settings_put_tenant_settings_sim_version) | **PUT** /tenant-settings/sim-version/{tenantId} | 
[**tenant_settings_put_tenant_worksheet_label_definitions**](TenantSettingsApi.md#tenant_settings_put_tenant_worksheet_label_definitions) | **PUT** /tenant-settings/worksheet-label-definitions/{tenantId} | 


# **tenant_settings_get_admin_tenant_settings**
> GetAdminTenantSettingsQueryResult tenant_settings_get_admin_tenant_settings(tenant_id)



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
api_instance = canopy.swagger.TenantSettingsApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 

try:
    api_response = api_instance.tenant_settings_get_admin_tenant_settings(tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantSettingsApi->tenant_settings_get_admin_tenant_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**GetAdminTenantSettingsQueryResult**](GetAdminTenantSettingsQueryResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_get_tenant_channel_import_mappings**
> GetTenantChannelImportMappingsQueryResult tenant_settings_get_tenant_channel_import_mappings(tenant_id)



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
api_instance = canopy.swagger.TenantSettingsApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 

try:
    api_response = api_instance.tenant_settings_get_tenant_channel_import_mappings(tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantSettingsApi->tenant_settings_get_tenant_channel_import_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**GetTenantChannelImportMappingsQueryResult**](GetTenantChannelImportMappingsQueryResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_get_tenant_default_custom_property_names**
> GetTenantDefaultCustomPropertyNamesQueryResult tenant_settings_get_tenant_default_custom_property_names(tenant_id, target_type=target_type)



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
api_instance = canopy.swagger.TenantSettingsApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
target_type = 'target_type_example' # str |  (optional)

try:
    api_response = api_instance.tenant_settings_get_tenant_default_custom_property_names(tenant_id, target_type=target_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantSettingsApi->tenant_settings_get_tenant_default_custom_property_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **target_type** | **str**|  | [optional] 

### Return type

[**GetTenantDefaultCustomPropertyNamesQueryResult**](GetTenantDefaultCustomPropertyNamesQueryResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_get_tenant_settings_sim_version**
> GetTenantSettingsSimVersionQueryResult tenant_settings_get_tenant_settings_sim_version(tenant_id)



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
api_instance = canopy.swagger.TenantSettingsApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 

try:
    api_response = api_instance.tenant_settings_get_tenant_settings_sim_version(tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantSettingsApi->tenant_settings_get_tenant_settings_sim_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**GetTenantSettingsSimVersionQueryResult**](GetTenantSettingsSimVersionQueryResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_get_tenant_worksheet_label_definitions**
> GetTenantWorksheetLabelDefinitionsQueryResult tenant_settings_get_tenant_worksheet_label_definitions(tenant_id)



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
api_instance = canopy.swagger.TenantSettingsApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 

try:
    api_response = api_instance.tenant_settings_get_tenant_worksheet_label_definitions(tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantSettingsApi->tenant_settings_get_tenant_worksheet_label_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**GetTenantWorksheetLabelDefinitionsQueryResult**](GetTenantWorksheetLabelDefinitionsQueryResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_put_admin_tenant_settings**
> str tenant_settings_put_admin_tenant_settings(tenant_id, data)



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
api_instance = canopy.swagger.TenantSettingsApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
data = canopy.swagger.UpdatedAdminTenantSettings() # UpdatedAdminTenantSettings | 

try:
    api_response = api_instance.tenant_settings_put_admin_tenant_settings(tenant_id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantSettingsApi->tenant_settings_put_admin_tenant_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **data** | [**UpdatedAdminTenantSettings**](UpdatedAdminTenantSettings.md)|  | 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_put_tenant_channel_import_mappings**
> tenant_settings_put_tenant_channel_import_mappings(tenant_id, data)



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
api_instance = canopy.swagger.TenantSettingsApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
data = canopy.swagger.UpdatedChannelImportMappings() # UpdatedChannelImportMappings | 

try:
    api_instance.tenant_settings_put_tenant_channel_import_mappings(tenant_id, data)
except ApiException as e:
    print("Exception when calling TenantSettingsApi->tenant_settings_put_tenant_channel_import_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **data** | [**UpdatedChannelImportMappings**](UpdatedChannelImportMappings.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_put_tenant_default_custom_property_names**
> tenant_settings_put_tenant_default_custom_property_names(tenant_id, data)



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
api_instance = canopy.swagger.TenantSettingsApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
data = canopy.swagger.UpdatedTenantDefaultCustomPropertyNames() # UpdatedTenantDefaultCustomPropertyNames | 

try:
    api_instance.tenant_settings_put_tenant_default_custom_property_names(tenant_id, data)
except ApiException as e:
    print("Exception when calling TenantSettingsApi->tenant_settings_put_tenant_default_custom_property_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **data** | [**UpdatedTenantDefaultCustomPropertyNames**](UpdatedTenantDefaultCustomPropertyNames.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_put_tenant_settings_sim_version**
> tenant_settings_put_tenant_settings_sim_version(tenant_id, data)



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
api_instance = canopy.swagger.TenantSettingsApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
data = canopy.swagger.UpdatedTenantSettingsSimVersion() # UpdatedTenantSettingsSimVersion | 

try:
    api_instance.tenant_settings_put_tenant_settings_sim_version(tenant_id, data)
except ApiException as e:
    print("Exception when calling TenantSettingsApi->tenant_settings_put_tenant_settings_sim_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **data** | [**UpdatedTenantSettingsSimVersion**](UpdatedTenantSettingsSimVersion.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_put_tenant_worksheet_label_definitions**
> tenant_settings_put_tenant_worksheet_label_definitions(tenant_id, data)



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
api_instance = canopy.swagger.TenantSettingsApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
data = canopy.swagger.UpdatedWorksheetLabelDefinitions() # UpdatedWorksheetLabelDefinitions | 

try:
    api_instance.tenant_settings_put_tenant_worksheet_label_definitions(tenant_id, data)
except ApiException as e:
    print("Exception when calling TenantSettingsApi->tenant_settings_put_tenant_worksheet_label_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **data** | [**UpdatedWorksheetLabelDefinitions**](UpdatedWorksheetLabelDefinitions.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

