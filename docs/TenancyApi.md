# canopy.swagger.TenancyApi

All URIs are relative to *https://localhost:44300*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenancy_get_tenant**](TenancyApi.md#tenancy_get_tenant) | **GET** /tenants/{tenantId} | 
[**tenancy_get_tenant_users**](TenancyApi.md#tenancy_get_tenant_users) | **GET** /tenants/{tenantId}/users | 
[**tenancy_get_tenants**](TenancyApi.md#tenancy_get_tenants) | **GET** /tenants | 
[**tenancy_post_tenant**](TenancyApi.md#tenancy_post_tenant) | **POST** /tenants | 
[**tenancy_put_tenant**](TenancyApi.md#tenancy_put_tenant) | **PUT** /tenants/{tenantId} | 


# **tenancy_get_tenant**
> GetTenantQueryResult tenancy_get_tenant(tenant_id)



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
api_instance = canopy.swagger.TenancyApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 

try:
    api_response = api_instance.tenancy_get_tenant(tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_get_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**GetTenantQueryResult**](GetTenantQueryResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_get_tenant_users**
> GetTenantUsersQueryResult tenancy_get_tenant_users(tenant_id)



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
api_instance = canopy.swagger.TenancyApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 

try:
    api_response = api_instance.tenancy_get_tenant_users(tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_get_tenant_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**GetTenantUsersQueryResult**](GetTenantUsersQueryResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_get_tenants**
> GetTenantsQueryResult tenancy_get_tenants()



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
api_instance = canopy.swagger.TenancyApi(canopy.swagger.ApiClient(configuration))

try:
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

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_post_tenant**
> tenancy_post_tenant(data)



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
api_instance = canopy.swagger.TenancyApi(canopy.swagger.ApiClient(configuration))
data = canopy.swagger.NewTenantData() # NewTenantData | 

try:
    api_instance.tenancy_post_tenant(data)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_post_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**NewTenantData**](NewTenantData.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_put_tenant**
> tenancy_put_tenant(tenant_id, data)



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
api_instance = canopy.swagger.TenancyApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
data = canopy.swagger.UpdatedTenantData() # UpdatedTenantData | 

try:
    api_instance.tenancy_put_tenant(tenant_id, data)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_put_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **data** | [**UpdatedTenantData**](UpdatedTenantData.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

