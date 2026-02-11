# canopy.openapi.EncryptionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**encryption_decrypt**](EncryptionApi.md#encryption_decrypt) | **POST** /encryption/decrypt | Decrypts the specified data.
[**encryption_delete_config_permission**](EncryptionApi.md#encryption_delete_config_permission) | **DELETE** /encryption/config-permissions/{tenantId}/{encryptingTenantShortName}/{decryptingTenantShortName} | Deletes an encryption key permission for the specified tenant.  Config permissions represent which encryption keys are allowed to be used by which tenants to re-encrypt any encrypted configs you provide.
[**encryption_delete_key_permission**](EncryptionApi.md#encryption_delete_key_permission) | **DELETE** /encryption/key-permissions/{tenantId}/{encryptingTenantShortName} | Deletes an encryption key permission for the specified tenant.  Key permissions represent which tenants are allowed to use your tenant&#39;s encryption key.
[**encryption_encrypt**](EncryptionApi.md#encryption_encrypt) | **POST** /encryption/encrypt | Encrypts the specified data.
[**encryption_get_config_permissions**](EncryptionApi.md#encryption_get_config_permissions) | **GET** /encryption/config-permissions/{tenantId} | Get the list of encryption config permissions for the specified tenant.  Config permissions represent which encryption keys are allowed to be used by which tenants to re-encrypt any encrypted configs you provide.
[**encryption_get_key_permissions**](EncryptionApi.md#encryption_get_key_permissions) | **GET** /encryption/key-permissions/{tenantId} | Get the list of encryption key permissions for the specified tenant.  Key permissions represent which tenants are allowed to use your tenant&#39;s encryption key.
[**encryption_put_config_permission**](EncryptionApi.md#encryption_put_config_permission) | **PUT** /encryption/config-permissions/{tenantId}/{encryptingTenantShortName}/{decryptingTenantShortName} | Adds or replaces an encryption config permission for the specified tenant.  Config permissions represent which encryption keys are allowed to be used by which tenants to re-encrypt any encrypted configs you provide.
[**encryption_put_key_permission**](EncryptionApi.md#encryption_put_key_permission) | **PUT** /encryption/key-permissions/{tenantId}/{encryptingTenantShortName} | Adds or replaces an encryption key permission for the specified tenant.  Key permissions represent which tenants are allowed to use your tenant&#39;s encryption key.
[**encryption_query**](EncryptionApi.md#encryption_query) | **POST** /encryption/query/{tenantId} | Queries the supplied data to determine what encryption keys can be used to re-encrypt it.  Internally, the API will find all encrypted components in the car (including recursively encrypted ones) and note the tenant IDs which encrypted them.   - For each of those encrypting tenant IDs it will search their permission lists to find any decrypting tenant IDs who have been granted permission by the encrypting tenant for their keys to be used by the config owner tenant.   - For each decrypting tenant ID it will also search their permission list to ensure permission has also been granted by the decrypting tenant for their key to be used by the config owner.
[**encryption_re_encrypt**](EncryptionApi.md#encryption_re_encrypt) | **POST** /encryption/re-encrypt/{tenantId} | Re-encrypts the specified data.  The data structure will be searched for encrypted nodes, and any found will be re-encrypted  using the encryption key for the tenant / sim version combination specified in the request body.  If either the decrypting tenant doesn&#39;t exist, or if the tenant ID parameter does not have the required permissions to use that encryption key,  then the method will fail as a bad request.


# **encryption_decrypt**
> GetDecryptedDataQueryResult encryption_decrypt(config_decrypt_with_metadata_request)

Decrypts the specified data.

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
    api_instance = canopy.openapi.EncryptionApi(api_client)
    config_decrypt_with_metadata_request = canopy.openapi.ConfigDecryptWithMetadataRequest() # ConfigDecryptWithMetadataRequest | The data to decrypt.

    try:
        # Decrypts the specified data.
        api_response = api_instance.encryption_decrypt(config_decrypt_with_metadata_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EncryptionApi->encryption_decrypt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_decrypt_with_metadata_request** | [**ConfigDecryptWithMetadataRequest**](ConfigDecryptWithMetadataRequest.md)| The data to decrypt. | 

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

# **encryption_delete_config_permission**
> encryption_delete_config_permission(tenant_id, encrypting_tenant_short_name, decrypting_tenant_short_name)

Deletes an encryption key permission for the specified tenant.  Config permissions represent which encryption keys are allowed to be used by which tenants to re-encrypt any encrypted configs you provide.

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
    api_instance = canopy.openapi.EncryptionApi(api_client)
    tenant_id = 'tenant_id_example' # str | The tenant to make the request for. This is usually the logged in user's tenant ID.
encrypting_tenant_short_name = 'encrypting_tenant_short_name_example' # str | The short name of the tenant who will use the encryption key for re-encrypting your configs.
decrypting_tenant_short_name = 'decrypting_tenant_short_name_example' # str | The short name of the tenant who owns the decryption key.

    try:
        # Deletes an encryption key permission for the specified tenant.  Config permissions represent which encryption keys are allowed to be used by which tenants to re-encrypt any encrypted configs you provide.
        api_instance.encryption_delete_config_permission(tenant_id, encrypting_tenant_short_name, decrypting_tenant_short_name)
    except ApiException as e:
        print("Exception when calling EncryptionApi->encryption_delete_config_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant to make the request for. This is usually the logged in user&#39;s tenant ID. | 
 **encrypting_tenant_short_name** | **str**| The short name of the tenant who will use the encryption key for re-encrypting your configs. | 
 **decrypting_tenant_short_name** | **str**| The short name of the tenant who owns the decryption key. | 

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

# **encryption_delete_key_permission**
> encryption_delete_key_permission(tenant_id, encrypting_tenant_short_name)

Deletes an encryption key permission for the specified tenant.  Key permissions represent which tenants are allowed to use your tenant's encryption key.

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
    api_instance = canopy.openapi.EncryptionApi(api_client)
    tenant_id = 'tenant_id_example' # str | The tenant to make the request for. This is usually the logged in user's tenant ID.
encrypting_tenant_short_name = 'encrypting_tenant_short_name_example' # str | The tenant short name whose permission should be deleted.

    try:
        # Deletes an encryption key permission for the specified tenant.  Key permissions represent which tenants are allowed to use your tenant's encryption key.
        api_instance.encryption_delete_key_permission(tenant_id, encrypting_tenant_short_name)
    except ApiException as e:
        print("Exception when calling EncryptionApi->encryption_delete_key_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant to make the request for. This is usually the logged in user&#39;s tenant ID. | 
 **encrypting_tenant_short_name** | **str**| The tenant short name whose permission should be deleted. | 

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

# **encryption_encrypt**
> GetEncryptedDataQueryResult encryption_encrypt(config_encrypt_with_metadata_request)

Encrypts the specified data.

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
    api_instance = canopy.openapi.EncryptionApi(api_client)
    config_encrypt_with_metadata_request = canopy.openapi.ConfigEncryptWithMetadataRequest() # ConfigEncryptWithMetadataRequest | The data to encrypt and other options.

    try:
        # Encrypts the specified data.
        api_response = api_instance.encryption_encrypt(config_encrypt_with_metadata_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EncryptionApi->encryption_encrypt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_encrypt_with_metadata_request** | [**ConfigEncryptWithMetadataRequest**](ConfigEncryptWithMetadataRequest.md)| The data to encrypt and other options. | 

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

# **encryption_get_config_permissions**
> GetConfigPermissionsQueryResult encryption_get_config_permissions(tenant_id)

Get the list of encryption config permissions for the specified tenant.  Config permissions represent which encryption keys are allowed to be used by which tenants to re-encrypt any encrypted configs you provide.

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
    api_instance = canopy.openapi.EncryptionApi(api_client)
    tenant_id = 'tenant_id_example' # str | The tenant to make the request for. This is usually the logged in user's tenant ID.

    try:
        # Get the list of encryption config permissions for the specified tenant.  Config permissions represent which encryption keys are allowed to be used by which tenants to re-encrypt any encrypted configs you provide.
        api_response = api_instance.encryption_get_config_permissions(tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EncryptionApi->encryption_get_config_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant to make the request for. This is usually the logged in user&#39;s tenant ID. | 

### Return type

[**GetConfigPermissionsQueryResult**](GetConfigPermissionsQueryResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **encryption_get_key_permissions**
> GetKeyPermissionsQueryResult encryption_get_key_permissions(tenant_id)

Get the list of encryption key permissions for the specified tenant.  Key permissions represent which tenants are allowed to use your tenant's encryption key.

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
    api_instance = canopy.openapi.EncryptionApi(api_client)
    tenant_id = 'tenant_id_example' # str | The tenant to make the request for. This is usually the logged in user's tenant ID.

    try:
        # Get the list of encryption key permissions for the specified tenant.  Key permissions represent which tenants are allowed to use your tenant's encryption key.
        api_response = api_instance.encryption_get_key_permissions(tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EncryptionApi->encryption_get_key_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant to make the request for. This is usually the logged in user&#39;s tenant ID. | 

### Return type

[**GetKeyPermissionsQueryResult**](GetKeyPermissionsQueryResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **encryption_put_config_permission**
> encryption_put_config_permission(tenant_id, encrypting_tenant_short_name, decrypting_tenant_short_name, encryption_put_config_permission_request)

Adds or replaces an encryption config permission for the specified tenant.  Config permissions represent which encryption keys are allowed to be used by which tenants to re-encrypt any encrypted configs you provide.

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
    api_instance = canopy.openapi.EncryptionApi(api_client)
    tenant_id = 'tenant_id_example' # str | The tenant to make the request for. This is usually the logged in user's tenant ID.
encrypting_tenant_short_name = 'encrypting_tenant_short_name_example' # str | The short name of the tenant who will use the encryption key for re-encrypting your configs.
decrypting_tenant_short_name = 'decrypting_tenant_short_name_example' # str | The short name of the tenant who owns the decryption key.
encryption_put_config_permission_request = canopy.openapi.EncryptionPutConfigPermissionRequest() # EncryptionPutConfigPermissionRequest | A data structure containing the minimum sim version from which the permission takes effect, and a description of the permission.

    try:
        # Adds or replaces an encryption config permission for the specified tenant.  Config permissions represent which encryption keys are allowed to be used by which tenants to re-encrypt any encrypted configs you provide.
        api_instance.encryption_put_config_permission(tenant_id, encrypting_tenant_short_name, decrypting_tenant_short_name, encryption_put_config_permission_request)
    except ApiException as e:
        print("Exception when calling EncryptionApi->encryption_put_config_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant to make the request for. This is usually the logged in user&#39;s tenant ID. | 
 **encrypting_tenant_short_name** | **str**| The short name of the tenant who will use the encryption key for re-encrypting your configs. | 
 **decrypting_tenant_short_name** | **str**| The short name of the tenant who owns the decryption key. | 
 **encryption_put_config_permission_request** | [**EncryptionPutConfigPermissionRequest**](EncryptionPutConfigPermissionRequest.md)| A data structure containing the minimum sim version from which the permission takes effect, and a description of the permission. | 

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

# **encryption_put_key_permission**
> encryption_put_key_permission(tenant_id, encrypting_tenant_short_name, encryption_put_key_permission_request)

Adds or replaces an encryption key permission for the specified tenant.  Key permissions represent which tenants are allowed to use your tenant's encryption key.

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
    api_instance = canopy.openapi.EncryptionApi(api_client)
    tenant_id = 'tenant_id_example' # str | The tenant to make the request for. This is usually the logged in user's tenant ID.
encrypting_tenant_short_name = 'encrypting_tenant_short_name_example' # str | The short name of the tenant who will use the encryption key for encrypting.
encryption_put_key_permission_request = canopy.openapi.EncryptionPutKeyPermissionRequest() # EncryptionPutKeyPermissionRequest | A data structure containing the minimum sim version from which the permission takes effect, and a description of the permission.

    try:
        # Adds or replaces an encryption key permission for the specified tenant.  Key permissions represent which tenants are allowed to use your tenant's encryption key.
        api_instance.encryption_put_key_permission(tenant_id, encrypting_tenant_short_name, encryption_put_key_permission_request)
    except ApiException as e:
        print("Exception when calling EncryptionApi->encryption_put_key_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant to make the request for. This is usually the logged in user&#39;s tenant ID. | 
 **encrypting_tenant_short_name** | **str**| The short name of the tenant who will use the encryption key for encrypting. | 
 **encryption_put_key_permission_request** | [**EncryptionPutKeyPermissionRequest**](EncryptionPutKeyPermissionRequest.md)| A data structure containing the minimum sim version from which the permission takes effect, and a description of the permission. | 

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

# **encryption_query**
> QueryEncryptedDataQueryResult encryption_query(tenant_id, encryption_query_request)

Queries the supplied data to determine what encryption keys can be used to re-encrypt it.  Internally, the API will find all encrypted components in the car (including recursively encrypted ones) and note the tenant IDs which encrypted them.   - For each of those encrypting tenant IDs it will search their permission lists to find any decrypting tenant IDs who have been granted permission by the encrypting tenant for their keys to be used by the config owner tenant.   - For each decrypting tenant ID it will also search their permission list to ensure permission has also been granted by the decrypting tenant for their key to be used by the config owner.

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
    api_instance = canopy.openapi.EncryptionApi(api_client)
    tenant_id = 'tenant_id_example' # str | The tenant to make the request for (the config owner). This is usually the logged in user's tenant ID.
encryption_query_request = canopy.openapi.EncryptionQueryRequest() # EncryptionQueryRequest | A data structure containing the data to be queried and the sim version of that data.

    try:
        # Queries the supplied data to determine what encryption keys can be used to re-encrypt it.  Internally, the API will find all encrypted components in the car (including recursively encrypted ones) and note the tenant IDs which encrypted them.   - For each of those encrypting tenant IDs it will search their permission lists to find any decrypting tenant IDs who have been granted permission by the encrypting tenant for their keys to be used by the config owner tenant.   - For each decrypting tenant ID it will also search their permission list to ensure permission has also been granted by the decrypting tenant for their key to be used by the config owner.
        api_response = api_instance.encryption_query(tenant_id, encryption_query_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EncryptionApi->encryption_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant to make the request for (the config owner). This is usually the logged in user&#39;s tenant ID. | 
 **encryption_query_request** | [**EncryptionQueryRequest**](EncryptionQueryRequest.md)| A data structure containing the data to be queried and the sim version of that data. | 

### Return type

[**QueryEncryptedDataQueryResult**](QueryEncryptedDataQueryResult.md)

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

# **encryption_re_encrypt**
> GetReEncryptedDataQueryResult encryption_re_encrypt(tenant_id, encryption_re_encrypt_request)

Re-encrypts the specified data.  The data structure will be searched for encrypted nodes, and any found will be re-encrypted  using the encryption key for the tenant / sim version combination specified in the request body.  If either the decrypting tenant doesn't exist, or if the tenant ID parameter does not have the required permissions to use that encryption key,  then the method will fail as a bad request.

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
    api_instance = canopy.openapi.EncryptionApi(api_client)
    tenant_id = 'tenant_id_example' # str | The tenant to make the request for. This is usually the logged in user's tenant ID.
encryption_re_encrypt_request = canopy.openapi.EncryptionReEncryptRequest() # EncryptionReEncryptRequest | A data structure containing the data to re-encrypt, the data's sim version, and the tenant short name. The sim version and tenant short name determine which encryption key will be used.

    try:
        # Re-encrypts the specified data.  The data structure will be searched for encrypted nodes, and any found will be re-encrypted  using the encryption key for the tenant / sim version combination specified in the request body.  If either the decrypting tenant doesn't exist, or if the tenant ID parameter does not have the required permissions to use that encryption key,  then the method will fail as a bad request.
        api_response = api_instance.encryption_re_encrypt(tenant_id, encryption_re_encrypt_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EncryptionApi->encryption_re_encrypt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant to make the request for. This is usually the logged in user&#39;s tenant ID. | 
 **encryption_re_encrypt_request** | [**EncryptionReEncryptRequest**](EncryptionReEncryptRequest.md)| A data structure containing the data to re-encrypt, the data&#39;s sim version, and the tenant short name. The sim version and tenant short name determine which encryption key will be used. | 

### Return type

[**GetReEncryptedDataQueryResult**](GetReEncryptedDataQueryResult.md)

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

