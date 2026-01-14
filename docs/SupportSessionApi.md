# canopy.openapi.SupportSessionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**support_session_get_all_support_sessions**](SupportSessionApi.md#support_session_get_all_support_sessions) | **GET** /support-sessions/all | Returns all the open support sessions on the platform.
[**support_session_get_support_session**](SupportSessionApi.md#support_session_get_support_session) | **GET** /support-sessions/{tenantId}/{documentId} | Gets the support session for the specified document (config, study or worksheet).
[**support_session_get_support_session_deprecated**](SupportSessionApi.md#support_session_get_support_session_deprecated) | **GET** /support-sessions/{tenantId}/{userId}/{documentId} | 
[**support_session_put_support_session**](SupportSessionApi.md#support_session_put_support_session) | **PUT** /support-sessions/{tenantId}/{documentId} | Updates the support session for the specified document (config, study or worksheet).  Note that messages are now handled by Zendesk, and this method is now only used to  open or close a support session.
[**support_session_put_support_session_deprecated**](SupportSessionApi.md#support_session_put_support_session_deprecated) | **PUT** /support-sessions/{tenantId}/{userId}/{documentId} | 


# **support_session_get_all_support_sessions**
> GetAllSupportSessionsQueryResult support_session_get_all_support_sessions()

Returns all the open support sessions on the platform.

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
    api_instance = canopy.openapi.SupportSessionApi(api_client)
    
    try:
        # Returns all the open support sessions on the platform.
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_session_get_support_session**
> GetSupportSessionQueryResult support_session_get_support_session(tenant_id, document_id)

Gets the support session for the specified document (config, study or worksheet).

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
    api_instance = canopy.openapi.SupportSessionApi(api_client)
    tenant_id = 'tenant_id_example' # str | The tenant ID.
document_id = 'document_id_example' # str | The document ID.

    try:
        # Gets the support session for the specified document (config, study or worksheet).
        api_response = api_instance.support_session_get_support_session(tenant_id, document_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SupportSessionApi->support_session_get_support_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 
 **document_id** | **str**| The document ID. | 

### Return type

[**GetSupportSessionQueryResult**](GetSupportSessionQueryResult.md)

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

# **support_session_get_support_session_deprecated**
> GetSupportSessionQueryResult support_session_get_support_session_deprecated(tenant_id, user_id, document_id)



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
    api_instance = canopy.openapi.SupportSessionApi(api_client)
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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_session_put_support_session**
> support_session_put_support_session(tenant_id, document_id, support_session_put_support_session_request)

Updates the support session for the specified document (config, study or worksheet).  Note that messages are now handled by Zendesk, and this method is now only used to  open or close a support session.

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
    api_instance = canopy.openapi.SupportSessionApi(api_client)
    tenant_id = 'tenant_id_example' # str | The tenant ID.
document_id = 'document_id_example' # str | The document ID.
support_session_put_support_session_request = canopy.openapi.SupportSessionPutSupportSessionRequest() # SupportSessionPutSupportSessionRequest | The updated support session data. This is appended to the support session.

    try:
        # Updates the support session for the specified document (config, study or worksheet).  Note that messages are now handled by Zendesk, and this method is now only used to  open or close a support session.
        api_instance.support_session_put_support_session(tenant_id, document_id, support_session_put_support_session_request)
    except ApiException as e:
        print("Exception when calling SupportSessionApi->support_session_put_support_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 
 **document_id** | **str**| The document ID. | 
 **support_session_put_support_session_request** | [**SupportSessionPutSupportSessionRequest**](SupportSessionPutSupportSessionRequest.md)| The updated support session data. This is appended to the support session. | 

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

# **support_session_put_support_session_deprecated**
> support_session_put_support_session_deprecated(tenant_id, user_id, document_id, support_session_put_support_session_request)



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
    api_instance = canopy.openapi.SupportSessionApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
document_id = 'document_id_example' # str | 
support_session_put_support_session_request = canopy.openapi.SupportSessionPutSupportSessionRequest() # SupportSessionPutSupportSessionRequest | 

    try:
        api_instance.support_session_put_support_session_deprecated(tenant_id, user_id, document_id, support_session_put_support_session_request)
    except ApiException as e:
        print("Exception when calling SupportSessionApi->support_session_put_support_session_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **document_id** | **str**|  | 
 **support_session_put_support_session_request** | [**SupportSessionPutSupportSessionRequest**](SupportSessionPutSupportSessionRequest.md)|  | 

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

