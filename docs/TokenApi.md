# canopy.openapi.TokenApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**token_post_token**](TokenApi.md#token_post_token) | **POST** /token | Gets a token for the specified user.


# **token_post_token**
> GrantTypeHandlerResponse token_post_token(grant_type=grant_type, refresh_token=refresh_token, username=username, tenant=tenant, password=password, client_id=client_id, client_secret=client_secret)

Gets a token for the specified user.

This method is marked as obsolete and should be replaced with the identity.canopysimulations.com/connect/token endpoint.

### Example

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


# Enter a context with an instance of the API client
with canopy.openapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = canopy.openapi.TokenApi(api_client)
    grant_type = 'grant_type_example' # str | The grant type. Either `password` or `refresh_token`. (optional)
refresh_token = 'refresh_token_example' # str | The refresh token. Required for `refresh_token` grant type. (optional)
username = 'username_example' # str | The user's username. Required for `password` grant type. (optional)
tenant = 'tenant_example' # str | The user's tenant short name. Required for `password` grant type. (optional)
password = 'password_example' # str | The user's password. Required for `password` grant type. (optional)
client_id = 'client_id_example' # str | The client ID. Required for `password` or `refresh_token` grant type. (optional)
client_secret = 'client_secret_example' # str | The client secret. Required for `password` grant type. (optional)

    try:
        # Gets a token for the specified user.
        api_response = api_instance.token_post_token(grant_type=grant_type, refresh_token=refresh_token, username=username, tenant=tenant, password=password, client_id=client_id, client_secret=client_secret)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TokenApi->token_post_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| The grant type. Either &#x60;password&#x60; or &#x60;refresh_token&#x60;. | [optional] 
 **refresh_token** | **str**| The refresh token. Required for &#x60;refresh_token&#x60; grant type. | [optional] 
 **username** | **str**| The user&#39;s username. Required for &#x60;password&#x60; grant type. | [optional] 
 **tenant** | **str**| The user&#39;s tenant short name. Required for &#x60;password&#x60; grant type. | [optional] 
 **password** | **str**| The user&#39;s password. Required for &#x60;password&#x60; grant type. | [optional] 
 **client_id** | **str**| The client ID. Required for &#x60;password&#x60; or &#x60;refresh_token&#x60; grant type. | [optional] 
 **client_secret** | **str**| The client secret. Required for &#x60;password&#x60; grant type. | [optional] 

### Return type

[**GrantTypeHandlerResponse**](GrantTypeHandlerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

