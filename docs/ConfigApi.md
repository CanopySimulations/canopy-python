# canopy.openapi.ConfigApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config_decrypt**](ConfigApi.md#config_decrypt) | **POST** /configs/decrypt | Decrypts the provided data.
[**config_decrypt_with_metadata**](ConfigApi.md#config_decrypt_with_metadata) | **POST** /configs/decryptWithMetadata | Decrypts the provided data.
[**config_delete_config**](ConfigApi.md#config_delete_config) | **DELETE** /configs/{tenantId}/{configId} | Deletes an existing config.
[**config_delete_config_deprecated**](ConfigApi.md#config_delete_config_deprecated) | **DELETE** /configs/{tenantId}/{userId}/{configId} | Deletes an existing config for the specified tenant and user.
[**config_encrypt**](ConfigApi.md#config_encrypt) | **POST** /configs/encrypt | Encrypts the provided data.
[**config_encrypt_with_metadata**](ConfigApi.md#config_encrypt_with_metadata) | **POST** /configs/encryptWithMetadata | Encrypted the provided data using the optional description and channel whitelist.
[**config_get_config**](ConfigApi.md#config_get_config) | **GET** /configs/{tenantId}/{configId} | Gets an existing config.
[**config_get_config_deprecated**](ConfigApi.md#config_get_config_deprecated) | **GET** /configs/{tenantId}/{userId}/{configId} | Gets an existing config for the specified tenant and user.
[**config_get_config_names**](ConfigApi.md#config_get_config_names) | **GET** /configs/{tenantId}/names | This method returns a list of config names for the specified config type,  optionally along with the most recent config ID and user ID of each config name.  It also returns the names of the default configs which are part of the specified sim version.
[**config_get_config_sub_paths**](ConfigApi.md#config_get_config_sub_paths) | **GET** /configs/{tenantId}/component-paths | Gets all the unique component paths for the specified tenant and config type.
[**config_get_config_versions**](ConfigApi.md#config_get_config_versions) | **GET** /configs/{tenantId}/{configId}/versions | Gets the version history of an existing config. Note that we do not keep a complete version history, so  the returned list of versions may not be exhaustive.
[**config_get_config_versions_deprecated**](ConfigApi.md#config_get_config_versions_deprecated) | **GET** /configs/{tenantId}/{userId}/{configId}/versions | Gets the versions of an existing config for the specified tenant and user.
[**config_get_config_without_user_id_deprecated**](ConfigApi.md#config_get_config_without_user_id_deprecated) | **GET** /configs/{tenantId}/auto/{configId} | Gets an existing config for the specified tenant without specifying a user ID.
[**config_get_configs**](ConfigApi.md#config_get_configs) | **GET** /configs/{tenantId} | Given the provided filter information, this method returns:  - a list of configs (metadata only)  - a list of custom property groups  ResultType can be used to specify which of the above lists to return.                The list of configs may contain a continuation token of more results are available. The continuation token  can be passed into a subsequent query as part of the filter to retrieve the next page of results.                The list of custom property groups is not guaranteed to be complete. It is a best effort.
[**config_post_config**](ConfigApi.md#config_post_config) | **POST** /configs/{tenantId} | Creates a new config for the specified tenant.
[**config_post_config_deprecated**](ConfigApi.md#config_post_config_deprecated) | **POST** /configs/{tenantId}/{userId} | Creates a new config for the specified tenant and user.
[**config_post_configs**](ConfigApi.md#config_post_configs) | **POST** /configs/{tenantId}/batch | Creates multiple new configs for the specified tenant.
[**config_post_configs_deprecated**](ConfigApi.md#config_post_configs_deprecated) | **POST** /configs/{tenantId}/{userId}/batch | Creates multiple new configs for the specified tenant and user.
[**config_put_config**](ConfigApi.md#config_put_config) | **PUT** /configs/{tenantId}/{configId} | Updates an existing config for the specified tenant.
[**config_put_config_deprecated**](ConfigApi.md#config_put_config_deprecated) | **PUT** /configs/{tenantId}/{userId}/{configId} | Updates an existing config for the specified tenant and user.
[**config_put_config_owner**](ConfigApi.md#config_put_config_owner) | **PUT** /configs/{tenantId}/{configId}/owner | Updates the owner of an existing config.
[**config_upgrade_config**](ConfigApi.md#config_upgrade_config) | **POST** /configs/upgrade/{tenantId}/{targetSimVersion} | Upgrades the config data to the specified target simulation version.
[**config_upgrade_config_deprecated**](ConfigApi.md#config_upgrade_config_deprecated) | **POST** /configs/upgrade/{targetSimVersion} | Upgrades the config data to the specified target simulation version.


# **config_decrypt**
> object config_decrypt(body)

Decrypts the provided data.

This method is marked as obsolete and should be replaced with the /encryption/decrypt endpoint.

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
    body = None # object | A JSON structure containing the data to decrypt.

    try:
        # Decrypts the provided data.
        api_response = api_instance.config_decrypt(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_decrypt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**| A JSON structure containing the data to decrypt. | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_decrypt_with_metadata**
> GetDecryptedDataQueryResult config_decrypt_with_metadata(config_decrypt_with_metadata_request)

Decrypts the provided data.

This method is marked as obsolete and should be replaced with the /encryption/decrypt endpoint.

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
    config_decrypt_with_metadata_request = canopy.openapi.ConfigDecryptWithMetadataRequest() # ConfigDecryptWithMetadataRequest | A structure containing the data to decrypt and a parameter indicating whether the data  should be decrypted recursively. Decrypting recursively means that if the decrypted data  contains further encrypted data, that data will also be decrypted until all data is decrypted.

    try:
        # Decrypts the provided data.
        api_response = api_instance.config_decrypt_with_metadata(config_decrypt_with_metadata_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_decrypt_with_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_decrypt_with_metadata_request** | [**ConfigDecryptWithMetadataRequest**](ConfigDecryptWithMetadataRequest.md)| A structure containing the data to decrypt and a parameter indicating whether the data  should be decrypted recursively. Decrypting recursively means that if the decrypted data  contains further encrypted data, that data will also be decrypted until all data is decrypted. | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_delete_config**
> config_delete_config(tenant_id, config_id, sub_tree_path=sub_tree_path, undelete=undelete)

Deletes an existing config.

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
    tenant_id = 'tenant_id_example' # str | The ID of the tenant that the config belongs to.
config_id = 'config_id_example' # str | The ID of the config to delete.
sub_tree_path = 'sub_tree_path_example' # str | An optional sub-tree path to delete the config under (e.g. `tyres.front`). (optional)
undelete = False # bool | A flag indicating whether to undelete the config instead of deleting it. (optional) (default to False)

    try:
        # Deletes an existing config.
        api_instance.config_delete_config(tenant_id, config_id, sub_tree_path=sub_tree_path, undelete=undelete)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_delete_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant that the config belongs to. | 
 **config_id** | **str**| The ID of the config to delete. | 
 **sub_tree_path** | **str**| An optional sub-tree path to delete the config under (e.g. &#x60;tyres.front&#x60;). | [optional] 
 **undelete** | **bool**| A flag indicating whether to undelete the config instead of deleting it. | [optional] [default to False]

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_delete_config_deprecated**
> config_delete_config_deprecated(tenant_id, user_id, config_id, sub_tree_path=sub_tree_path, undelete=undelete)

Deletes an existing config for the specified tenant and user.

This method is marked as deprecated. The replacement method does not require the `userId` parameter. See M:Canopy.Api.Controllers.Simulations.ConfigController.DeleteConfigAsync(System.String,System.String,System.String,System.Boolean).

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
    tenant_id = 'tenant_id_example' # str | The ID of the tenant that the config belongs to.
user_id = 'user_id_example' # str | The ID of the user that the config belongs to.
config_id = 'config_id_example' # str | The ID of the config to delete.
sub_tree_path = 'sub_tree_path_example' # str | An optional sub-tree path to delete the config under (e.g. `tyres.front`). (optional)
undelete = False # bool | A flag indicating whether to undelete the config instead of deleting it. (optional) (default to False)

    try:
        # Deletes an existing config for the specified tenant and user.
        api_instance.config_delete_config_deprecated(tenant_id, user_id, config_id, sub_tree_path=sub_tree_path, undelete=undelete)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_delete_config_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant that the config belongs to. | 
 **user_id** | **str**| The ID of the user that the config belongs to. | 
 **config_id** | **str**| The ID of the config to delete. | 
 **sub_tree_path** | **str**| An optional sub-tree path to delete the config under (e.g. &#x60;tyres.front&#x60;). | [optional] 
 **undelete** | **bool**| A flag indicating whether to undelete the config instead of deleting it. | [optional] [default to False]

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_encrypt**
> object config_encrypt(body, description=description)

Encrypts the provided data.

This method is marked as obsolete and should be replaced with the /encryption/encrypt endpoint.

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
    body = None # object | The data to encrypt.
description = 'description_example' # str | An optional description of the encrypted data. (optional)

    try:
        # Encrypts the provided data.
        api_response = api_instance.config_encrypt(body, description=description)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_encrypt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**| The data to encrypt. | 
 **description** | **str**| An optional description of the encrypted data. | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_encrypt_with_metadata**
> GetEncryptedDataQueryResult config_encrypt_with_metadata(config_encrypt_with_metadata_request)

Encrypted the provided data using the optional description and channel whitelist.

This method is marked as obsolete and should be replaced with the /encryption/encrypt endpoint.

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
    config_encrypt_with_metadata_request = canopy.openapi.ConfigEncryptWithMetadataRequest() # ConfigEncryptWithMetadataRequest | A structure containing the data to encrypt, the optional description, and the optional channel whitelist.

    try:
        # Encrypted the provided data using the optional description and channel whitelist.
        api_response = api_instance.config_encrypt_with_metadata(config_encrypt_with_metadata_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_encrypt_with_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_encrypt_with_metadata_request** | [**ConfigEncryptWithMetadataRequest**](ConfigEncryptWithMetadataRequest.md)| A structure containing the data to encrypt, the optional description, and the optional channel whitelist. | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_get_config**
> GetConfigQueryResult config_get_config(tenant_id, config_id, sub_tree_path=sub_tree_path, sim_version=sim_version, config_version=config_version)

Gets an existing config.

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
    tenant_id = 'tenant_id_example' # str | The ID of the tenant that the config belongs to.
config_id = 'config_id_example' # str | The ID of the config to get.
sub_tree_path = 'sub_tree_path_example' # str | An optional sub-tree path to get the config under (e.g. `tyres.front`). (optional)
sim_version = 'sim_version_example' # str | An optional simulation version to get the config for. This defaults to the current tenant sim version. (optional)
config_version = 'config_version_example' # str | An optional config version to get the config for. The list of config versions can be found using M:Canopy.Api.Controllers.Simulations.ConfigController.GetConfigVersionsAsync(System.String,System.String,System.String). (optional)

    try:
        # Gets an existing config.
        api_response = api_instance.config_get_config(tenant_id, config_id, sub_tree_path=sub_tree_path, sim_version=sim_version, config_version=config_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_get_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant that the config belongs to. | 
 **config_id** | **str**| The ID of the config to get. | 
 **sub_tree_path** | **str**| An optional sub-tree path to get the config under (e.g. &#x60;tyres.front&#x60;). | [optional] 
 **sim_version** | **str**| An optional simulation version to get the config for. This defaults to the current tenant sim version. | [optional] 
 **config_version** | **str**| An optional config version to get the config for. The list of config versions can be found using M:Canopy.Api.Controllers.Simulations.ConfigController.GetConfigVersionsAsync(System.String,System.String,System.String). | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_get_config_deprecated**
> GetConfigQueryResult config_get_config_deprecated(tenant_id, user_id, config_id, sub_tree_path=sub_tree_path, sim_version=sim_version, config_version=config_version)

Gets an existing config for the specified tenant and user.

This method is marked as deprecated. The replacement method does not require the `userId` parameter. See M:Canopy.Api.Controllers.Simulations.ConfigController.GetConfigAsync(System.String,System.String,System.String,System.String,System.String).

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
    tenant_id = 'tenant_id_example' # str | The ID of the tenant that the config belongs to.
user_id = 'user_id_example' # str | The ID of the user that the config belongs to.
config_id = 'config_id_example' # str | The ID of the config to get.
sub_tree_path = 'sub_tree_path_example' # str | An optional sub-tree path to get the config under (e.g. `tyres.front`). (optional)
sim_version = 'sim_version_example' # str | An optional simulation version to get the config for. (optional)
config_version = 'config_version_example' # str | An optional configuration version to get the config for. (optional)

    try:
        # Gets an existing config for the specified tenant and user.
        api_response = api_instance.config_get_config_deprecated(tenant_id, user_id, config_id, sub_tree_path=sub_tree_path, sim_version=sim_version, config_version=config_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_get_config_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant that the config belongs to. | 
 **user_id** | **str**| The ID of the user that the config belongs to. | 
 **config_id** | **str**| The ID of the config to get. | 
 **sub_tree_path** | **str**| An optional sub-tree path to get the config under (e.g. &#x60;tyres.front&#x60;). | [optional] 
 **sim_version** | **str**| An optional simulation version to get the config for. | [optional] 
 **config_version** | **str**| An optional configuration version to get the config for. | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_get_config_names**
> GetConfigNamesQueryResult config_get_config_names(tenant_id, config_type, result_type=result_type, sub_tree_path=sub_tree_path, sim_version=sim_version)

This method returns a list of config names for the specified config type,  optionally along with the most recent config ID and user ID of each config name.  It also returns the names of the default configs which are part of the specified sim version.

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
    tenant_id = 'tenant_id_example' # str | The ID of the tenant to get config names for.
config_type = 'config_type_example' # str | The type of config to get names for.
result_type = 'result_type_example' # str | The type of result to return. This can be one of the following:  - `name`: names only  - `nameAndId`: names and config IDs  - `matchedNameAndId`: distinct names and config IDs (when multiple configs have the same name, only the most recent config ID is returned)  - `nameAndIdAndOwner`: name and config IDs and owner user IDs  - `matchedNameAndIdAndOwner`: name and config IDs and owner user IDs, distinct by name and user ID (when multiple configs have the same name and user ID, only the most recent config ID is returned). (optional)
sub_tree_path = 'sub_tree_path_example' # str | An optional sub-tree path to retrieve. (optional)
sim_version = 'sim_version_example' # str | An optional simulation version to retrieve default config names for (the current tenant sim version is used if not supplied). (optional)

    try:
        # This method returns a list of config names for the specified config type,  optionally along with the most recent config ID and user ID of each config name.  It also returns the names of the default configs which are part of the specified sim version.
        api_response = api_instance.config_get_config_names(tenant_id, config_type, result_type=result_type, sub_tree_path=sub_tree_path, sim_version=sim_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_get_config_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant to get config names for. | 
 **config_type** | **str**| The type of config to get names for. | 
 **result_type** | **str**| The type of result to return. This can be one of the following:  - &#x60;name&#x60;: names only  - &#x60;nameAndId&#x60;: names and config IDs  - &#x60;matchedNameAndId&#x60;: distinct names and config IDs (when multiple configs have the same name, only the most recent config ID is returned)  - &#x60;nameAndIdAndOwner&#x60;: name and config IDs and owner user IDs  - &#x60;matchedNameAndIdAndOwner&#x60;: name and config IDs and owner user IDs, distinct by name and user ID (when multiple configs have the same name and user ID, only the most recent config ID is returned). | [optional] 
 **sub_tree_path** | **str**| An optional sub-tree path to retrieve. | [optional] 
 **sim_version** | **str**| An optional simulation version to retrieve default config names for (the current tenant sim version is used if not supplied). | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_get_config_sub_paths**
> GetConfigSubPathsQueryResult config_get_config_sub_paths(tenant_id, config_type)

Gets all the unique component paths for the specified tenant and config type.

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
    tenant_id = 'tenant_id_example' # str | The ID of the tenant to get component paths for.
config_type = 'config_type_example' # str | The type of config to get component paths for.

    try:
        # Gets all the unique component paths for the specified tenant and config type.
        api_response = api_instance.config_get_config_sub_paths(tenant_id, config_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_get_config_sub_paths: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant to get component paths for. | 
 **config_type** | **str**| The type of config to get component paths for. | 

### Return type

[**GetConfigSubPathsQueryResult**](GetConfigSubPathsQueryResult.md)

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

# **config_get_config_versions**
> GetConfigVersionsQueryResult config_get_config_versions(tenant_id, config_id, sub_tree_path=sub_tree_path)

Gets the version history of an existing config. Note that we do not keep a complete version history, so  the returned list of versions may not be exhaustive.

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
    tenant_id = 'tenant_id_example' # str | The ID of the tenant that the config belongs to.
config_id = 'config_id_example' # str | The ID of the config to get the versions of.
sub_tree_path = 'sub_tree_path_example' # str | An optional sub-tree path to get the versions of the config under (e.g. `tyres.front`). (optional)

    try:
        # Gets the version history of an existing config. Note that we do not keep a complete version history, so  the returned list of versions may not be exhaustive.
        api_response = api_instance.config_get_config_versions(tenant_id, config_id, sub_tree_path=sub_tree_path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_get_config_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant that the config belongs to. | 
 **config_id** | **str**| The ID of the config to get the versions of. | 
 **sub_tree_path** | **str**| An optional sub-tree path to get the versions of the config under (e.g. &#x60;tyres.front&#x60;). | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_get_config_versions_deprecated**
> GetConfigVersionsQueryResult config_get_config_versions_deprecated(tenant_id, user_id, config_id, sub_tree_path=sub_tree_path)

Gets the versions of an existing config for the specified tenant and user.

This method is marked as deprecated. The replacement method does not require the `userId` parameter. See M:Canopy.Api.Controllers.Simulations.ConfigController.GetConfigVersionsAsync(System.String,System.String,System.String).

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
    tenant_id = 'tenant_id_example' # str | The ID of the tenant that the config belongs to.
user_id = 'user_id_example' # str | The ID of the user that the config belongs to.
config_id = 'config_id_example' # str | The ID of the config to get the versions of.
sub_tree_path = 'sub_tree_path_example' # str | An optional sub-tree path to get the versions of the config under (e.g. `tyres.front`). (optional)

    try:
        # Gets the versions of an existing config for the specified tenant and user.
        api_response = api_instance.config_get_config_versions_deprecated(tenant_id, user_id, config_id, sub_tree_path=sub_tree_path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_get_config_versions_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant that the config belongs to. | 
 **user_id** | **str**| The ID of the user that the config belongs to. | 
 **config_id** | **str**| The ID of the config to get the versions of. | 
 **sub_tree_path** | **str**| An optional sub-tree path to get the versions of the config under (e.g. &#x60;tyres.front&#x60;). | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_get_config_without_user_id_deprecated**
> GetConfigQueryResult config_get_config_without_user_id_deprecated(tenant_id, config_id, sub_tree_path=sub_tree_path, sim_version=sim_version, config_version=config_version)

Gets an existing config for the specified tenant without specifying a user ID.

This method is marked as deprecated. The replacement method does not require the `userId` parameter, or having it set to `auto`. See M:Canopy.Api.Controllers.Simulations.ConfigController.GetConfigAsync(System.String,System.String,System.String,System.String,System.String).

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
    tenant_id = 'tenant_id_example' # str | The ID of the tenant that the config belongs to.
config_id = 'config_id_example' # str | The ID of the config to get.
sub_tree_path = 'sub_tree_path_example' # str | An optional sub-tree path to get the config under (e.g. `tyres.front`). (optional)
sim_version = 'sim_version_example' # str | An optional simulation version to get the config for. (optional)
config_version = 'config_version_example' # str | An optional configuration version to get the config for. (optional)

    try:
        # Gets an existing config for the specified tenant without specifying a user ID.
        api_response = api_instance.config_get_config_without_user_id_deprecated(tenant_id, config_id, sub_tree_path=sub_tree_path, sim_version=sim_version, config_version=config_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_get_config_without_user_id_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant that the config belongs to. | 
 **config_id** | **str**| The ID of the config to get. | 
 **sub_tree_path** | **str**| An optional sub-tree path to get the config under (e.g. &#x60;tyres.front&#x60;). | [optional] 
 **sim_version** | **str**| An optional simulation version to get the config for. | [optional] 
 **config_version** | **str**| An optional configuration version to get the config for. | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_get_configs**
> GetConfigsQueryResult config_get_configs(tenant_id, config_type, filter=filter, sub_tree_path=sub_tree_path, result_type=result_type)

Given the provided filter information, this method returns:  - a list of configs (metadata only)  - a list of custom property groups  ResultType can be used to specify which of the above lists to return.                The list of configs may contain a continuation token of more results are available. The continuation token  can be passed into a subsequent query as part of the filter to retrieve the next page of results.                The list of custom property groups is not guaranteed to be complete. It is a best effort.

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
    tenant_id = 'tenant_id_example' # str | The ID of the tenant to get config data for.
config_type = 'config_type_example' # str | The type of config to get.
filter = 'filter_example' # str | An optional filter to apply to the config data list. (optional)
sub_tree_path = 'sub_tree_path_example' # str | An optional sub-tree path to retrieve. (optional)
result_type = 'result_type_example' # str | An optional result type to return (`all` / `queryOnly` / `groupOnly`). (optional)

    try:
        # Given the provided filter information, this method returns:  - a list of configs (metadata only)  - a list of custom property groups  ResultType can be used to specify which of the above lists to return.                The list of configs may contain a continuation token of more results are available. The continuation token  can be passed into a subsequent query as part of the filter to retrieve the next page of results.                The list of custom property groups is not guaranteed to be complete. It is a best effort.
        api_response = api_instance.config_get_configs(tenant_id, config_type, filter=filter, sub_tree_path=sub_tree_path, result_type=result_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_get_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant to get config data for. | 
 **config_type** | **str**| The type of config to get. | 
 **filter** | **str**| An optional filter to apply to the config data list. | [optional] 
 **sub_tree_path** | **str**| An optional sub-tree path to retrieve. | [optional] 
 **result_type** | **str**| An optional result type to return (&#x60;all&#x60; / &#x60;queryOnly&#x60; / &#x60;groupOnly&#x60;). | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_post_config**
> str config_post_config(tenant_id, config_post_config_request, sub_tree_path=sub_tree_path)

Creates a new config for the specified tenant.

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
    tenant_id = 'tenant_id_example' # str | The ID of the tenant to create the config for.
config_post_config_request = canopy.openapi.ConfigPostConfigRequest() # ConfigPostConfigRequest | The data for the new config.
sub_tree_path = 'sub_tree_path_example' # str | An optional sub-tree path to create the config under (e.g. `tyres.front`). (optional)

    try:
        # Creates a new config for the specified tenant.
        api_response = api_instance.config_post_config(tenant_id, config_post_config_request, sub_tree_path=sub_tree_path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_post_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant to create the config for. | 
 **config_post_config_request** | [**ConfigPostConfigRequest**](ConfigPostConfigRequest.md)| The data for the new config. | 
 **sub_tree_path** | **str**| An optional sub-tree path to create the config under (e.g. &#x60;tyres.front&#x60;). | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_post_config_deprecated**
> str config_post_config_deprecated(tenant_id, user_id, config_post_config_request, sub_tree_path=sub_tree_path)

Creates a new config for the specified tenant and user.

This method is marked as deprecated. The replacement method does not require the `userId` parameter. See M:Canopy.Api.Controllers.Simulations.ConfigController.PostConfigAsync(System.String,Canopy.Api.Controllers.Simulations.NewConfigData,System.String).

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
    tenant_id = 'tenant_id_example' # str | The ID of the tenant to create the config for.
user_id = 'user_id_example' # str | The ID of the user to create the config for.
config_post_config_request = canopy.openapi.ConfigPostConfigRequest() # ConfigPostConfigRequest | The data for the new config.
sub_tree_path = 'sub_tree_path_example' # str | An optional sub-tree path to create the config under (e.g. `tyres.front`). (optional)

    try:
        # Creates a new config for the specified tenant and user.
        api_response = api_instance.config_post_config_deprecated(tenant_id, user_id, config_post_config_request, sub_tree_path=sub_tree_path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_post_config_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant to create the config for. | 
 **user_id** | **str**| The ID of the user to create the config for. | 
 **config_post_config_request** | [**ConfigPostConfigRequest**](ConfigPostConfigRequest.md)| The data for the new config. | 
 **sub_tree_path** | **str**| An optional sub-tree path to create the config under (e.g. &#x60;tyres.front&#x60;). | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_post_configs**
> BatchCreateConfigsResult config_post_configs(tenant_id, config_post_configs_request, sub_tree_path=sub_tree_path)

Creates multiple new configs for the specified tenant.

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
    tenant_id = 'tenant_id_example' # str | The ID of the tenant to create the configs for.
config_post_configs_request = canopy.openapi.ConfigPostConfigsRequest() # ConfigPostConfigsRequest | The data for each new config. Note that you must provide the sim version for each individual config.
sub_tree_path = 'sub_tree_path_example' # str | An optional sub-tree path to create the configs under. (optional)

    try:
        # Creates multiple new configs for the specified tenant.
        api_response = api_instance.config_post_configs(tenant_id, config_post_configs_request, sub_tree_path=sub_tree_path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_post_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant to create the configs for. | 
 **config_post_configs_request** | [**ConfigPostConfigsRequest**](ConfigPostConfigsRequest.md)| The data for each new config. Note that you must provide the sim version for each individual config. | 
 **sub_tree_path** | **str**| An optional sub-tree path to create the configs under. | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_post_configs_deprecated**
> BatchCreateConfigsResult config_post_configs_deprecated(tenant_id, user_id, config_post_configs_request, sub_tree_path=sub_tree_path)

Creates multiple new configs for the specified tenant and user.

This method is marked as deprecated. The replacement method does not require the `userId` parameter. See M:Canopy.Api.Controllers.Simulations.ConfigController.PostConfigsAsync(System.String,Canopy.Api.Controllers.Simulations.NewBatchConfigData,System.String).

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
    tenant_id = 'tenant_id_example' # str | The ID of the tenant to create the configs for.
user_id = 'user_id_example' # str | The ID of the user to create the configs for.
config_post_configs_request = canopy.openapi.ConfigPostConfigsRequest() # ConfigPostConfigsRequest | The data for the new configs.
sub_tree_path = 'sub_tree_path_example' # str | An optional sub-tree path to create the configs under (e.g. `tyres.front`). (optional)

    try:
        # Creates multiple new configs for the specified tenant and user.
        api_response = api_instance.config_post_configs_deprecated(tenant_id, user_id, config_post_configs_request, sub_tree_path=sub_tree_path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_post_configs_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant to create the configs for. | 
 **user_id** | **str**| The ID of the user to create the configs for. | 
 **config_post_configs_request** | [**ConfigPostConfigsRequest**](ConfigPostConfigsRequest.md)| The data for the new configs. | 
 **sub_tree_path** | **str**| An optional sub-tree path to create the configs under (e.g. &#x60;tyres.front&#x60;). | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_put_config**
> config_put_config(tenant_id, config_id, config_put_config_request, sub_tree_path=sub_tree_path)

Updates an existing config for the specified tenant.

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
    tenant_id = 'tenant_id_example' # str | The ID of the tenant that the config belongs to.
config_id = 'config_id_example' # str | The ID of the config to update.
config_put_config_request = canopy.openapi.ConfigPutConfigRequest() # ConfigPutConfigRequest | The updated data for the config.
sub_tree_path = 'sub_tree_path_example' # str | An optional sub-tree path to update the config under (e.g. `tyres.front`). (optional)

    try:
        # Updates an existing config for the specified tenant.
        api_instance.config_put_config(tenant_id, config_id, config_put_config_request, sub_tree_path=sub_tree_path)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_put_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant that the config belongs to. | 
 **config_id** | **str**| The ID of the config to update. | 
 **config_put_config_request** | [**ConfigPutConfigRequest**](ConfigPutConfigRequest.md)| The updated data for the config. | 
 **sub_tree_path** | **str**| An optional sub-tree path to update the config under (e.g. &#x60;tyres.front&#x60;). | [optional] 

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

# **config_put_config_deprecated**
> config_put_config_deprecated(tenant_id, user_id, config_id, config_put_config_request, sub_tree_path=sub_tree_path)

Updates an existing config for the specified tenant and user.

This method is marked as deprecated. The replacement method does not require the `userId` parameter. See M:Canopy.Api.Controllers.Simulations.ConfigController.PutConfigAsync(System.String,System.String,Canopy.Api.Controllers.Simulations.UpdatedConfigData,System.String).

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
    tenant_id = 'tenant_id_example' # str | The ID of the tenant that the config belongs to.
user_id = 'user_id_example' # str | The ID of the user that the config belongs to.
config_id = 'config_id_example' # str | The ID of the config to update.
config_put_config_request = canopy.openapi.ConfigPutConfigRequest() # ConfigPutConfigRequest | The updated data for the config.
sub_tree_path = 'sub_tree_path_example' # str | An optional sub-tree path to update the config under (e.g. `tyres.front`). (optional)

    try:
        # Updates an existing config for the specified tenant and user.
        api_instance.config_put_config_deprecated(tenant_id, user_id, config_id, config_put_config_request, sub_tree_path=sub_tree_path)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_put_config_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant that the config belongs to. | 
 **user_id** | **str**| The ID of the user that the config belongs to. | 
 **config_id** | **str**| The ID of the config to update. | 
 **config_put_config_request** | [**ConfigPutConfigRequest**](ConfigPutConfigRequest.md)| The updated data for the config. | 
 **sub_tree_path** | **str**| An optional sub-tree path to update the config under (e.g. &#x60;tyres.front&#x60;). | [optional] 

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

# **config_put_config_owner**
> config_put_config_owner(tenant_id, config_id, config_put_config_owner_request)

Updates the owner of an existing config.

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
    tenant_id = 'tenant_id_example' # str | The ID of the tenant that the config belongs to.
config_id = 'config_id_example' # str | The ID of the config to update the owner of.
config_put_config_owner_request = canopy.openapi.ConfigPutConfigOwnerRequest() # ConfigPutConfigOwnerRequest | The updated owner data for the config.

    try:
        # Updates the owner of an existing config.
        api_instance.config_put_config_owner(tenant_id, config_id, config_put_config_owner_request)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_put_config_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The ID of the tenant that the config belongs to. | 
 **config_id** | **str**| The ID of the config to update the owner of. | 
 **config_put_config_owner_request** | [**ConfigPutConfigOwnerRequest**](ConfigPutConfigOwnerRequest.md)| The updated owner data for the config. | 

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

# **config_upgrade_config**
> UpgradeConfigQueryResult config_upgrade_config(tenant_id, target_sim_version, config_upgrade_config_deprecated_request, sub_tree_path=sub_tree_path)

Upgrades the config data to the specified target simulation version.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID whose schema will be used to upgrade the data.
target_sim_version = 'target_sim_version_example' # str | The target simulation version to upgrade to.
config_upgrade_config_deprecated_request = canopy.openapi.ConfigUpgradeConfigDeprecatedRequest() # ConfigUpgradeConfigDeprecatedRequest | The config data to upgrade.
sub_tree_path = 'sub_tree_path_example' # str | An optional sub-tree path, if the data is a sub-component of a config. (optional)

    try:
        # Upgrades the config data to the specified target simulation version.
        api_response = api_instance.config_upgrade_config(tenant_id, target_sim_version, config_upgrade_config_deprecated_request, sub_tree_path=sub_tree_path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_upgrade_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID whose schema will be used to upgrade the data. | 
 **target_sim_version** | **str**| The target simulation version to upgrade to. | 
 **config_upgrade_config_deprecated_request** | [**ConfigUpgradeConfigDeprecatedRequest**](ConfigUpgradeConfigDeprecatedRequest.md)| The config data to upgrade. | 
 **sub_tree_path** | **str**| An optional sub-tree path, if the data is a sub-component of a config. | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_upgrade_config_deprecated**
> UpgradeConfigQueryResult config_upgrade_config_deprecated(target_sim_version, config_upgrade_config_deprecated_request, sub_tree_path=sub_tree_path)

Upgrades the config data to the specified target simulation version.

This method is marked as obsolete and should be replaced with the /simulations/config/upgrade endpoint.

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
    target_sim_version = 'target_sim_version_example' # str | The target simulation version to upgrade to.
config_upgrade_config_deprecated_request = canopy.openapi.ConfigUpgradeConfigDeprecatedRequest() # ConfigUpgradeConfigDeprecatedRequest | The config data to upgrade.
sub_tree_path = 'sub_tree_path_example' # str | An optional sub-tree path, if the data is a sub-component of a config. (optional)

    try:
        # Upgrades the config data to the specified target simulation version.
        api_response = api_instance.config_upgrade_config_deprecated(target_sim_version, config_upgrade_config_deprecated_request, sub_tree_path=sub_tree_path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigApi->config_upgrade_config_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_sim_version** | **str**| The target simulation version to upgrade to. | 
 **config_upgrade_config_deprecated_request** | [**ConfigUpgradeConfigDeprecatedRequest**](ConfigUpgradeConfigDeprecatedRequest.md)| The config data to upgrade. | 
 **sub_tree_path** | **str**| An optional sub-tree path, if the data is a sub-component of a config. | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

