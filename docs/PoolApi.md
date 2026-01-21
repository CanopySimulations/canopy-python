# canopy.openapi.PoolApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pool_get_pool_status**](PoolApi.md#pool_get_pool_status) | **GET** /pools/{tenantId} | Gets the status of a pool.
[**pool_get_pools**](PoolApi.md#pool_get_pools) | **GET** /pools | Gets the status of all pools.
[**pool_get_test_auto_scale_formula**](PoolApi.md#pool_get_test_auto_scale_formula) | **GET** /pools/{tenantId}/autoscale/test | Tests an auto-scale formula on a specific pool without applying it.


# **pool_get_pool_status**
> GetPoolStatusQueryResult pool_get_pool_status(tenant_id, pool_type=pool_type)

Gets the status of a pool.

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
    api_instance = canopy.openapi.PoolApi(api_client)
    tenant_id = 'tenant_id_example' # str | The tenant ID.
pool_type = 'pool_type_example' # str | The type of pool. This can be one of `primary`, `secondary`, `heavy`. (optional)

    try:
        # Gets the status of a pool.
        api_response = api_instance.pool_get_pool_status(tenant_id, pool_type=pool_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PoolApi->pool_get_pool_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 
 **pool_type** | **str**| The type of pool. This can be one of &#x60;primary&#x60;, &#x60;secondary&#x60;, &#x60;heavy&#x60;. | [optional] 

### Return type

[**GetPoolStatusQueryResult**](GetPoolStatusQueryResult.md)

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

# **pool_get_pools**
> GetPoolsQueryResult pool_get_pools()

Gets the status of all pools.

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
    api_instance = canopy.openapi.PoolApi(api_client)
    
    try:
        # Gets the status of all pools.
        api_response = api_instance.pool_get_pools()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PoolApi->pool_get_pools: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetPoolsQueryResult**](GetPoolsQueryResult.md)

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

# **pool_get_test_auto_scale_formula**
> TestAutoScaleFormulaQueryResult pool_get_test_auto_scale_formula(tenant_id, pool_id=pool_id, formula=formula)

Tests an auto-scale formula on a specific pool without applying it.

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
    api_instance = canopy.openapi.PoolApi(api_client)
    tenant_id = 'tenant_id_example' # str | The tenant ID.
pool_id = 'pool_id_example' # str | The pool ID. (optional)
formula = 'formula_example' # str | The formula to test. (optional)

    try:
        # Tests an auto-scale formula on a specific pool without applying it.
        api_response = api_instance.pool_get_test_auto_scale_formula(tenant_id, pool_id=pool_id, formula=formula)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PoolApi->pool_get_test_auto_scale_formula: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 
 **pool_id** | **str**| The pool ID. | [optional] 
 **formula** | **str**| The formula to test. | [optional] 

### Return type

[**TestAutoScaleFormulaQueryResult**](TestAutoScaleFormulaQueryResult.md)

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

