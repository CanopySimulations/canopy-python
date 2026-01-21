# canopy.openapi.MembershipApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**membership_delete_refresh_tokens**](MembershipApi.md#membership_delete_refresh_tokens) | **DELETE** /membership/refresh-tokens/{tenantId}/{userId} | Clears all refresh tokens for the specified user. This forces all clients to re-authenticate.
[**membership_get_password_reset_token_validity**](MembershipApi.md#membership_get_password_reset_token_validity) | **GET** /membership/password-reset-tokens/{userId} | Checks the validity of a password reset token.
[**membership_get_user_roles**](MembershipApi.md#membership_get_user_roles) | **GET** /membership/roles/{tenantId}/{userId} | Gets the specified user&#39;s roles.
[**membership_get_zendesk_token**](MembershipApi.md#membership_get_zendesk_token) | **GET** /membership/zendesk-token/{tenantId}/{userId} | Gets the specified user&#39;s Zendesk token. This is used to provide SSO with Zendesk.
[**membership_post_email_confirmation**](MembershipApi.md#membership_post_email_confirmation) | **POST** /membership/email-confirmations | Posts an email address confirmation. If successful, the user&#39;s email address will have been confirmed.
[**membership_post_email_confirmation_request**](MembershipApi.md#membership_post_email_confirmation_request) | **POST** /membership/email-confirmation-requests/{tenantId}/{userId} | Request an email address confirmation for a user. This sends an email to the user which they can use to confirm their email address.
[**membership_post_identified_user**](MembershipApi.md#membership_post_identified_user) | **POST** /membership/identified-users | This API endpoint is no longer used.
[**membership_post_initialize**](MembershipApi.md#membership_post_initialize) | **POST** /membership/initialize | This method performs some initialization tasks on a new instance of the platform,  and does nothing on existing instances.
[**membership_post_password_reset_confirmation**](MembershipApi.md#membership_post_password_reset_confirmation) | **POST** /membership/password-reset-confirmations | Confirms a password reset for a user.
[**membership_post_password_reset_request**](MembershipApi.md#membership_post_password_reset_request) | **POST** /membership/password-reset-requests | Requests a password reset for a user.  If the user exists they will be send a password reset email containing a link they can click on  to reset their password.  If the user does not exist, nothing happens.
[**membership_post_registration**](MembershipApi.md#membership_post_registration) | **POST** /membership/registrations | Registers a new user on the platform.
[**membership_put_user_role**](MembershipApi.md#membership_put_user_role) | **PUT** /membership/roles/{tenantId}/{userId} | Adds or removes a user role from the specified user.


# **membership_delete_refresh_tokens**
> membership_delete_refresh_tokens(tenant_id, user_id)

Clears all refresh tokens for the specified user. This forces all clients to re-authenticate.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID of the user.
user_id = 'user_id_example' # str | The user ID of the user.

    try:
        # Clears all refresh tokens for the specified user. This forces all clients to re-authenticate.
        api_instance.membership_delete_refresh_tokens(tenant_id, user_id)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_delete_refresh_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID of the user. | 
 **user_id** | **str**| The user ID of the user. | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membership_get_password_reset_token_validity**
> membership_get_password_reset_token_validity(user_id, token)

Checks the validity of a password reset token.

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
    user_id = 'user_id_example' # str | The user ID the token was generated for.
token = 'token_example' # str | The password reset token.

    try:
        # Checks the validity of a password reset token.
        api_instance.membership_get_password_reset_token_validity(user_id, token)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_get_password_reset_token_validity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user ID the token was generated for. | 
 **token** | **str**| The password reset token. | 

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

# **membership_get_user_roles**
> GetUserRolesQueryResult membership_get_user_roles(tenant_id, user_id)

Gets the specified user's roles.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID of the user.
user_id = 'user_id_example' # str | The user ID of the user.

    try:
        # Gets the specified user's roles.
        api_response = api_instance.membership_get_user_roles(tenant_id, user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_get_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID of the user. | 
 **user_id** | **str**| The user ID of the user. | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membership_get_zendesk_token**
> GetZendeskTokenQueryResult membership_get_zendesk_token(tenant_id, user_id)

Gets the specified user's Zendesk token. This is used to provide SSO with Zendesk.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID of the user.
user_id = 'user_id_example' # str | The user ID of the user.

    try:
        # Gets the specified user's Zendesk token. This is used to provide SSO with Zendesk.
        api_response = api_instance.membership_get_zendesk_token(tenant_id, user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_get_zendesk_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID of the user. | 
 **user_id** | **str**| The user ID of the user. | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membership_post_email_confirmation**
> membership_post_email_confirmation(membership_post_email_confirmation_request)

Posts an email address confirmation. If successful, the user's email address will have been confirmed.

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
    membership_post_email_confirmation_request = canopy.openapi.MembershipPostEmailConfirmationRequest() # MembershipPostEmailConfirmationRequest | A data structure containing the email confirmation token which was sent to the user's email address.

    try:
        # Posts an email address confirmation. If successful, the user's email address will have been confirmed.
        api_instance.membership_post_email_confirmation(membership_post_email_confirmation_request)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_post_email_confirmation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_post_email_confirmation_request** | [**MembershipPostEmailConfirmationRequest**](MembershipPostEmailConfirmationRequest.md)| A data structure containing the email confirmation token which was sent to the user&#39;s email address. | 

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

Request an email address confirmation for a user. This sends an email to the user which they can use to confirm their email address.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID of the user.
user_id = 'user_id_example' # str | The user ID of the user.

    try:
        # Request an email address confirmation for a user. This sends an email to the user which they can use to confirm their email address.
        api_instance.membership_post_email_confirmation_request(tenant_id, user_id)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_post_email_confirmation_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID of the user. | 
 **user_id** | **str**| The user ID of the user. | 

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
> membership_post_identified_user(membership_post_identified_user_request)

This API endpoint is no longer used.

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
    membership_post_identified_user_request = canopy.openapi.MembershipPostIdentifiedUserRequest() # MembershipPostIdentifiedUserRequest | Information about the identified user.

    try:
        # This API endpoint is no longer used.
        api_instance.membership_post_identified_user(membership_post_identified_user_request)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_post_identified_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_post_identified_user_request** | [**MembershipPostIdentifiedUserRequest**](MembershipPostIdentifiedUserRequest.md)| Information about the identified user. | 

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

This method performs some initialization tasks on a new instance of the platform,  and does nothing on existing instances.

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
        # This method performs some initialization tasks on a new instance of the platform,  and does nothing on existing instances.
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membership_post_password_reset_confirmation**
> membership_post_password_reset_confirmation(membership_post_password_reset_confirmation_request)

Confirms a password reset for a user.

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
    membership_post_password_reset_confirmation_request = canopy.openapi.MembershipPostPasswordResetConfirmationRequest() # MembershipPostPasswordResetConfirmationRequest | The password reset confirmation data, consisting of the user ID, then new password, and the security token from the password reset email.

    try:
        # Confirms a password reset for a user.
        api_instance.membership_post_password_reset_confirmation(membership_post_password_reset_confirmation_request)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_post_password_reset_confirmation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_post_password_reset_confirmation_request** | [**MembershipPostPasswordResetConfirmationRequest**](MembershipPostPasswordResetConfirmationRequest.md)| The password reset confirmation data, consisting of the user ID, then new password, and the security token from the password reset email. | 

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
> membership_post_password_reset_request(membership_post_password_reset_request_request)

Requests a password reset for a user.  If the user exists they will be send a password reset email containing a link they can click on  to reset their password.  If the user does not exist, nothing happens.

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
    membership_post_password_reset_request_request = canopy.openapi.MembershipPostPasswordResetRequestRequest() # MembershipPostPasswordResetRequestRequest | A data structure containing the tenant short name, and either the username or the email address of the user.

    try:
        # Requests a password reset for a user.  If the user exists they will be send a password reset email containing a link they can click on  to reset their password.  If the user does not exist, nothing happens.
        api_instance.membership_post_password_reset_request(membership_post_password_reset_request_request)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_post_password_reset_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_post_password_reset_request_request** | [**MembershipPostPasswordResetRequestRequest**](MembershipPostPasswordResetRequestRequest.md)| A data structure containing the tenant short name, and either the username or the email address of the user. | 

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
> membership_post_registration(membership_post_registration_request)

Registers a new user on the platform.

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
    membership_post_registration_request = canopy.openapi.MembershipPostRegistrationRequest() # MembershipPostRegistrationRequest | Required information about the new user.

    try:
        # Registers a new user on the platform.
        api_instance.membership_post_registration(membership_post_registration_request)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_post_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_post_registration_request** | [**MembershipPostRegistrationRequest**](MembershipPostRegistrationRequest.md)| Required information about the new user. | 

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

Adds or removes a user role from the specified user.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID of the user.
user_id = 'user_id_example' # str | The user ID of the user.
membership_put_user_role_request = canopy.openapi.MembershipPutUserRoleRequest() # MembershipPutUserRoleRequest | The role and whether or not it is enabled.

    try:
        # Adds or removes a user role from the specified user.
        api_instance.membership_put_user_role(tenant_id, user_id, membership_put_user_role_request)
    except ApiException as e:
        print("Exception when calling MembershipApi->membership_put_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID of the user. | 
 **user_id** | **str**| The user ID of the user. | 
 **membership_put_user_role_request** | [**MembershipPutUserRoleRequest**](MembershipPutUserRoleRequest.md)| The role and whether or not it is enabled. | 

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

