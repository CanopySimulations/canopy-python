# canopy.openapi.SimVersionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sim_version_get_document**](SimVersionApi.md#sim_version_get_document) | **GET** /sim-versions/{simVersion}/documents/{documentPath} | 
[**sim_version_get_documents**](SimVersionApi.md#sim_version_get_documents) | **GET** /sim-versions/{simVersion}/documents | 
[**sim_version_get_downloads**](SimVersionApi.md#sim_version_get_downloads) | **GET** /sim-versions/{simVersion}/downloads | 
[**sim_version_get_sim_version**](SimVersionApi.md#sim_version_get_sim_version) | **GET** /sim-versions/current | 
[**sim_version_get_wiki_document**](SimVersionApi.md#sim_version_get_wiki_document) | **GET** /sim-versions/{wikiVersion}/wiki/{documentPath} | 
[**sim_version_post_sim_version**](SimVersionApi.md#sim_version_post_sim_version) | **POST** /sim-versions/current | 


# **sim_version_get_document**
> GetSimVersionDocumentQueryResult sim_version_get_document(sim_version, document_path, tenant_id=tenant_id)



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
    api_instance = canopy.openapi.SimVersionApi(api_client)
    sim_version = 'sim_version_example' # str | 
document_path = 'document_path_example' # str | 
tenant_id = 'tenant_id_example' # str |  (optional)

    try:
        api_response = api_instance.sim_version_get_document(sim_version, document_path, tenant_id=tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SimVersionApi->sim_version_get_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_version** | **str**|  | 
 **document_path** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 

### Return type

[**GetSimVersionDocumentQueryResult**](GetSimVersionDocumentQueryResult.md)

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

# **sim_version_get_documents**
> GetSimVersionDocumentsQueryResult sim_version_get_documents(sim_version, tenant_id=tenant_id)



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
    api_instance = canopy.openapi.SimVersionApi(api_client)
    sim_version = 'sim_version_example' # str | 
tenant_id = 'tenant_id_example' # str |  (optional)

    try:
        api_response = api_instance.sim_version_get_documents(sim_version, tenant_id=tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SimVersionApi->sim_version_get_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_version** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 

### Return type

[**GetSimVersionDocumentsQueryResult**](GetSimVersionDocumentsQueryResult.md)

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

# **sim_version_get_downloads**
> GetSimVersionDownloadsQueryResult sim_version_get_downloads(sim_version, tenant_id=tenant_id)



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
    api_instance = canopy.openapi.SimVersionApi(api_client)
    sim_version = 'sim_version_example' # str | 
tenant_id = 'tenant_id_example' # str |  (optional)

    try:
        api_response = api_instance.sim_version_get_downloads(sim_version, tenant_id=tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SimVersionApi->sim_version_get_downloads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_version** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 

### Return type

[**GetSimVersionDownloadsQueryResult**](GetSimVersionDownloadsQueryResult.md)

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

# **sim_version_get_sim_version**
> object sim_version_get_sim_version(tenant_id=tenant_id)



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
    api_instance = canopy.openapi.SimVersionApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)

    try:
        api_response = api_instance.sim_version_get_sim_version(tenant_id=tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SimVersionApi->sim_version_get_sim_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 

### Return type

**object**

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

# **sim_version_get_wiki_document**
> GetWikiDocumentQueryResult sim_version_get_wiki_document(wiki_version, document_path, tenant_id=tenant_id)



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
    api_instance = canopy.openapi.SimVersionApi(api_client)
    wiki_version = 'wiki_version_example' # str | 
document_path = 'document_path_example' # str | 
tenant_id = 'tenant_id_example' # str |  (optional)

    try:
        api_response = api_instance.sim_version_get_wiki_document(wiki_version, document_path, tenant_id=tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SimVersionApi->sim_version_get_wiki_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wiki_version** | **str**|  | 
 **document_path** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 

### Return type

[**GetWikiDocumentQueryResult**](GetWikiDocumentQueryResult.md)

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

# **sim_version_post_sim_version**
> sim_version_post_sim_version(sim_version_post_sim_version_request)



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
    api_instance = canopy.openapi.SimVersionApi(api_client)
    sim_version_post_sim_version_request = canopy.openapi.SimVersionPostSimVersionRequest() # SimVersionPostSimVersionRequest | 

    try:
        api_instance.sim_version_post_sim_version(sim_version_post_sim_version_request)
    except ApiException as e:
        print("Exception when calling SimVersionApi->sim_version_post_sim_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_version_post_sim_version_request** | [**SimVersionPostSimVersionRequest**](SimVersionPostSimVersionRequest.md)|  | 

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

