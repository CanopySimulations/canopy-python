# swagger_client.WorksheetApi

All URIs are relative to *https://api.canopysimulations.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**worksheet_get_worksheet**](WorksheetApi.md#worksheet_get_worksheet) | **GET** /worksheets/{tenantId}/{worksheetId} | 
[**worksheet_post_duplicate_configs**](WorksheetApi.md#worksheet_post_duplicate_configs) | **POST** /worksheets/{tenantId}/{worksheetId}/duplicate | 
[**worksheet_post_worksheet**](WorksheetApi.md#worksheet_post_worksheet) | **POST** /worksheets/{tenantId} | 
[**worksheet_put_worksheet**](WorksheetApi.md#worksheet_put_worksheet) | **PUT** /worksheets/{tenantId}/{worksheetId} | 


# **worksheet_get_worksheet**
> GetWorksheetQueryResult worksheet_get_worksheet(tenant_id, worksheet_id, config_version=config_version)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.WorksheetApi(swagger_client.ApiClient(configuration))
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

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **worksheet_post_duplicate_configs**
> DuplicateConfigsResult worksheet_post_duplicate_configs(tenant_id, worksheet_id, data, sim_version=sim_version)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.WorksheetApi(swagger_client.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
worksheet_id = 'worksheet_id_example' # str | 
data = swagger_client.DuplicateConfigsData() # DuplicateConfigsData | 
sim_version = 'sim_version_example' # str |  (optional)

try:
    api_response = api_instance.worksheet_post_duplicate_configs(tenant_id, worksheet_id, data, sim_version=sim_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorksheetApi->worksheet_post_duplicate_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **worksheet_id** | **str**|  | 
 **data** | [**DuplicateConfigsData**](DuplicateConfigsData.md)|  | 
 **sim_version** | **str**|  | [optional] 

### Return type

[**DuplicateConfigsResult**](DuplicateConfigsResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **worksheet_post_worksheet**
> GetWorksheetQueryResult worksheet_post_worksheet(tenant_id, data)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.WorksheetApi(swagger_client.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
data = swagger_client.NewWorksheetData() # NewWorksheetData | 

try:
    api_response = api_instance.worksheet_post_worksheet(tenant_id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorksheetApi->worksheet_post_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **data** | [**NewWorksheetData**](NewWorksheetData.md)|  | 

### Return type

[**GetWorksheetQueryResult**](GetWorksheetQueryResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **worksheet_put_worksheet**
> GetWorksheetQueryResult worksheet_put_worksheet(tenant_id, worksheet_id, data)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.WorksheetApi(swagger_client.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
worksheet_id = 'worksheet_id_example' # str | 
data = swagger_client.UpdatedWorksheetData() # UpdatedWorksheetData | 

try:
    api_response = api_instance.worksheet_put_worksheet(tenant_id, worksheet_id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorksheetApi->worksheet_put_worksheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **worksheet_id** | **str**|  | 
 **data** | [**UpdatedWorksheetData**](UpdatedWorksheetData.md)|  | 

### Return type

[**GetWorksheetQueryResult**](GetWorksheetQueryResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

