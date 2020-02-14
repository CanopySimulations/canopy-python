# canopy.openapi.PoolApi

All URIs are relative to *https://api.canopysimulations.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pool_get_pool_status**](PoolApi.md#pool_get_pool_status) | **GET** /pools/{tenantId} | 
[**pool_get_pools**](PoolApi.md#pool_get_pools) | **GET** /pools | 
[**pool_get_test_auto_scale_formula**](PoolApi.md#pool_get_test_auto_scale_formula) | **GET** /pools/{tenantId}/autoscale/test | 


# **pool_get_pool_status**
> GetPoolStatusQueryResult pool_get_pool_status(tenant_id, pool_type=pool_type)



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
    api_instance = canopy.openapi.PoolApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
pool_type = 'pool_type_example' # str |  (optional)

    try:
        api_response = api_instance.pool_get_pool_status(tenant_id, pool_type=pool_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PoolApi->pool_get_pool_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pool_type** | **str**|  | [optional] 

### Return type

[**GetPoolStatusQueryResult**](GetPoolStatusQueryResult.md)

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

# **pool_get_pools**
> GetPoolsQueryResult pool_get_pools()



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
    api_instance = canopy.openapi.PoolApi(api_client)
    
    try:
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

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pool_get_test_auto_scale_formula**
> TestAutoScaleFormulaQueryResult pool_get_test_auto_scale_formula(tenant_id, pool_id, formula=formula)



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
    api_instance = canopy.openapi.PoolApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
pool_id = 'pool_id_example' # str | 
formula = 'formula_example' # str |  (optional)

    try:
        api_response = api_instance.pool_get_test_auto_scale_formula(tenant_id, pool_id, formula=formula)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PoolApi->pool_get_test_auto_scale_formula: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pool_id** | **str**|  | 
 **formula** | **str**|  | [optional] 

### Return type

[**TestAutoScaleFormulaQueryResult**](TestAutoScaleFormulaQueryResult.md)

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

