# canopy.openapi.TenantSettingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenant_settings_get_admin_tenant_settings**](TenantSettingsApi.md#tenant_settings_get_admin_tenant_settings) | **GET** /tenant-settings/admin/{tenantId} | 
[**tenant_settings_get_tenant_channel_import_mappings**](TenantSettingsApi.md#tenant_settings_get_tenant_channel_import_mappings) | **GET** /tenant-settings/channel-import-mappings/{tenantId} | 
[**tenant_settings_get_tenant_channel_whitelists**](TenantSettingsApi.md#tenant_settings_get_tenant_channel_whitelists) | **GET** /tenant-settings/channel-whitelists/{tenantId} | 
[**tenant_settings_get_tenant_default_custom_property_names**](TenantSettingsApi.md#tenant_settings_get_tenant_default_custom_property_names) | **GET** /tenant-settings/default-custom-property-names/{tenantId} | 
[**tenant_settings_get_tenant_settings_sim_version**](TenantSettingsApi.md#tenant_settings_get_tenant_settings_sim_version) | **GET** /tenant-settings/sim-version/{tenantId} | 
[**tenant_settings_get_tenant_worksheet_label_definitions**](TenantSettingsApi.md#tenant_settings_get_tenant_worksheet_label_definitions) | **GET** /tenant-settings/worksheet-label-definitions/{tenantId} | 
[**tenant_settings_put_admin_tenant_settings**](TenantSettingsApi.md#tenant_settings_put_admin_tenant_settings) | **PUT** /tenant-settings/admin/{tenantId} | 
[**tenant_settings_put_tenant_channel_import_mappings**](TenantSettingsApi.md#tenant_settings_put_tenant_channel_import_mappings) | **PUT** /tenant-settings/channel-import-mappings/{tenantId} | 
[**tenant_settings_put_tenant_channel_whitelists**](TenantSettingsApi.md#tenant_settings_put_tenant_channel_whitelists) | **PUT** /tenant-settings/channel-whitelists/{tenantId} | 
[**tenant_settings_put_tenant_default_custom_property_names**](TenantSettingsApi.md#tenant_settings_put_tenant_default_custom_property_names) | **PUT** /tenant-settings/default-custom-property-names/{tenantId} | 
[**tenant_settings_put_tenant_settings_sim_version**](TenantSettingsApi.md#tenant_settings_put_tenant_settings_sim_version) | **PUT** /tenant-settings/sim-version/{tenantId} | 
[**tenant_settings_put_tenant_worksheet_label_definitions**](TenantSettingsApi.md#tenant_settings_put_tenant_worksheet_label_definitions) | **PUT** /tenant-settings/worksheet-label-definitions/{tenantId} | 


# **tenant_settings_get_admin_tenant_settings**
> GetAdminTenantSettingsQueryResult tenant_settings_get_admin_tenant_settings(tenant_id)



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
    api_instance = canopy.openapi.TenantSettingsApi(api_client)
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_get_tenant_channel_import_mappings**
> GetTenantChannelImportMappingsQueryResult tenant_settings_get_tenant_channel_import_mappings(tenant_id)



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
    api_instance = canopy.openapi.TenantSettingsApi(api_client)
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_get_tenant_channel_whitelists**
> GetTenantChannelWhitelistsQueryResult tenant_settings_get_tenant_channel_whitelists(tenant_id)



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
    api_instance = canopy.openapi.TenantSettingsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        api_response = api_instance.tenant_settings_get_tenant_channel_whitelists(tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TenantSettingsApi->tenant_settings_get_tenant_channel_whitelists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**GetTenantChannelWhitelistsQueryResult**](GetTenantChannelWhitelistsQueryResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_get_tenant_default_custom_property_names**
> GetTenantDefaultCustomPropertyNamesQueryResult tenant_settings_get_tenant_default_custom_property_names(tenant_id, target_type=target_type)



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
    api_instance = canopy.openapi.TenantSettingsApi(api_client)
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_get_tenant_settings_sim_version**
> GetTenantSettingsSimVersionQueryResult tenant_settings_get_tenant_settings_sim_version(tenant_id)



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
    api_instance = canopy.openapi.TenantSettingsApi(api_client)
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_get_tenant_worksheet_label_definitions**
> GetTenantWorksheetLabelDefinitionsQueryResult tenant_settings_get_tenant_worksheet_label_definitions(tenant_id)



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
    api_instance = canopy.openapi.TenantSettingsApi(api_client)
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_put_admin_tenant_settings**
> str tenant_settings_put_admin_tenant_settings(tenant_id, tenant_settings_put_admin_tenant_settings_request)



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
    api_instance = canopy.openapi.TenantSettingsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
tenant_settings_put_admin_tenant_settings_request = canopy.openapi.TenantSettingsPutAdminTenantSettingsRequest() # TenantSettingsPutAdminTenantSettingsRequest | 

    try:
        api_response = api_instance.tenant_settings_put_admin_tenant_settings(tenant_id, tenant_settings_put_admin_tenant_settings_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TenantSettingsApi->tenant_settings_put_admin_tenant_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_settings_put_admin_tenant_settings_request** | [**TenantSettingsPutAdminTenantSettingsRequest**](TenantSettingsPutAdminTenantSettingsRequest.md)|  | 

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_put_tenant_channel_import_mappings**
> tenant_settings_put_tenant_channel_import_mappings(tenant_id, tenant_settings_put_tenant_channel_import_mappings_request)



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
    api_instance = canopy.openapi.TenantSettingsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
tenant_settings_put_tenant_channel_import_mappings_request = canopy.openapi.TenantSettingsPutTenantChannelImportMappingsRequest() # TenantSettingsPutTenantChannelImportMappingsRequest | 

    try:
        api_instance.tenant_settings_put_tenant_channel_import_mappings(tenant_id, tenant_settings_put_tenant_channel_import_mappings_request)
    except ApiException as e:
        print("Exception when calling TenantSettingsApi->tenant_settings_put_tenant_channel_import_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_settings_put_tenant_channel_import_mappings_request** | [**TenantSettingsPutTenantChannelImportMappingsRequest**](TenantSettingsPutTenantChannelImportMappingsRequest.md)|  | 

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_put_tenant_channel_whitelists**
> tenant_settings_put_tenant_channel_whitelists(tenant_id, tenant_settings_put_tenant_channel_whitelists_request)



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
    api_instance = canopy.openapi.TenantSettingsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
tenant_settings_put_tenant_channel_whitelists_request = canopy.openapi.TenantSettingsPutTenantChannelWhitelistsRequest() # TenantSettingsPutTenantChannelWhitelistsRequest | 

    try:
        api_instance.tenant_settings_put_tenant_channel_whitelists(tenant_id, tenant_settings_put_tenant_channel_whitelists_request)
    except ApiException as e:
        print("Exception when calling TenantSettingsApi->tenant_settings_put_tenant_channel_whitelists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_settings_put_tenant_channel_whitelists_request** | [**TenantSettingsPutTenantChannelWhitelistsRequest**](TenantSettingsPutTenantChannelWhitelistsRequest.md)|  | 

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_put_tenant_default_custom_property_names**
> tenant_settings_put_tenant_default_custom_property_names(tenant_id, tenant_settings_put_tenant_default_custom_property_names_request)



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
    api_instance = canopy.openapi.TenantSettingsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
tenant_settings_put_tenant_default_custom_property_names_request = canopy.openapi.TenantSettingsPutTenantDefaultCustomPropertyNamesRequest() # TenantSettingsPutTenantDefaultCustomPropertyNamesRequest | 

    try:
        api_instance.tenant_settings_put_tenant_default_custom_property_names(tenant_id, tenant_settings_put_tenant_default_custom_property_names_request)
    except ApiException as e:
        print("Exception when calling TenantSettingsApi->tenant_settings_put_tenant_default_custom_property_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_settings_put_tenant_default_custom_property_names_request** | [**TenantSettingsPutTenantDefaultCustomPropertyNamesRequest**](TenantSettingsPutTenantDefaultCustomPropertyNamesRequest.md)|  | 

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_put_tenant_settings_sim_version**
> tenant_settings_put_tenant_settings_sim_version(tenant_id, tenant_settings_put_tenant_settings_sim_version_request)



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
    api_instance = canopy.openapi.TenantSettingsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
tenant_settings_put_tenant_settings_sim_version_request = canopy.openapi.TenantSettingsPutTenantSettingsSimVersionRequest() # TenantSettingsPutTenantSettingsSimVersionRequest | 

    try:
        api_instance.tenant_settings_put_tenant_settings_sim_version(tenant_id, tenant_settings_put_tenant_settings_sim_version_request)
    except ApiException as e:
        print("Exception when calling TenantSettingsApi->tenant_settings_put_tenant_settings_sim_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_settings_put_tenant_settings_sim_version_request** | [**TenantSettingsPutTenantSettingsSimVersionRequest**](TenantSettingsPutTenantSettingsSimVersionRequest.md)|  | 

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_put_tenant_worksheet_label_definitions**
> tenant_settings_put_tenant_worksheet_label_definitions(tenant_id, tenant_settings_put_tenant_worksheet_label_definitions_request)



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
    api_instance = canopy.openapi.TenantSettingsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
tenant_settings_put_tenant_worksheet_label_definitions_request = canopy.openapi.TenantSettingsPutTenantWorksheetLabelDefinitionsRequest() # TenantSettingsPutTenantWorksheetLabelDefinitionsRequest | 

    try:
        api_instance.tenant_settings_put_tenant_worksheet_label_definitions(tenant_id, tenant_settings_put_tenant_worksheet_label_definitions_request)
    except ApiException as e:
        print("Exception when calling TenantSettingsApi->tenant_settings_put_tenant_worksheet_label_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **tenant_settings_put_tenant_worksheet_label_definitions_request** | [**TenantSettingsPutTenantWorksheetLabelDefinitionsRequest**](TenantSettingsPutTenantWorksheetLabelDefinitionsRequest.md)|  | 

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

