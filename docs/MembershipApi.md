# canopy.openapi.MembershipApi

All URIs are relative to *https://api.canopysimulations.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**membership_delete_refresh_tokens**](MembershipApi.md#membership_delete_refresh_tokens) | **DELETE** /membership/refresh-tokens/{tenantId}/{userId} | 
[**membership_get_password_reset_token_validity**](MembershipApi.md#membership_get_password_reset_token_validity) | **GET** /membership/password-reset-tokens/{userId} | 
[**membership_get_user_roles**](MembershipApi.md#membership_get_user_roles) | **GET** /membership/roles/{tenantId}/{userId} | 
[**membership_post_identified_user**](MembershipApi.md#membership_post_identified_user) | **POST** /membership/identified-users | 
[**membership_post_initialize**](MembershipApi.md#membership_post_initialize) | **POST** /membership/initialize | 
[**membership_post_password_reset_confirmation**](MembershipApi.md#membership_post_password_reset_confirmation) | **POST** /membership/password-reset-confirmations | 
[**membership_post_password_reset_request**](MembershipApi.md#membership_post_password_reset_request) | **POST** /membership/password-reset-requests | 
[**membership_post_registration**](MembershipApi.md#membership_post_registration) | **POST** /membership/registrations | 
[**membership_put_user_role**](MembershipApi.md#membership_put_user_role) | **PUT** /membership/roles/{tenantId}/{userId} | 


# **membership_delete_refresh_tokens**
> membership_delete_refresh_tokens(tenant_id, user_id)



### Example

```python
from __future__ import print_function
import time
import canopy.openapi
from canopy.openapi.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with canopy.openapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = canopy.openapi.MembershipApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 

    try:
        api_instance.membership_delete_refresh_tokens(tenant_id, user_id)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_delete_refresh_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membership_get_password_reset_token_validity**
> object membership_get_password_reset_token_validity(user_id, token)



### Example

```python
from __future__ import print_function
import time
import canopy.openapi
from canopy.openapi.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with canopy.openapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = canopy.openapi.MembershipApi(api_client)
    user_id = 'user_id_example' # str | 
token = 'token_example' # str | 

    try:
        api_response = api_instance.membership_get_password_reset_token_validity(user_id, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_get_password_reset_token_validity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **token** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membership_get_user_roles**
> GetUserRolesQueryResult membership_get_user_roles(tenant_id, user_id)



### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import canopy.openapi
from canopy.openapi.rest import ApiException
from pprint import pprint
configuration = canopy.openapi.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.canopysimulations.com
configuration.host = "https://api.canopysimulations.com"

# Enter a context with an instance of the API client
with canopy.openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = canopy.openapi.MembershipApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 

    try:
        api_response = api_instance.membership_get_user_roles(tenant_id, user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_get_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**GetUserRolesQueryResult**](GetUserRolesQueryResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membership_post_identified_user**
> object membership_post_identified_user(identified_user_data)



### Example

```python
from __future__ import print_function
import time
import canopy.openapi
from canopy.openapi.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with canopy.openapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = canopy.openapi.MembershipApi(api_client)
    identified_user_data = canopy.openapi.IdentifiedUserData() # IdentifiedUserData | 

    try:
        api_response = api_instance.membership_post_identified_user(identified_user_data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_post_identified_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identified_user_data** | [**IdentifiedUserData**](IdentifiedUserData.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membership_post_initialize**
> membership_post_initialize()



### Example

```python
from __future__ import print_function
import time
import canopy.openapi
from canopy.openapi.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with canopy.openapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = canopy.openapi.MembershipApi(api_client)
    
    try:
        api_instance.membership_post_initialize()
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_post_initialize: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membership_post_password_reset_confirmation**
> object membership_post_password_reset_confirmation(password_reset_confirmation_data)



### Example

```python
from __future__ import print_function
import time
import canopy.openapi
from canopy.openapi.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with canopy.openapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = canopy.openapi.MembershipApi(api_client)
    password_reset_confirmation_data = canopy.openapi.PasswordResetConfirmationData() # PasswordResetConfirmationData | 

    try:
        api_response = api_instance.membership_post_password_reset_confirmation(password_reset_confirmation_data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_post_password_reset_confirmation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_reset_confirmation_data** | [**PasswordResetConfirmationData**](PasswordResetConfirmationData.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membership_post_password_reset_request**
> object membership_post_password_reset_request(password_reset_request_data)



### Example

```python
from __future__ import print_function
import time
import canopy.openapi
from canopy.openapi.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with canopy.openapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = canopy.openapi.MembershipApi(api_client)
    password_reset_request_data = canopy.openapi.PasswordResetRequestData() # PasswordResetRequestData | 

    try:
        api_response = api_instance.membership_post_password_reset_request(password_reset_request_data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_post_password_reset_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_reset_request_data** | [**PasswordResetRequestData**](PasswordResetRequestData.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membership_post_registration**
> object membership_post_registration(registration_data)



### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import canopy.openapi
from canopy.openapi.rest import ApiException
from pprint import pprint
configuration = canopy.openapi.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.canopysimulations.com
configuration.host = "https://api.canopysimulations.com"

# Enter a context with an instance of the API client
with canopy.openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = canopy.openapi.MembershipApi(api_client)
    registration_data = canopy.openapi.RegistrationData() # RegistrationData | 

    try:
        api_response = api_instance.membership_post_registration(registration_data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_post_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_data** | [**RegistrationData**](RegistrationData.md)|  | 

### Return type

**object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membership_put_user_role**
> membership_put_user_role(tenant_id, user_id, role_data)



### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import canopy.openapi
from canopy.openapi.rest import ApiException
from pprint import pprint
configuration = canopy.openapi.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.canopysimulations.com
configuration.host = "https://api.canopysimulations.com"

# Enter a context with an instance of the API client
with canopy.openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = canopy.openapi.MembershipApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
role_data = canopy.openapi.UserRoleData() # UserRoleData | 

    try:
        api_instance.membership_put_user_role(tenant_id, user_id, role_data)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_put_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **role_data** | [**UserRoleData**](UserRoleData.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

