# canopy.openapi.WorksheetApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**worksheet_get_worksheet**](WorksheetApi.md#worksheet_get_worksheet) | **GET** /worksheets/{tenantId}/{worksheetId} | 
[**worksheet_post_duplicate_configs**](WorksheetApi.md#worksheet_post_duplicate_configs) | **POST** /worksheets/{tenantId}/{worksheetId}/duplicate | 
[**worksheet_post_worksheet**](WorksheetApi.md#worksheet_post_worksheet) | **POST** /worksheets/{tenantId} | 
[**worksheet_put_worksheet**](WorksheetApi.md#worksheet_put_worksheet) | **PUT** /worksheets/{tenantId}/{worksheetId} | 


# **worksheet_get_worksheet**
> GetWorksheetQueryResult worksheet_get_worksheet(tenant_id, worksheet_id, config_version=config_version)



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
    api_instance = canopy.openapi.WorksheetApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
worksheet_id = 'worksheet_id_example' # str | 
config_version = 'config_version_example' # str |  (optional)

    try:
        api_response = api_instance.worksheet_get_worksheet(tenant_id, worksheet_id, config_version=config_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorksheetApi->worksheet_get_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **worksheet_id** | **str**|  | 
 **config_version** | **str**|  | [optional] 

### Return type

[**GetWorksheetQueryResult**](GetWorksheetQueryResult.md)

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

# **worksheet_post_duplicate_configs**
> DuplicateConfigsResult worksheet_post_duplicate_configs(tenant_id, worksheet_id, worksheet_post_duplicate_configs_request, sim_version=sim_version)



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
    api_instance = canopy.openapi.WorksheetApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
worksheet_id = 'worksheet_id_example' # str | 
worksheet_post_duplicate_configs_request = canopy.openapi.WorksheetPostDuplicateConfigsRequest() # WorksheetPostDuplicateConfigsRequest | 
sim_version = 'sim_version_example' # str |  (optional)

    try:
        api_response = api_instance.worksheet_post_duplicate_configs(tenant_id, worksheet_id, worksheet_post_duplicate_configs_request, sim_version=sim_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorksheetApi->worksheet_post_duplicate_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **worksheet_id** | **str**|  | 
 **worksheet_post_duplicate_configs_request** | [**WorksheetPostDuplicateConfigsRequest**](WorksheetPostDuplicateConfigsRequest.md)|  | 
 **sim_version** | **str**|  | [optional] 

### Return type

[**DuplicateConfigsResult**](DuplicateConfigsResult.md)

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

# **worksheet_post_worksheet**
> GetWorksheetQueryResult worksheet_post_worksheet(tenant_id, worksheet_post_worksheet_request)



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
    api_instance = canopy.openapi.WorksheetApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
worksheet_post_worksheet_request = canopy.openapi.WorksheetPostWorksheetRequest() # WorksheetPostWorksheetRequest | 

    try:
        api_response = api_instance.worksheet_post_worksheet(tenant_id, worksheet_post_worksheet_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorksheetApi->worksheet_post_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **worksheet_post_worksheet_request** | [**WorksheetPostWorksheetRequest**](WorksheetPostWorksheetRequest.md)|  | 

### Return type

[**GetWorksheetQueryResult**](GetWorksheetQueryResult.md)

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

# **worksheet_put_worksheet**
> GetWorksheetQueryResult worksheet_put_worksheet(tenant_id, worksheet_id, worksheet_put_worksheet_request)



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
    api_instance = canopy.openapi.WorksheetApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
worksheet_id = 'worksheet_id_example' # str | 
worksheet_put_worksheet_request = canopy.openapi.WorksheetPutWorksheetRequest() # WorksheetPutWorksheetRequest | 

    try:
        api_response = api_instance.worksheet_put_worksheet(tenant_id, worksheet_id, worksheet_put_worksheet_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorksheetApi->worksheet_put_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **worksheet_id** | **str**|  | 
 **worksheet_put_worksheet_request** | [**WorksheetPutWorksheetRequest**](WorksheetPutWorksheetRequest.md)|  | 

### Return type

[**GetWorksheetQueryResult**](GetWorksheetQueryResult.md)

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

