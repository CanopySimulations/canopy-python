# canopy.openapi.TenantSettingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenant_settings_get_admin_tenant_settings**](TenantSettingsApi.md#tenant_settings_get_admin_tenant_settings) | **GET** /tenant-settings/admin/{tenantId} | Gets the administrative tenant settings. These are only available to Canopy personnel.
[**tenant_settings_get_tenant_channel_import_mappings**](TenantSettingsApi.md#tenant_settings_get_tenant_channel_import_mappings) | **GET** /tenant-settings/channel-import-mappings/{tenantId} | Gets the tenant channel import mappings, which specify how to map channels when importing telemetry.
[**tenant_settings_get_tenant_channel_whitelists**](TenantSettingsApi.md#tenant_settings_get_tenant_channel_whitelists) | **GET** /tenant-settings/channel-whitelists/{tenantId} | Gets the channel whitelists for the specified tenant.  The tenant channel whitelist specifies which channels are always whitelisted  when using that tenant&#39;s encrypted components.
[**tenant_settings_get_tenant_default_custom_property_names**](TenantSettingsApi.md#tenant_settings_get_tenant_default_custom_property_names) | **GET** /tenant-settings/default-custom-property-names/{tenantId} | Gets the default custom property names for the specified tenant.  The default custom property names will be shown by default when using the  specified config.
[**tenant_settings_get_tenant_settings_sim_version**](TenantSettingsApi.md#tenant_settings_get_tenant_settings_sim_version) | **GET** /tenant-settings/sim-version/{tenantId} | Gets the tenant sim version. This is the default sim version for the tenant, unless  overridden in an API call.  If no sim version is specified, then the platform default sim version is used.
[**tenant_settings_get_tenant_worksheet_label_definitions**](TenantSettingsApi.md#tenant_settings_get_tenant_worksheet_label_definitions) | **GET** /tenant-settings/worksheet-label-definitions/{tenantId} | Gets the tenant&#39;s worksheet label definitions. These specify what worksheet labels to show for all  users in the tenant.
[**tenant_settings_put_admin_tenant_settings**](TenantSettingsApi.md#tenant_settings_put_admin_tenant_settings) | **PUT** /tenant-settings/admin/{tenantId} | Updates the administrative tenant settings.  The provided ETag ensures that the settings have not been updated since they were last retrieved.
[**tenant_settings_put_tenant_channel_import_mappings**](TenantSettingsApi.md#tenant_settings_put_tenant_channel_import_mappings) | **PUT** /tenant-settings/channel-import-mappings/{tenantId} | Updates the tenant channel import mappings, which specify how to map channels when importing telemetry.
[**tenant_settings_put_tenant_channel_whitelists**](TenantSettingsApi.md#tenant_settings_put_tenant_channel_whitelists) | **PUT** /tenant-settings/channel-whitelists/{tenantId} | Update the whitelist of channels for the specified tenant.  The tenant channel whitelist specifies which channels are always whitelisted  when using that tenant&#39;s encrypted components.
[**tenant_settings_put_tenant_default_custom_property_names**](TenantSettingsApi.md#tenant_settings_put_tenant_default_custom_property_names) | **PUT** /tenant-settings/default-custom-property-names/{tenantId} | Updates the default custom property names for the specified tenant.  The default custom property names will be shown by default when using the  specified config.
[**tenant_settings_put_tenant_settings_sim_version**](TenantSettingsApi.md#tenant_settings_put_tenant_settings_sim_version) | **PUT** /tenant-settings/sim-version/{tenantId} | Updates the tenant sim version. This is the default sim version for the tenant, unless  overridden in an API call.  If no sim version is specified, then the platform default sim version is used.
[**tenant_settings_put_tenant_worksheet_label_definitions**](TenantSettingsApi.md#tenant_settings_put_tenant_worksheet_label_definitions) | **PUT** /tenant-settings/worksheet-label-definitions/{tenantId} | Updates the tenant&#39;s worksheet label definitions. These specify what worksheet labels to show for all  users in the tenant.


# **tenant_settings_get_admin_tenant_settings**
> GetAdminTenantSettingsQueryResult tenant_settings_get_admin_tenant_settings(tenant_id)

Gets the administrative tenant settings. These are only available to Canopy personnel.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.

    try:
        # Gets the administrative tenant settings. These are only available to Canopy personnel.
        api_response = api_instance.tenant_settings_get_admin_tenant_settings(tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TenantSettingsApi->tenant_settings_get_admin_tenant_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_get_tenant_channel_import_mappings**
> GetTenantChannelImportMappingsQueryResult tenant_settings_get_tenant_channel_import_mappings(tenant_id)

Gets the tenant channel import mappings, which specify how to map channels when importing telemetry.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.

    try:
        # Gets the tenant channel import mappings, which specify how to map channels when importing telemetry.
        api_response = api_instance.tenant_settings_get_tenant_channel_import_mappings(tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TenantSettingsApi->tenant_settings_get_tenant_channel_import_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_get_tenant_channel_whitelists**
> GetTenantChannelWhitelistsQueryResult tenant_settings_get_tenant_channel_whitelists(tenant_id)

Gets the channel whitelists for the specified tenant.  The tenant channel whitelist specifies which channels are always whitelisted  when using that tenant's encrypted components.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.

    try:
        # Gets the channel whitelists for the specified tenant.  The tenant channel whitelist specifies which channels are always whitelisted  when using that tenant's encrypted components.
        api_response = api_instance.tenant_settings_get_tenant_channel_whitelists(tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TenantSettingsApi->tenant_settings_get_tenant_channel_whitelists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_get_tenant_default_custom_property_names**
> GetTenantDefaultCustomPropertyNamesQueryResult tenant_settings_get_tenant_default_custom_property_names(tenant_id, target_type=target_type)

Gets the default custom property names for the specified tenant.  The default custom property names will be shown by default when using the  specified config.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.
target_type = 'target_type_example' # str | The target (config type, study) for which to fetch the custom properies (optional). (optional)

    try:
        # Gets the default custom property names for the specified tenant.  The default custom property names will be shown by default when using the  specified config.
        api_response = api_instance.tenant_settings_get_tenant_default_custom_property_names(tenant_id, target_type=target_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TenantSettingsApi->tenant_settings_get_tenant_default_custom_property_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 
 **target_type** | **str**| The target (config type, study) for which to fetch the custom properies (optional). | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_get_tenant_settings_sim_version**
> GetTenantSettingsSimVersionQueryResult tenant_settings_get_tenant_settings_sim_version(tenant_id)

Gets the tenant sim version. This is the default sim version for the tenant, unless  overridden in an API call.  If no sim version is specified, then the platform default sim version is used.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.

    try:
        # Gets the tenant sim version. This is the default sim version for the tenant, unless  overridden in an API call.  If no sim version is specified, then the platform default sim version is used.
        api_response = api_instance.tenant_settings_get_tenant_settings_sim_version(tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TenantSettingsApi->tenant_settings_get_tenant_settings_sim_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_get_tenant_worksheet_label_definitions**
> GetTenantWorksheetLabelDefinitionsQueryResult tenant_settings_get_tenant_worksheet_label_definitions(tenant_id)

Gets the tenant's worksheet label definitions. These specify what worksheet labels to show for all  users in the tenant.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.

    try:
        # Gets the tenant's worksheet label definitions. These specify what worksheet labels to show for all  users in the tenant.
        api_response = api_instance.tenant_settings_get_tenant_worksheet_label_definitions(tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TenantSettingsApi->tenant_settings_get_tenant_worksheet_label_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenant_settings_put_admin_tenant_settings**
> str tenant_settings_put_admin_tenant_settings(tenant_id, tenant_settings_put_admin_tenant_settings_request)

Updates the administrative tenant settings.  The provided ETag ensures that the settings have not been updated since they were last retrieved.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.
tenant_settings_put_admin_tenant_settings_request = canopy.openapi.TenantSettingsPutAdminTenantSettingsRequest() # TenantSettingsPutAdminTenantSettingsRequest | The updated admin tenant settings and ETag.

    try:
        # Updates the administrative tenant settings.  The provided ETag ensures that the settings have not been updated since they were last retrieved.
        api_response = api_instance.tenant_settings_put_admin_tenant_settings(tenant_id, tenant_settings_put_admin_tenant_settings_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TenantSettingsApi->tenant_settings_put_admin_tenant_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 
 **tenant_settings_put_admin_tenant_settings_request** | [**TenantSettingsPutAdminTenantSettingsRequest**](TenantSettingsPutAdminTenantSettingsRequest.md)| The updated admin tenant settings and ETag. | 

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

# **tenant_settings_put_tenant_channel_import_mappings**
> tenant_settings_put_tenant_channel_import_mappings(tenant_id, tenant_settings_put_tenant_channel_import_mappings_request)

Updates the tenant channel import mappings, which specify how to map channels when importing telemetry.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.
tenant_settings_put_tenant_channel_import_mappings_request = canopy.openapi.TenantSettingsPutTenantChannelImportMappingsRequest() # TenantSettingsPutTenantChannelImportMappingsRequest | The new channel import mapping data.

    try:
        # Updates the tenant channel import mappings, which specify how to map channels when importing telemetry.
        api_instance.tenant_settings_put_tenant_channel_import_mappings(tenant_id, tenant_settings_put_tenant_channel_import_mappings_request)
    except ApiException as e:
        print("Exception when calling TenantSettingsApi->tenant_settings_put_tenant_channel_import_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 
 **tenant_settings_put_tenant_channel_import_mappings_request** | [**TenantSettingsPutTenantChannelImportMappingsRequest**](TenantSettingsPutTenantChannelImportMappingsRequest.md)| The new channel import mapping data. | 

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

# **tenant_settings_put_tenant_channel_whitelists**
> tenant_settings_put_tenant_channel_whitelists(tenant_id, tenant_settings_put_tenant_channel_whitelists_request)

Update the whitelist of channels for the specified tenant.  The tenant channel whitelist specifies which channels are always whitelisted  when using that tenant's encrypted components.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.
tenant_settings_put_tenant_channel_whitelists_request = canopy.openapi.TenantSettingsPutTenantChannelWhitelistsRequest() # TenantSettingsPutTenantChannelWhitelistsRequest | The updated whitelist data.

    try:
        # Update the whitelist of channels for the specified tenant.  The tenant channel whitelist specifies which channels are always whitelisted  when using that tenant's encrypted components.
        api_instance.tenant_settings_put_tenant_channel_whitelists(tenant_id, tenant_settings_put_tenant_channel_whitelists_request)
    except ApiException as e:
        print("Exception when calling TenantSettingsApi->tenant_settings_put_tenant_channel_whitelists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 
 **tenant_settings_put_tenant_channel_whitelists_request** | [**TenantSettingsPutTenantChannelWhitelistsRequest**](TenantSettingsPutTenantChannelWhitelistsRequest.md)| The updated whitelist data. | 

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

# **tenant_settings_put_tenant_default_custom_property_names**
> tenant_settings_put_tenant_default_custom_property_names(tenant_id, tenant_settings_put_tenant_default_custom_property_names_request)

Updates the default custom property names for the specified tenant.  The default custom property names will be shown by default when using the  specified config.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.
tenant_settings_put_tenant_default_custom_property_names_request = canopy.openapi.TenantSettingsPutTenantDefaultCustomPropertyNamesRequest() # TenantSettingsPutTenantDefaultCustomPropertyNamesRequest | The updated default custom property data.

    try:
        # Updates the default custom property names for the specified tenant.  The default custom property names will be shown by default when using the  specified config.
        api_instance.tenant_settings_put_tenant_default_custom_property_names(tenant_id, tenant_settings_put_tenant_default_custom_property_names_request)
    except ApiException as e:
        print("Exception when calling TenantSettingsApi->tenant_settings_put_tenant_default_custom_property_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 
 **tenant_settings_put_tenant_default_custom_property_names_request** | [**TenantSettingsPutTenantDefaultCustomPropertyNamesRequest**](TenantSettingsPutTenantDefaultCustomPropertyNamesRequest.md)| The updated default custom property data. | 

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

# **tenant_settings_put_tenant_settings_sim_version**
> tenant_settings_put_tenant_settings_sim_version(tenant_id, tenant_settings_put_tenant_settings_sim_version_request)

Updates the tenant sim version. This is the default sim version for the tenant, unless  overridden in an API call.  If no sim version is specified, then the platform default sim version is used.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.
tenant_settings_put_tenant_settings_sim_version_request = canopy.openapi.TenantSettingsPutTenantSettingsSimVersionRequest() # TenantSettingsPutTenantSettingsSimVersionRequest | The new default sim version data.

    try:
        # Updates the tenant sim version. This is the default sim version for the tenant, unless  overridden in an API call.  If no sim version is specified, then the platform default sim version is used.
        api_instance.tenant_settings_put_tenant_settings_sim_version(tenant_id, tenant_settings_put_tenant_settings_sim_version_request)
    except ApiException as e:
        print("Exception when calling TenantSettingsApi->tenant_settings_put_tenant_settings_sim_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 
 **tenant_settings_put_tenant_settings_sim_version_request** | [**TenantSettingsPutTenantSettingsSimVersionRequest**](TenantSettingsPutTenantSettingsSimVersionRequest.md)| The new default sim version data. | 

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

# **tenant_settings_put_tenant_worksheet_label_definitions**
> tenant_settings_put_tenant_worksheet_label_definitions(tenant_id, tenant_settings_put_tenant_worksheet_label_definitions_request)

Updates the tenant's worksheet label definitions. These specify what worksheet labels to show for all  users in the tenant.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.
tenant_settings_put_tenant_worksheet_label_definitions_request = canopy.openapi.TenantSettingsPutTenantWorksheetLabelDefinitionsRequest() # TenantSettingsPutTenantWorksheetLabelDefinitionsRequest | The updated label definitions.

    try:
        # Updates the tenant's worksheet label definitions. These specify what worksheet labels to show for all  users in the tenant.
        api_instance.tenant_settings_put_tenant_worksheet_label_definitions(tenant_id, tenant_settings_put_tenant_worksheet_label_definitions_request)
    except ApiException as e:
        print("Exception when calling TenantSettingsApi->tenant_settings_put_tenant_worksheet_label_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 
 **tenant_settings_put_tenant_worksheet_label_definitions_request** | [**TenantSettingsPutTenantWorksheetLabelDefinitionsRequest**](TenantSettingsPutTenantWorksheetLabelDefinitionsRequest.md)| The updated label definitions. | 

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

