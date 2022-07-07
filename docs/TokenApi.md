# canopy.openapi.TokenApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**token_post_token**](TokenApi.md#token_post_token) | **POST** /token | 


# **token_post_token**
> GrantTypeHandlerResponse token_post_token(grant_type=grant_type, refresh_token=refresh_token, username=username, tenant=tenant, password=password, client_id=client_id, client_secret=client_secret)



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
    grant_type = 'grant_type_example' # str |  (optional)
refresh_token = 'refresh_token_example' # str |  (optional)
username = 'username_example' # str |  (optional)
tenant = 'tenant_example' # str |  (optional)
password = 'password_example' # str |  (optional)
client_id = 'client_id_example' # str |  (optional)
client_secret = 'client_secret_example' # str |  (optional)

    try:
        api_response = api_instance.token_post_token(grant_type=grant_type, refresh_token=refresh_token, username=username, tenant=tenant, password=password, client_id=client_id, client_secret=client_secret)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TokenApi->token_post_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**|  | [optional] 
 **refresh_token** | **str**|  | [optional] 
 **username** | **str**|  | [optional] 
 **tenant** | **str**|  | [optional] 
 **password** | **str**|  | [optional] 
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

