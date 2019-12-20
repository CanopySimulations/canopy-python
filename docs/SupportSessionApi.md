# swagger_client.SupportSessionApi

All URIs are relative to *https://api.canopysimulations.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**support_session_get_all_support_sessions**](SupportSessionApi.md#support_session_get_all_support_sessions) | **GET** /support-sessions/all | 
[**support_session_get_support_session**](SupportSessionApi.md#support_session_get_support_session) | **GET** /support-sessions/{tenantId}/{documentId} | 
[**support_session_get_support_session_deprecated**](SupportSessionApi.md#support_session_get_support_session_deprecated) | **GET** /support-sessions/{tenantId}/{userId}/{documentId} | 
[**support_session_put_support_session**](SupportSessionApi.md#support_session_put_support_session) | **PUT** /support-sessions/{tenantId}/{documentId} | 
[**support_session_put_support_session_deprecated**](SupportSessionApi.md#support_session_put_support_session_deprecated) | **PUT** /support-sessions/{tenantId}/{userId}/{documentId} | 


# **support_session_get_all_support_sessions**
> GetAllSupportSessionsQueryResult support_session_get_all_support_sessions()



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
api_instance = swagger_client.SupportSessionApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.support_session_get_all_support_sessions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportSessionApi->support_session_get_all_support_sessions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAllSupportSessionsQueryResult**](GetAllSupportSessionsQueryResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_session_get_support_session**
> GetSupportSessionQueryResult support_session_get_support_session(tenant_id, document_id)



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
api_instance = swagger_client.SupportSessionApi(swagger_client.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
document_id = 'document_id_example' # str | 

try:
    api_response = api_instance.support_session_get_support_session(tenant_id, document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportSessionApi->support_session_get_support_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **document_id** | **str**|  | 

### Return type

[**GetSupportSessionQueryResult**](GetSupportSessionQueryResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_session_get_support_session_deprecated**
> GetSupportSessionQueryResult support_session_get_support_session_deprecated(tenant_id, user_id, document_id)



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
api_instance = swagger_client.SupportSessionApi(swagger_client.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
document_id = 'document_id_example' # str | 

try:
    api_response = api_instance.support_session_get_support_session_deprecated(tenant_id, user_id, document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportSessionApi->support_session_get_support_session_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **document_id** | **str**|  | 

### Return type

[**GetSupportSessionQueryResult**](GetSupportSessionQueryResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_session_put_support_session**
> support_session_put_support_session(tenant_id, document_id, data)



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
api_instance = swagger_client.SupportSessionApi(swagger_client.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
document_id = 'document_id_example' # str | 
data = swagger_client.SupportSessionData() # SupportSessionData | 

try:
    api_instance.support_session_put_support_session(tenant_id, document_id, data)
except ApiException as e:
    print("Exception when calling SupportSessionApi->support_session_put_support_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **document_id** | **str**|  | 
 **data** | [**SupportSessionData**](SupportSessionData.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_session_put_support_session_deprecated**
> support_session_put_support_session_deprecated(tenant_id, user_id, document_id, data)



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
api_instance = swagger_client.SupportSessionApi(swagger_client.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
document_id = 'document_id_example' # str | 
data = swagger_client.SupportSessionData() # SupportSessionData | 

try:
    api_instance.support_session_put_support_session_deprecated(tenant_id, user_id, document_id, data)
except ApiException as e:
    print("Exception when calling SupportSessionApi->support_session_put_support_session_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **document_id** | **str**|  | 
 **data** | [**SupportSessionData**](SupportSessionData.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

