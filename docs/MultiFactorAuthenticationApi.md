# canopy.openapi.MultiFactorAuthenticationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**multi_factor_authentication_get_multi_factor_authentication_code**](MultiFactorAuthenticationApi.md#multi_factor_authentication_get_multi_factor_authentication_code) | **GET** /mfa/{tenantId}/{userId} | 
[**multi_factor_authentication_post_multi_factor_authentication**](MultiFactorAuthenticationApi.md#multi_factor_authentication_post_multi_factor_authentication) | **POST** /mfa/{tenantId}/{userId} | 


# **multi_factor_authentication_get_multi_factor_authentication_code**
> GenerateMfaSetupCodeResult multi_factor_authentication_get_multi_factor_authentication_code(tenant_id, user_id)



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
    api_instance = canopy.openapi.MultiFactorAuthenticationApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 

    try:
        api_response = api_instance.multi_factor_authentication_get_multi_factor_authentication_code(tenant_id, user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MultiFactorAuthenticationApi->multi_factor_authentication_get_multi_factor_authentication_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**GenerateMfaSetupCodeResult**](GenerateMfaSetupCodeResult.md)

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

# **multi_factor_authentication_post_multi_factor_authentication**
> multi_factor_authentication_post_multi_factor_authentication(tenant_id, user_id, multi_factor_authentication_post_multi_factor_authentication_request)



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
    api_instance = canopy.openapi.MultiFactorAuthenticationApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
multi_factor_authentication_post_multi_factor_authentication_request = canopy.openapi.MultiFactorAuthenticationPostMultiFactorAuthenticationRequest() # MultiFactorAuthenticationPostMultiFactorAuthenticationRequest | 

    try:
        api_instance.multi_factor_authentication_post_multi_factor_authentication(tenant_id, user_id, multi_factor_authentication_post_multi_factor_authentication_request)
    except ApiException as e:
        print("Exception when calling MultiFactorAuthenticationApi->multi_factor_authentication_post_multi_factor_authentication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **multi_factor_authentication_post_multi_factor_authentication_request** | [**MultiFactorAuthenticationPostMultiFactorAuthenticationRequest**](MultiFactorAuthenticationPostMultiFactorAuthenticationRequest.md)|  | 

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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

