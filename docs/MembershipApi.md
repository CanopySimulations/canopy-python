# canopy.openapi.MembershipApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**membership_delete_refresh_tokens**](MembershipApi.md#membership_delete_refresh_tokens) | **DELETE** /membership/refresh-tokens/{tenantId}/{userId} | 
[**membership_get_password_reset_token_validity**](MembershipApi.md#membership_get_password_reset_token_validity) | **GET** /membership/password-reset-tokens/{userId} | 
[**membership_get_upvoty_token**](MembershipApi.md#membership_get_upvoty_token) | **GET** /membership/upvoty-token/{tenantId}/{userId} | 
[**membership_get_user_roles**](MembershipApi.md#membership_get_user_roles) | **GET** /membership/roles/{tenantId}/{userId} | 
[**membership_get_zendesk_token**](MembershipApi.md#membership_get_zendesk_token) | **GET** /membership/zendesk-token/{tenantId}/{userId} | 
[**membership_post_email_confirmation**](MembershipApi.md#membership_post_email_confirmation) | **POST** /membership/email-confirmations | 
[**membership_post_email_confirmation_request**](MembershipApi.md#membership_post_email_confirmation_request) | **POST** /membership/email-confirmation-requests/{tenantId}/{userId} | 
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
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = canopy.openapi.Configuration(
    host = "http://localhost"
)


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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membership_get_password_reset_token_validity**
> membership_get_password_reset_token_validity(user_id, token)



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
    api_instance = canopy.openapi.MembershipApi(api_client)
    user_id = 'user_id_example' # str | 
token = 'token_example' # str | 

    try:
        api_instance.membership_get_password_reset_token_validity(user_id, token)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_get_password_reset_token_validity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **token** | **str**|  | 

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

# **membership_get_upvoty_token**
> GetUpvotyTokenQueryResult membership_get_upvoty_token(tenant_id, user_id)



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
    api_instance = canopy.openapi.MembershipApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 

    try:
        api_response = api_instance.membership_get_upvoty_token(tenant_id, user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_get_upvoty_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**GetUpvotyTokenQueryResult**](GetUpvotyTokenQueryResult.md)

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

# **membership_get_user_roles**
> GetUserRolesQueryResult membership_get_user_roles(tenant_id, user_id)



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

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membership_get_zendesk_token**
> GetZendeskTokenQueryResult membership_get_zendesk_token(tenant_id, user_id)



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
    api_instance = canopy.openapi.MembershipApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 

    try:
        api_response = api_instance.membership_get_zendesk_token(tenant_id, user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_get_zendesk_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**GetZendeskTokenQueryResult**](GetZendeskTokenQueryResult.md)

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

# **membership_post_email_confirmation**
> membership_post_email_confirmation(membership_post_email_confirmation_request=membership_post_email_confirmation_request)



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
    api_instance = canopy.openapi.MembershipApi(api_client)
    membership_post_email_confirmation_request = canopy.openapi.MembershipPostEmailConfirmationRequest() # MembershipPostEmailConfirmationRequest |  (optional)

    try:
        api_instance.membership_post_email_confirmation(membership_post_email_confirmation_request=membership_post_email_confirmation_request)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_post_email_confirmation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_post_email_confirmation_request** | [**MembershipPostEmailConfirmationRequest**](MembershipPostEmailConfirmationRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membership_post_email_confirmation_request**
> membership_post_email_confirmation_request(tenant_id, user_id)



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
    api_instance = canopy.openapi.MembershipApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 

    try:
        api_instance.membership_post_email_confirmation_request(tenant_id, user_id)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_post_email_confirmation_request: %s\n" % e)
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

# **membership_post_identified_user**
> membership_post_identified_user(membership_post_identified_user_request=membership_post_identified_user_request)



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
    api_instance = canopy.openapi.MembershipApi(api_client)
    membership_post_identified_user_request = canopy.openapi.MembershipPostIdentifiedUserRequest() # MembershipPostIdentifiedUserRequest |  (optional)

    try:
        api_instance.membership_post_identified_user(membership_post_identified_user_request=membership_post_identified_user_request)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_post_identified_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_post_identified_user_request** | [**MembershipPostIdentifiedUserRequest**](MembershipPostIdentifiedUserRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

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
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = canopy.openapi.Configuration(
    host = "http://localhost"
)


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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membership_post_password_reset_confirmation**
> membership_post_password_reset_confirmation(membership_post_password_reset_confirmation_request=membership_post_password_reset_confirmation_request)



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
    api_instance = canopy.openapi.MembershipApi(api_client)
    membership_post_password_reset_confirmation_request = canopy.openapi.MembershipPostPasswordResetConfirmationRequest() # MembershipPostPasswordResetConfirmationRequest |  (optional)

    try:
        api_instance.membership_post_password_reset_confirmation(membership_post_password_reset_confirmation_request=membership_post_password_reset_confirmation_request)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_post_password_reset_confirmation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_post_password_reset_confirmation_request** | [**MembershipPostPasswordResetConfirmationRequest**](MembershipPostPasswordResetConfirmationRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membership_post_password_reset_request**
> membership_post_password_reset_request(membership_post_password_reset_request_request=membership_post_password_reset_request_request)



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
    api_instance = canopy.openapi.MembershipApi(api_client)
    membership_post_password_reset_request_request = canopy.openapi.MembershipPostPasswordResetRequestRequest() # MembershipPostPasswordResetRequestRequest |  (optional)

    try:
        api_instance.membership_post_password_reset_request(membership_post_password_reset_request_request=membership_post_password_reset_request_request)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_post_password_reset_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_post_password_reset_request_request** | [**MembershipPostPasswordResetRequestRequest**](MembershipPostPasswordResetRequestRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membership_post_registration**
> membership_post_registration(membership_post_registration_request=membership_post_registration_request)



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
    api_instance = canopy.openapi.MembershipApi(api_client)
    membership_post_registration_request = canopy.openapi.MembershipPostRegistrationRequest() # MembershipPostRegistrationRequest |  (optional)

    try:
        api_instance.membership_post_registration(membership_post_registration_request=membership_post_registration_request)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_post_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_post_registration_request** | [**MembershipPostRegistrationRequest**](MembershipPostRegistrationRequest.md)|  | [optional] 

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

# **membership_put_user_role**
> membership_put_user_role(tenant_id, user_id, membership_put_user_role_request)



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
    api_instance = canopy.openapi.MembershipApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
membership_put_user_role_request = canopy.openapi.MembershipPutUserRoleRequest() # MembershipPutUserRoleRequest | 

    try:
        api_instance.membership_put_user_role(tenant_id, user_id, membership_put_user_role_request)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_put_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **membership_put_user_role_request** | [**MembershipPutUserRoleRequest**](MembershipPutUserRoleRequest.md)|  | 

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

