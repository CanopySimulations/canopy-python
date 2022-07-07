# canopy.openapi.ConfigApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config_decrypt**](ConfigApi.md#config_decrypt) | **POST** /configs/decrypt | 
[**config_decrypt_with_metadata**](ConfigApi.md#config_decrypt_with_metadata) | **POST** /configs/decryptWithMetadata | 
[**config_delete_config**](ConfigApi.md#config_delete_config) | **DELETE** /configs/{tenantId}/{configId} | 
[**config_delete_config_deprecated**](ConfigApi.md#config_delete_config_deprecated) | **DELETE** /configs/{tenantId}/{userId}/{configId} | 
[**config_encrypt**](ConfigApi.md#config_encrypt) | **POST** /configs/encrypt | 
[**config_encrypt_with_metadata**](ConfigApi.md#config_encrypt_with_metadata) | **POST** /configs/encryptWithMetadata | 
[**config_get_config**](ConfigApi.md#config_get_config) | **GET** /configs/{tenantId}/{configId} | 
[**config_get_config_deprecated**](ConfigApi.md#config_get_config_deprecated) | **GET** /configs/{tenantId}/{userId}/{configId} | 
[**config_get_config_names**](ConfigApi.md#config_get_config_names) | **GET** /configs/{tenantId}/names | 
[**config_get_config_versions**](ConfigApi.md#config_get_config_versions) | **GET** /configs/{tenantId}/{configId}/versions | 
[**config_get_config_versions_deprecated**](ConfigApi.md#config_get_config_versions_deprecated) | **GET** /configs/{tenantId}/{userId}/{configId}/versions | 
[**config_get_config_without_user_id_deprecated**](ConfigApi.md#config_get_config_without_user_id_deprecated) | **GET** /configs/{tenantId}/auto/{configId} | 
[**config_get_configs**](ConfigApi.md#config_get_configs) | **GET** /configs/{tenantId} | 
[**config_post_config**](ConfigApi.md#config_post_config) | **POST** /configs/{tenantId} | 
[**config_post_config_deprecated**](ConfigApi.md#config_post_config_deprecated) | **POST** /configs/{tenantId}/{userId} | 
[**config_post_configs**](ConfigApi.md#config_post_configs) | **POST** /configs/{tenantId}/batch | 
[**config_post_configs_deprecated**](ConfigApi.md#config_post_configs_deprecated) | **POST** /configs/{tenantId}/{userId}/batch | 
[**config_put_config**](ConfigApi.md#config_put_config) | **PUT** /configs/{tenantId}/{configId} | 
[**config_put_config_deprecated**](ConfigApi.md#config_put_config_deprecated) | **PUT** /configs/{tenantId}/{userId}/{configId} | 
[**config_put_config_owner**](ConfigApi.md#config_put_config_owner) | **PUT** /configs/{tenantId}/{configId}/owner | 
[**config_upgrade_config**](ConfigApi.md#config_upgrade_config) | **POST** /configs/upgrade/{tenantId}/{targetSimVersion} | 
[**config_upgrade_config_deprecated**](ConfigApi.md#config_upgrade_config_deprecated) | **POST** /configs/upgrade/{targetSimVersion} | 


# **config_decrypt**
> object config_decrypt(body)



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
    api_instance = canopy.openapi.ConfigApi(api_client)
    body = None # object | 

    try:
        api_response = api_instance.config_decrypt(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_decrypt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

**object**

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

# **config_decrypt_with_metadata**
> GetDecryptedDataQueryResult config_decrypt_with_metadata(config_decrypt_with_metadata_request)



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
    api_instance = canopy.openapi.ConfigApi(api_client)
    config_decrypt_with_metadata_request = canopy.openapi.ConfigDecryptWithMetadataRequest() # ConfigDecryptWithMetadataRequest | 

    try:
        api_response = api_instance.config_decrypt_with_metadata(config_decrypt_with_metadata_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_decrypt_with_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_decrypt_with_metadata_request** | [**ConfigDecryptWithMetadataRequest**](ConfigDecryptWithMetadataRequest.md)|  | 

### Return type

[**GetDecryptedDataQueryResult**](GetDecryptedDataQueryResult.md)

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

# **config_delete_config**
> config_delete_config(tenant_id, config_id, sub_tree_path=sub_tree_path, undelete=undelete)



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
    api_instance = canopy.openapi.ConfigApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
config_id = 'config_id_example' # str | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)
undelete = False # bool |  (optional) (default to False)

    try:
        api_instance.config_delete_config(tenant_id, config_id, sub_tree_path=sub_tree_path, undelete=undelete)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_delete_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **config_id** | **str**|  | 
 **sub_tree_path** | **str**|  | [optional] 
 **undelete** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_delete_config_deprecated**
> config_delete_config_deprecated(tenant_id, user_id, config_id, sub_tree_path=sub_tree_path, undelete=undelete)



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
    api_instance = canopy.openapi.ConfigApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
config_id = 'config_id_example' # str | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)
undelete = False # bool |  (optional) (default to False)

    try:
        api_instance.config_delete_config_deprecated(tenant_id, user_id, config_id, sub_tree_path=sub_tree_path, undelete=undelete)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_delete_config_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **config_id** | **str**|  | 
 **sub_tree_path** | **str**|  | [optional] 
 **undelete** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_encrypt**
> object config_encrypt(body, description=description)



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
    api_instance = canopy.openapi.ConfigApi(api_client)
    body = None # object | 
description = 'description_example' # str |  (optional)

    try:
        api_response = api_instance.config_encrypt(body, description=description)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_encrypt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 
 **description** | **str**|  | [optional] 

### Return type

**object**

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

# **config_encrypt_with_metadata**
> GetEncryptedDataQueryResult config_encrypt_with_metadata(config_encrypt_with_metadata_request)



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
    api_instance = canopy.openapi.ConfigApi(api_client)
    config_encrypt_with_metadata_request = canopy.openapi.ConfigEncryptWithMetadataRequest() # ConfigEncryptWithMetadataRequest | 

    try:
        api_response = api_instance.config_encrypt_with_metadata(config_encrypt_with_metadata_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_encrypt_with_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_encrypt_with_metadata_request** | [**ConfigEncryptWithMetadataRequest**](ConfigEncryptWithMetadataRequest.md)|  | 

### Return type

[**GetEncryptedDataQueryResult**](GetEncryptedDataQueryResult.md)

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

# **config_get_config**
> GetConfigQueryResult config_get_config(tenant_id, config_id, sub_tree_path=sub_tree_path, sim_version=sim_version, config_version=config_version)



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
    api_instance = canopy.openapi.ConfigApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
config_id = 'config_id_example' # str | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)
sim_version = 'sim_version_example' # str |  (optional)
config_version = 'config_version_example' # str |  (optional)

    try:
        api_response = api_instance.config_get_config(tenant_id, config_id, sub_tree_path=sub_tree_path, sim_version=sim_version, config_version=config_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_get_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **config_id** | **str**|  | 
 **sub_tree_path** | **str**|  | [optional] 
 **sim_version** | **str**|  | [optional] 
 **config_version** | **str**|  | [optional] 

### Return type

[**GetConfigQueryResult**](GetConfigQueryResult.md)

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

# **config_get_config_deprecated**
> GetConfigQueryResult config_get_config_deprecated(tenant_id, user_id, config_id, sub_tree_path=sub_tree_path, sim_version=sim_version, config_version=config_version)



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
    api_instance = canopy.openapi.ConfigApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
config_id = 'config_id_example' # str | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)
sim_version = 'sim_version_example' # str |  (optional)
config_version = 'config_version_example' # str |  (optional)

    try:
        api_response = api_instance.config_get_config_deprecated(tenant_id, user_id, config_id, sub_tree_path=sub_tree_path, sim_version=sim_version, config_version=config_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_get_config_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **config_id** | **str**|  | 
 **sub_tree_path** | **str**|  | [optional] 
 **sim_version** | **str**|  | [optional] 
 **config_version** | **str**|  | [optional] 

### Return type

[**GetConfigQueryResult**](GetConfigQueryResult.md)

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

# **config_get_config_names**
> GetConfigNamesQueryResult config_get_config_names(tenant_id, config_type, result_type=result_type, sub_tree_path=sub_tree_path, sim_version=sim_version)



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
    api_instance = canopy.openapi.ConfigApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
config_type = 'config_type_example' # str | 
result_type = 'result_type_example' # str |  (optional)
sub_tree_path = 'sub_tree_path_example' # str |  (optional)
sim_version = 'sim_version_example' # str |  (optional)

    try:
        api_response = api_instance.config_get_config_names(tenant_id, config_type, result_type=result_type, sub_tree_path=sub_tree_path, sim_version=sim_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_get_config_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **config_type** | **str**|  | 
 **result_type** | **str**|  | [optional] 
 **sub_tree_path** | **str**|  | [optional] 
 **sim_version** | **str**|  | [optional] 

### Return type

[**GetConfigNamesQueryResult**](GetConfigNamesQueryResult.md)

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

# **config_get_config_versions**
> GetConfigVersionsQueryResult config_get_config_versions(tenant_id, config_id, sub_tree_path=sub_tree_path)



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
    api_instance = canopy.openapi.ConfigApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
config_id = 'config_id_example' # str | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)

    try:
        api_response = api_instance.config_get_config_versions(tenant_id, config_id, sub_tree_path=sub_tree_path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_get_config_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **config_id** | **str**|  | 
 **sub_tree_path** | **str**|  | [optional] 

### Return type

[**GetConfigVersionsQueryResult**](GetConfigVersionsQueryResult.md)

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

# **config_get_config_versions_deprecated**
> GetConfigVersionsQueryResult config_get_config_versions_deprecated(tenant_id, user_id, config_id, sub_tree_path=sub_tree_path)



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
    api_instance = canopy.openapi.ConfigApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
config_id = 'config_id_example' # str | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)

    try:
        api_response = api_instance.config_get_config_versions_deprecated(tenant_id, user_id, config_id, sub_tree_path=sub_tree_path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_get_config_versions_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **config_id** | **str**|  | 
 **sub_tree_path** | **str**|  | [optional] 

### Return type

[**GetConfigVersionsQueryResult**](GetConfigVersionsQueryResult.md)

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

# **config_get_config_without_user_id_deprecated**
> GetConfigQueryResult config_get_config_without_user_id_deprecated(tenant_id, config_id, sub_tree_path=sub_tree_path, sim_version=sim_version, config_version=config_version)



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
    api_instance = canopy.openapi.ConfigApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
config_id = 'config_id_example' # str | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)
sim_version = 'sim_version_example' # str |  (optional)
config_version = 'config_version_example' # str |  (optional)

    try:
        api_response = api_instance.config_get_config_without_user_id_deprecated(tenant_id, config_id, sub_tree_path=sub_tree_path, sim_version=sim_version, config_version=config_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_get_config_without_user_id_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **config_id** | **str**|  | 
 **sub_tree_path** | **str**|  | [optional] 
 **sim_version** | **str**|  | [optional] 
 **config_version** | **str**|  | [optional] 

### Return type

[**GetConfigQueryResult**](GetConfigQueryResult.md)

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

# **config_get_configs**
> GetConfigsQueryResult config_get_configs(tenant_id, config_type, filter=filter, sub_tree_path=sub_tree_path, result_type=result_type)



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
    api_instance = canopy.openapi.ConfigApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
config_type = 'config_type_example' # str | 
filter = 'filter_example' # str |  (optional)
sub_tree_path = 'sub_tree_path_example' # str |  (optional)
result_type = 'result_type_example' # str |  (optional)

    try:
        api_response = api_instance.config_get_configs(tenant_id, config_type, filter=filter, sub_tree_path=sub_tree_path, result_type=result_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_get_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **config_type** | **str**|  | 
 **filter** | **str**|  | [optional] 
 **sub_tree_path** | **str**|  | [optional] 
 **result_type** | **str**|  | [optional] 

### Return type

[**GetConfigsQueryResult**](GetConfigsQueryResult.md)

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

# **config_post_config**
> str config_post_config(tenant_id, config_post_config_request, sub_tree_path=sub_tree_path)



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
    api_instance = canopy.openapi.ConfigApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
config_post_config_request = canopy.openapi.ConfigPostConfigRequest() # ConfigPostConfigRequest | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)

    try:
        api_response = api_instance.config_post_config(tenant_id, config_post_config_request, sub_tree_path=sub_tree_path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_post_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **config_post_config_request** | [**ConfigPostConfigRequest**](ConfigPostConfigRequest.md)|  | 
 **sub_tree_path** | **str**|  | [optional] 

### Return type

**str**

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

# **config_post_config_deprecated**
> str config_post_config_deprecated(tenant_id, user_id, config_post_config_request, sub_tree_path=sub_tree_path)



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
    api_instance = canopy.openapi.ConfigApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
config_post_config_request = canopy.openapi.ConfigPostConfigRequest() # ConfigPostConfigRequest | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)

    try:
        api_response = api_instance.config_post_config_deprecated(tenant_id, user_id, config_post_config_request, sub_tree_path=sub_tree_path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_post_config_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **config_post_config_request** | [**ConfigPostConfigRequest**](ConfigPostConfigRequest.md)|  | 
 **sub_tree_path** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_post_configs**
> BatchCreateConfigsResult config_post_configs(tenant_id, config_post_configs_request, sub_tree_path=sub_tree_path)



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
    api_instance = canopy.openapi.ConfigApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
config_post_configs_request = canopy.openapi.ConfigPostConfigsRequest() # ConfigPostConfigsRequest | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)

    try:
        api_response = api_instance.config_post_configs(tenant_id, config_post_configs_request, sub_tree_path=sub_tree_path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_post_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **config_post_configs_request** | [**ConfigPostConfigsRequest**](ConfigPostConfigsRequest.md)|  | 
 **sub_tree_path** | **str**|  | [optional] 

### Return type

[**BatchCreateConfigsResult**](BatchCreateConfigsResult.md)

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

# **config_post_configs_deprecated**
> BatchCreateConfigsResult config_post_configs_deprecated(tenant_id, user_id, config_post_configs_request, sub_tree_path=sub_tree_path)



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
    api_instance = canopy.openapi.ConfigApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
config_post_configs_request = canopy.openapi.ConfigPostConfigsRequest() # ConfigPostConfigsRequest | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)

    try:
        api_response = api_instance.config_post_configs_deprecated(tenant_id, user_id, config_post_configs_request, sub_tree_path=sub_tree_path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_post_configs_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **config_post_configs_request** | [**ConfigPostConfigsRequest**](ConfigPostConfigsRequest.md)|  | 
 **sub_tree_path** | **str**|  | [optional] 

### Return type

[**BatchCreateConfigsResult**](BatchCreateConfigsResult.md)

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

# **config_put_config**
> config_put_config(tenant_id, config_id, config_put_config_request, sub_tree_path=sub_tree_path)



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
    api_instance = canopy.openapi.ConfigApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
config_id = 'config_id_example' # str | 
config_put_config_request = canopy.openapi.ConfigPutConfigRequest() # ConfigPutConfigRequest | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)

    try:
        api_instance.config_put_config(tenant_id, config_id, config_put_config_request, sub_tree_path=sub_tree_path)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_put_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **config_id** | **str**|  | 
 **config_put_config_request** | [**ConfigPutConfigRequest**](ConfigPutConfigRequest.md)|  | 
 **sub_tree_path** | **str**|  | [optional] 

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

# **config_put_config_deprecated**
> config_put_config_deprecated(tenant_id, user_id, config_id, config_put_config_request, sub_tree_path=sub_tree_path)



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
    api_instance = canopy.openapi.ConfigApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
config_id = 'config_id_example' # str | 
config_put_config_request = canopy.openapi.ConfigPutConfigRequest() # ConfigPutConfigRequest | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)

    try:
        api_instance.config_put_config_deprecated(tenant_id, user_id, config_id, config_put_config_request, sub_tree_path=sub_tree_path)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_put_config_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **config_id** | **str**|  | 
 **config_put_config_request** | [**ConfigPutConfigRequest**](ConfigPutConfigRequest.md)|  | 
 **sub_tree_path** | **str**|  | [optional] 

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

# **config_put_config_owner**
> config_put_config_owner(tenant_id, config_id, config_put_config_owner_request)



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
    api_instance = canopy.openapi.ConfigApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
config_id = 'config_id_example' # str | 
config_put_config_owner_request = canopy.openapi.ConfigPutConfigOwnerRequest() # ConfigPutConfigOwnerRequest | 

    try:
        api_instance.config_put_config_owner(tenant_id, config_id, config_put_config_owner_request)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_put_config_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **config_id** | **str**|  | 
 **config_put_config_owner_request** | [**ConfigPutConfigOwnerRequest**](ConfigPutConfigOwnerRequest.md)|  | 

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

# **config_upgrade_config**
> UpgradeConfigQueryResult config_upgrade_config(tenant_id, target_sim_version, config_upgrade_config_deprecated_request, sub_tree_path=sub_tree_path)



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
    api_instance = canopy.openapi.ConfigApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
target_sim_version = 'target_sim_version_example' # str | 
config_upgrade_config_deprecated_request = canopy.openapi.ConfigUpgradeConfigDeprecatedRequest() # ConfigUpgradeConfigDeprecatedRequest | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)

    try:
        api_response = api_instance.config_upgrade_config(tenant_id, target_sim_version, config_upgrade_config_deprecated_request, sub_tree_path=sub_tree_path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_upgrade_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **target_sim_version** | **str**|  | 
 **config_upgrade_config_deprecated_request** | [**ConfigUpgradeConfigDeprecatedRequest**](ConfigUpgradeConfigDeprecatedRequest.md)|  | 
 **sub_tree_path** | **str**|  | [optional] 

### Return type

[**UpgradeConfigQueryResult**](UpgradeConfigQueryResult.md)

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

# **config_upgrade_config_deprecated**
> UpgradeConfigQueryResult config_upgrade_config_deprecated(target_sim_version, config_upgrade_config_deprecated_request, sub_tree_path=sub_tree_path)



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
    api_instance = canopy.openapi.ConfigApi(api_client)
    target_sim_version = 'target_sim_version_example' # str | 
config_upgrade_config_deprecated_request = canopy.openapi.ConfigUpgradeConfigDeprecatedRequest() # ConfigUpgradeConfigDeprecatedRequest | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)

    try:
        api_response = api_instance.config_upgrade_config_deprecated(target_sim_version, config_upgrade_config_deprecated_request, sub_tree_path=sub_tree_path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_upgrade_config_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_sim_version** | **str**|  | 
 **config_upgrade_config_deprecated_request** | [**ConfigUpgradeConfigDeprecatedRequest**](ConfigUpgradeConfigDeprecatedRequest.md)|  | 
 **sub_tree_path** | **str**|  | [optional] 

### Return type

[**UpgradeConfigQueryResult**](UpgradeConfigQueryResult.md)

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

