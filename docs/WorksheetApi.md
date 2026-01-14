# canopy.openapi.WorksheetApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**worksheet_get_worksheet**](WorksheetApi.md#worksheet_get_worksheet) | **GET** /worksheets/{tenantId}/{worksheetId} | Gets a worksheet, including all resolved references and labels.
[**worksheet_post_duplicate_configs**](WorksheetApi.md#worksheet_post_duplicate_configs) | **POST** /worksheets/{tenantId}/{worksheetId}/duplicate | Duplicates the specified set of configs from the (optional) source worksheet to the target worksheet.
[**worksheet_post_worksheet**](WorksheetApi.md#worksheet_post_worksheet) | **POST** /worksheets/{tenantId} | Creates a new worksheet.
[**worksheet_put_worksheet**](WorksheetApi.md#worksheet_put_worksheet) | **PUT** /worksheets/{tenantId}/{worksheetId} | Updates a worksheet.


# **worksheet_get_worksheet**
> GetWorksheetQueryResult worksheet_get_worksheet(tenant_id, worksheet_id, config_version=config_version)

Gets a worksheet, including all resolved references and labels.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID of the worksheet.
worksheet_id = 'worksheet_id_example' # str | The worksheet ID.
config_version = 'config_version_example' # str | An optional version string, if a previous version of the worksheet is required. (optional)

    try:
        # Gets a worksheet, including all resolved references and labels.
        api_response = api_instance.worksheet_get_worksheet(tenant_id, worksheet_id, config_version=config_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorksheetApi->worksheet_get_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID of the worksheet. | 
 **worksheet_id** | **str**| The worksheet ID. | 
 **config_version** | **str**| An optional version string, if a previous version of the worksheet is required. | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **worksheet_post_duplicate_configs**
> DuplicateConfigsResult worksheet_post_duplicate_configs(tenant_id, worksheet_id, worksheet_post_duplicate_configs_request, sim_version=sim_version)

Duplicates the specified set of configs from the (optional) source worksheet to the target worksheet.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID of the target worksheet.
worksheet_id = 'worksheet_id_example' # str | The target worksheet ID.
worksheet_post_duplicate_configs_request = canopy.openapi.WorksheetPostDuplicateConfigsRequest() # WorksheetPostDuplicateConfigsRequest | The data defining which configs to duplicate.
sim_version = 'sim_version_example' # str | The sim version of the default configs. (optional)

    try:
        # Duplicates the specified set of configs from the (optional) source worksheet to the target worksheet.
        api_response = api_instance.worksheet_post_duplicate_configs(tenant_id, worksheet_id, worksheet_post_duplicate_configs_request, sim_version=sim_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorksheetApi->worksheet_post_duplicate_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID of the target worksheet. | 
 **worksheet_id** | **str**| The target worksheet ID. | 
 **worksheet_post_duplicate_configs_request** | [**WorksheetPostDuplicateConfigsRequest**](WorksheetPostDuplicateConfigsRequest.md)| The data defining which configs to duplicate. | 
 **sim_version** | **str**| The sim version of the default configs. | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **worksheet_post_worksheet**
> GetWorksheetQueryResult worksheet_post_worksheet(tenant_id, worksheet_post_worksheet_request)

Creates a new worksheet.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.
worksheet_post_worksheet_request = canopy.openapi.WorksheetPostWorksheetRequest() # WorksheetPostWorksheetRequest | The data defining the new worksheet.

    try:
        # Creates a new worksheet.
        api_response = api_instance.worksheet_post_worksheet(tenant_id, worksheet_post_worksheet_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorksheetApi->worksheet_post_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 
 **worksheet_post_worksheet_request** | [**WorksheetPostWorksheetRequest**](WorksheetPostWorksheetRequest.md)| The data defining the new worksheet. | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **worksheet_put_worksheet**
> GetWorksheetQueryResult worksheet_put_worksheet(tenant_id, worksheet_id, worksheet_put_worksheet_request)

Updates a worksheet.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID of the worksheet.
worksheet_id = 'worksheet_id_example' # str | The worksheet ID.
worksheet_put_worksheet_request = canopy.openapi.WorksheetPutWorksheetRequest() # WorksheetPutWorksheetRequest | The updated worksheet data.

    try:
        # Updates a worksheet.
        api_response = api_instance.worksheet_put_worksheet(tenant_id, worksheet_id, worksheet_put_worksheet_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorksheetApi->worksheet_put_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID of the worksheet. | 
 **worksheet_id** | **str**| The worksheet ID. | 
 **worksheet_put_worksheet_request** | [**WorksheetPutWorksheetRequest**](WorksheetPutWorksheetRequest.md)| The updated worksheet data. | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

