# canopy.swagger.ConfigApi

All URIs are relative to *https://localhost:44300*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config_decrypt**](ConfigApi.md#config_decrypt) | **POST** /configs/decrypt | 
[**config_delete_config**](ConfigApi.md#config_delete_config) | **DELETE** /configs/{tenantId}/{configId} | 
[**config_delete_config_deprecated**](ConfigApi.md#config_delete_config_deprecated) | **DELETE** /configs/{tenantId}/{userId}/{configId} | 
[**config_encrypt**](ConfigApi.md#config_encrypt) | **POST** /configs/encrypt | 
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
> object config_decrypt(data)



### Example
```python
from __future__ import print_function
import time
import canopy.swagger
from canopy.swagger.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = canopy.swagger.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = canopy.swagger.ConfigApi(canopy.swagger.ApiClient(configuration))
data = NULL # object | 

try:
    api_response = api_instance.config_decrypt(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->config_decrypt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **object**|  | 

### Return type

**object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_delete_config**
> config_delete_config(tenant_id, config_id, sub_tree_path=sub_tree_path, undelete=undelete)



### Example
```python
from __future__ import print_function
import time
import canopy.swagger
from canopy.swagger.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = canopy.swagger.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = canopy.swagger.ConfigApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
config_id = 'config_id_example' # str | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)
undelete = true # bool |  (optional)

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
 **undelete** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_delete_config_deprecated**
> config_delete_config_deprecated(tenant_id, user_id, config_id, sub_tree_path=sub_tree_path, undelete=undelete)



### Example
```python
from __future__ import print_function
import time
import canopy.swagger
from canopy.swagger.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = canopy.swagger.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = canopy.swagger.ConfigApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
config_id = 'config_id_example' # str | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)
undelete = true # bool |  (optional)

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
 **undelete** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_encrypt**
> object config_encrypt(data, description=description)



### Example
```python
from __future__ import print_function
import time
import canopy.swagger
from canopy.swagger.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = canopy.swagger.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = canopy.swagger.ConfigApi(canopy.swagger.ApiClient(configuration))
data = NULL # object | 
description = 'description_example' # str |  (optional)

try:
    api_response = api_instance.config_encrypt(data, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->config_encrypt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **object**|  | 
 **description** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_get_config**
> GetConfigQueryResult config_get_config(tenant_id, config_id, sub_tree_path=sub_tree_path, sim_version=sim_version, config_version=config_version)



### Example
```python
from __future__ import print_function
import time
import canopy.swagger
from canopy.swagger.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = canopy.swagger.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = canopy.swagger.ConfigApi(canopy.swagger.ApiClient(configuration))
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

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_get_config_deprecated**
> GetConfigQueryResult config_get_config_deprecated(tenant_id, user_id, config_id, sub_tree_path=sub_tree_path, sim_version=sim_version, config_version=config_version)



### Example
```python
from __future__ import print_function
import time
import canopy.swagger
from canopy.swagger.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = canopy.swagger.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = canopy.swagger.ConfigApi(canopy.swagger.ApiClient(configuration))
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

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_get_config_names**
> GetConfigNamesQueryResult config_get_config_names(tenant_id, config_type, result_type, sub_tree_path=sub_tree_path, sim_version=sim_version)



### Example
```python
from __future__ import print_function
import time
import canopy.swagger
from canopy.swagger.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = canopy.swagger.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = canopy.swagger.ConfigApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
config_type = 'config_type_example' # str | 
result_type = 'result_type_example' # str | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)
sim_version = 'sim_version_example' # str |  (optional)

try:
    api_response = api_instance.config_get_config_names(tenant_id, config_type, result_type, sub_tree_path=sub_tree_path, sim_version=sim_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->config_get_config_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **config_type** | **str**|  | 
 **result_type** | **str**|  | 
 **sub_tree_path** | **str**|  | [optional] 
 **sim_version** | **str**|  | [optional] 

### Return type

[**GetConfigNamesQueryResult**](GetConfigNamesQueryResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_get_config_versions**
> GetConfigVersionsQueryResult config_get_config_versions(tenant_id, config_id, sub_tree_path=sub_tree_path)



### Example
```python
from __future__ import print_function
import time
import canopy.swagger
from canopy.swagger.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = canopy.swagger.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = canopy.swagger.ConfigApi(canopy.swagger.ApiClient(configuration))
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

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_get_config_versions_deprecated**
> GetConfigVersionsQueryResult config_get_config_versions_deprecated(tenant_id, user_id, config_id, sub_tree_path=sub_tree_path)



### Example
```python
from __future__ import print_function
import time
import canopy.swagger
from canopy.swagger.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = canopy.swagger.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = canopy.swagger.ConfigApi(canopy.swagger.ApiClient(configuration))
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

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_get_config_without_user_id_deprecated**
> GetConfigQueryResult config_get_config_without_user_id_deprecated(tenant_id, config_id, sub_tree_path=sub_tree_path, sim_version=sim_version, config_version=config_version)



### Example
```python
from __future__ import print_function
import time
import canopy.swagger
from canopy.swagger.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = canopy.swagger.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = canopy.swagger.ConfigApi(canopy.swagger.ApiClient(configuration))
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

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_get_configs**
> GetConfigsQueryResult config_get_configs(tenant_id, config_type, filter=filter, sub_tree_path=sub_tree_path, result_type=result_type)



### Example
```python
from __future__ import print_function
import time
import canopy.swagger
from canopy.swagger.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = canopy.swagger.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = canopy.swagger.ConfigApi(canopy.swagger.ApiClient(configuration))
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

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_post_config**
> str config_post_config(tenant_id, data, sub_tree_path=sub_tree_path)



### Example
```python
from __future__ import print_function
import time
import canopy.swagger
from canopy.swagger.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = canopy.swagger.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = canopy.swagger.ConfigApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
data = canopy.swagger.NewConfigData() # NewConfigData | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)

try:
    api_response = api_instance.config_post_config(tenant_id, data, sub_tree_path=sub_tree_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->config_post_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **data** | [**NewConfigData**](NewConfigData.md)|  | 
 **sub_tree_path** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_post_config_deprecated**
> str config_post_config_deprecated(tenant_id, user_id, data, sub_tree_path=sub_tree_path)



### Example
```python
from __future__ import print_function
import time
import canopy.swagger
from canopy.swagger.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = canopy.swagger.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = canopy.swagger.ConfigApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
data = canopy.swagger.NewConfigData() # NewConfigData | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)

try:
    api_response = api_instance.config_post_config_deprecated(tenant_id, user_id, data, sub_tree_path=sub_tree_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->config_post_config_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **data** | [**NewConfigData**](NewConfigData.md)|  | 
 **sub_tree_path** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_post_configs**
> BatchCreateConfigsResult config_post_configs(tenant_id, data, sub_tree_path=sub_tree_path)



### Example
```python
from __future__ import print_function
import time
import canopy.swagger
from canopy.swagger.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = canopy.swagger.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = canopy.swagger.ConfigApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
data = canopy.swagger.NewBatchConfigData() # NewBatchConfigData | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)

try:
    api_response = api_instance.config_post_configs(tenant_id, data, sub_tree_path=sub_tree_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->config_post_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **data** | [**NewBatchConfigData**](NewBatchConfigData.md)|  | 
 **sub_tree_path** | **str**|  | [optional] 

### Return type

[**BatchCreateConfigsResult**](BatchCreateConfigsResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_post_configs_deprecated**
> BatchCreateConfigsResult config_post_configs_deprecated(tenant_id, user_id, data, sub_tree_path=sub_tree_path)



### Example
```python
from __future__ import print_function
import time
import canopy.swagger
from canopy.swagger.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = canopy.swagger.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = canopy.swagger.ConfigApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
data = canopy.swagger.NewBatchConfigData() # NewBatchConfigData | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)

try:
    api_response = api_instance.config_post_configs_deprecated(tenant_id, user_id, data, sub_tree_path=sub_tree_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->config_post_configs_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **data** | [**NewBatchConfigData**](NewBatchConfigData.md)|  | 
 **sub_tree_path** | **str**|  | [optional] 

### Return type

[**BatchCreateConfigsResult**](BatchCreateConfigsResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_put_config**
> config_put_config(tenant_id, config_id, data, sub_tree_path=sub_tree_path)



### Example
```python
from __future__ import print_function
import time
import canopy.swagger
from canopy.swagger.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = canopy.swagger.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = canopy.swagger.ConfigApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
config_id = 'config_id_example' # str | 
data = canopy.swagger.UpdatedConfigData() # UpdatedConfigData | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)

try:
    api_instance.config_put_config(tenant_id, config_id, data, sub_tree_path=sub_tree_path)
except ApiException as e:
    print("Exception when calling ConfigApi->config_put_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **config_id** | **str**|  | 
 **data** | [**UpdatedConfigData**](UpdatedConfigData.md)|  | 
 **sub_tree_path** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_put_config_deprecated**
> config_put_config_deprecated(tenant_id, user_id, config_id, data, sub_tree_path=sub_tree_path)



### Example
```python
from __future__ import print_function
import time
import canopy.swagger
from canopy.swagger.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = canopy.swagger.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = canopy.swagger.ConfigApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
config_id = 'config_id_example' # str | 
data = canopy.swagger.UpdatedConfigData() # UpdatedConfigData | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)

try:
    api_instance.config_put_config_deprecated(tenant_id, user_id, config_id, data, sub_tree_path=sub_tree_path)
except ApiException as e:
    print("Exception when calling ConfigApi->config_put_config_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **config_id** | **str**|  | 
 **data** | [**UpdatedConfigData**](UpdatedConfigData.md)|  | 
 **sub_tree_path** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_put_config_owner**
> config_put_config_owner(tenant_id, config_id, owner_data)



### Example
```python
from __future__ import print_function
import time
import canopy.swagger
from canopy.swagger.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = canopy.swagger.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = canopy.swagger.ConfigApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
config_id = 'config_id_example' # str | 
owner_data = canopy.swagger.ConfigOwnerData() # ConfigOwnerData | 

try:
    api_instance.config_put_config_owner(tenant_id, config_id, owner_data)
except ApiException as e:
    print("Exception when calling ConfigApi->config_put_config_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **config_id** | **str**|  | 
 **owner_data** | [**ConfigOwnerData**](ConfigOwnerData.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_upgrade_config**
> UpgradeConfigQueryResult config_upgrade_config(tenant_id, target_sim_version, data, sub_tree_path=sub_tree_path)



### Example
```python
from __future__ import print_function
import time
import canopy.swagger
from canopy.swagger.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = canopy.swagger.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = canopy.swagger.ConfigApi(canopy.swagger.ApiClient(configuration))
tenant_id = 'tenant_id_example' # str | 
target_sim_version = 'target_sim_version_example' # str | 
data = canopy.swagger.UpgradeConfigData() # UpgradeConfigData | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)

try:
    api_response = api_instance.config_upgrade_config(tenant_id, target_sim_version, data, sub_tree_path=sub_tree_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->config_upgrade_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **target_sim_version** | **str**|  | 
 **data** | [**UpgradeConfigData**](UpgradeConfigData.md)|  | 
 **sub_tree_path** | **str**|  | [optional] 

### Return type

[**UpgradeConfigQueryResult**](UpgradeConfigQueryResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_upgrade_config_deprecated**
> UpgradeConfigQueryResult config_upgrade_config_deprecated(target_sim_version, data, sub_tree_path=sub_tree_path)



### Example
```python
from __future__ import print_function
import time
import canopy.swagger
from canopy.swagger.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = canopy.swagger.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = canopy.swagger.ConfigApi(canopy.swagger.ApiClient(configuration))
target_sim_version = 'target_sim_version_example' # str | 
data = canopy.swagger.UpgradeConfigData() # UpgradeConfigData | 
sub_tree_path = 'sub_tree_path_example' # str |  (optional)

try:
    api_response = api_instance.config_upgrade_config_deprecated(target_sim_version, data, sub_tree_path=sub_tree_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->config_upgrade_config_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_sim_version** | **str**|  | 
 **data** | [**UpgradeConfigData**](UpgradeConfigData.md)|  | 
 **sub_tree_path** | **str**|  | [optional] 

### Return type

[**UpgradeConfigQueryResult**](UpgradeConfigQueryResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

