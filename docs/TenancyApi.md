# canopy.openapi.TenancyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenancy_delete_tenant**](TenancyApi.md#tenancy_delete_tenant) | **DELETE** /tenants/{tenantId} | Deletes the specified tenant. This is irreversible.  This will delete the tenant&#39;s document database, then all their blob storage containers,  and finally it will remove the tenant from the authentication database.  The data will not be recoverable.  This method can only be called once all the tenant&#39;s users have been deleted.
[**tenancy_get_tenant**](TenancyApi.md#tenancy_get_tenant) | **GET** /tenants/{tenantId} | Gets metadata about the specified tenant.
[**tenancy_get_tenant_users**](TenancyApi.md#tenancy_get_tenant_users) | **GET** /tenants/{tenantId}/users | Gets the list of users for the specified tenant.
[**tenancy_get_tenants**](TenancyApi.md#tenancy_get_tenants) | **GET** /tenants | Gets metadata about all tenants.
[**tenancy_post_tenant**](TenancyApi.md#tenancy_post_tenant) | **POST** /tenants | Creates a new tenant in the specified region, including a new database if necessary.
[**tenancy_put_tenant**](TenancyApi.md#tenancy_put_tenant) | **PUT** /tenants/{tenantId} | Updates the specified tenant.


# **tenancy_delete_tenant**
> tenancy_delete_tenant(tenant_id)

Deletes the specified tenant. This is irreversible.  This will delete the tenant's document database, then all their blob storage containers,  and finally it will remove the tenant from the authentication database.  The data will not be recoverable.  This method can only be called once all the tenant's users have been deleted.

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
    api_instance = canopy.openapi.TenancyApi(api_client)
    tenant_id = 'tenant_id_example' # str | The tenant ID.

    try:
        # Deletes the specified tenant. This is irreversible.  This will delete the tenant's document database, then all their blob storage containers,  and finally it will remove the tenant from the authentication database.  The data will not be recoverable.  This method can only be called once all the tenant's users have been deleted.
        api_instance.tenancy_delete_tenant(tenant_id)
    except ApiException as e:
        print("Exception when calling TenancyApi->tenancy_delete_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_get_tenant**
> GetTenantQueryResult tenancy_get_tenant(tenant_id)

Gets metadata about the specified tenant.

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
    api_instance = canopy.openapi.TenancyApi(api_client)
    tenant_id = 'tenant_id_example' # str | The tenant ID.

    try:
        # Gets metadata about the specified tenant.
        api_response = api_instance.tenancy_get_tenant(tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TenancyApi->tenancy_get_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 

### Return type

[**GetTenantQueryResult**](GetTenantQueryResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_get_tenant_users**
> GetTenantUsersQueryResult tenancy_get_tenant_users(tenant_id)

Gets the list of users for the specified tenant.

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
    api_instance = canopy.openapi.TenancyApi(api_client)
    tenant_id = 'tenant_id_example' # str | The tenant ID.

    try:
        # Gets the list of users for the specified tenant.
        api_response = api_instance.tenancy_get_tenant_users(tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TenancyApi->tenancy_get_tenant_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 

### Return type

[**GetTenantUsersQueryResult**](GetTenantUsersQueryResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_get_tenants**
> GetTenantsQueryResult tenancy_get_tenants()

Gets metadata about all tenants.

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
    api_instance = canopy.openapi.TenancyApi(api_client)
    
    try:
        # Gets metadata about all tenants.
        api_response = api_instance.tenancy_get_tenants()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TenancyApi->tenancy_get_tenants: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetTenantsQueryResult**](GetTenantsQueryResult.md)

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

# **tenancy_post_tenant**
> tenancy_post_tenant(tenancy_post_tenant_request=tenancy_post_tenant_request)

Creates a new tenant in the specified region, including a new database if necessary.

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
    api_instance = canopy.openapi.TenancyApi(api_client)
    tenancy_post_tenant_request = canopy.openapi.TenancyPostTenantRequest() # TenancyPostTenantRequest | A data structure containing the name, short name, region, and database ID of the new tenant.  The region and database ID are optional.  If the region isn't supplied it will default to North Europe, otherwise `east-us` is the only valid option.  If the database ID isn't specified it will default to the tenant ID.  If a database with the specified ID doesn't exist in the specified region, it will be created. (optional)

    try:
        # Creates a new tenant in the specified region, including a new database if necessary.
        api_instance.tenancy_post_tenant(tenancy_post_tenant_request=tenancy_post_tenant_request)
    except ApiException as e:
        print("Exception when calling TenancyApi->tenancy_post_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenancy_post_tenant_request** | [**TenancyPostTenantRequest**](TenancyPostTenantRequest.md)| A data structure containing the name, short name, region, and database ID of the new tenant.  The region and database ID are optional.  If the region isn&#39;t supplied it will default to North Europe, otherwise &#x60;east-us&#x60; is the only valid option.  If the database ID isn&#39;t specified it will default to the tenant ID.  If a database with the specified ID doesn&#39;t exist in the specified region, it will be created. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_put_tenant**
> tenancy_put_tenant(tenant_id, tenancy_put_tenant_request)

Updates the specified tenant.

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
    api_instance = canopy.openapi.TenancyApi(api_client)
    tenant_id = 'tenant_id_example' # str | The tenant ID to update.
tenancy_put_tenant_request = canopy.openapi.TenancyPutTenantRequest() # TenancyPutTenantRequest | A data structure optionally containing the tenant name, short name, database ID and a flag indicating whether the tenant is enabled.  Only supplied values will be updated.

    try:
        # Updates the specified tenant.
        api_instance.tenancy_put_tenant(tenant_id, tenancy_put_tenant_request)
    except ApiException as e:
        print("Exception when calling TenancyApi->tenancy_put_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID to update. | 
 **tenancy_put_tenant_request** | [**TenancyPutTenantRequest**](TenancyPutTenantRequest.md)| A data structure optionally containing the tenant name, short name, database ID and a flag indicating whether the tenant is enabled.  Only supplied values will be updated. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

