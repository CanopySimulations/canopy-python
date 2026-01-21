# canopy.openapi.DeploymentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deployments_create_deployment**](DeploymentsApi.md#deployments_create_deployment) | **POST** /deployments | Creates a new deployment.
[**deployments_get_account_features**](DeploymentsApi.md#deployments_get_account_features) | **GET** /deployments/features | Gets a list of all account features.
[**deployments_get_deployment**](DeploymentsApi.md#deployments_get_deployment) | **GET** /deployments/{deploymentId} | Gets metadata about the specified deployment.
[**deployments_get_deployments**](DeploymentsApi.md#deployments_get_deployments) | **GET** /deployments | Gets a list of all deployments.
[**deployments_get_invoice_bot_deployments**](DeploymentsApi.md#deployments_get_invoice_bot_deployments) | **GET** /deployments/invoicebot | Gets a list of deployments for invoice bot processing.
[**deployments_get_subscription_level**](DeploymentsApi.md#deployments_get_subscription_level) | **GET** /deployments/subscription-levels/{subscriptionLevelId} | Gets metadata about the specified subscription level.
[**deployments_get_subscription_levels**](DeploymentsApi.md#deployments_get_subscription_levels) | **GET** /deployments/subscription-levels | Gets a list of all subscription levels.
[**deployments_post_deployment_note**](DeploymentsApi.md#deployments_post_deployment_note) | **POST** /deployments/{deploymentId}/notes | Adds a note to the specified deployment.
[**deployments_update_deployment**](DeploymentsApi.md#deployments_update_deployment) | **PUT** /deployments/{deploymentId} | Updates the specified deployment.
[**deployments_update_invoice_bot_deployment**](DeploymentsApi.md#deployments_update_invoice_bot_deployment) | **PATCH** /deployments/{deploymentId}/invoicebot | Updates invoice bot fields for the specified deployment.


# **deployments_create_deployment**
> int deployments_create_deployment(deployments_create_deployment_request)

Creates a new deployment.

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
    api_instance = canopy.openapi.DeploymentsApi(api_client)
    deployments_create_deployment_request = canopy.openapi.DeploymentsCreateDeploymentRequest() # DeploymentsCreateDeploymentRequest | A data structure containing the deployment data.

    try:
        # Creates a new deployment.
        api_response = api_instance.deployments_create_deployment(deployments_create_deployment_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentsApi->deployments_create_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployments_create_deployment_request** | [**DeploymentsCreateDeploymentRequest**](DeploymentsCreateDeploymentRequest.md)| A data structure containing the deployment data. | 

### Return type

**int**

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

# **deployments_get_account_features**
> GetAccountFeaturesQueryResult deployments_get_account_features()

Gets a list of all account features.

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
    api_instance = canopy.openapi.DeploymentsApi(api_client)
    
    try:
        # Gets a list of all account features.
        api_response = api_instance.deployments_get_account_features()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentsApi->deployments_get_account_features: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAccountFeaturesQueryResult**](GetAccountFeaturesQueryResult.md)

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

# **deployments_get_deployment**
> GetDeploymentQueryResult deployments_get_deployment(deployment_id)

Gets metadata about the specified deployment.

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
    api_instance = canopy.openapi.DeploymentsApi(api_client)
    deployment_id = 56 # int | The deployment ID.

    try:
        # Gets metadata about the specified deployment.
        api_response = api_instance.deployments_get_deployment(deployment_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentsApi->deployments_get_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**| The deployment ID. | 

### Return type

[**GetDeploymentQueryResult**](GetDeploymentQueryResult.md)

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

# **deployments_get_deployments**
> GetDeploymentsQueryResult deployments_get_deployments()

Gets a list of all deployments.

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
    api_instance = canopy.openapi.DeploymentsApi(api_client)
    
    try:
        # Gets a list of all deployments.
        api_response = api_instance.deployments_get_deployments()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentsApi->deployments_get_deployments: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetDeploymentsQueryResult**](GetDeploymentsQueryResult.md)

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

# **deployments_get_invoice_bot_deployments**
> GetInvoiceBotDeploymentsQueryResult deployments_get_invoice_bot_deployments()

Gets a list of deployments for invoice bot processing.

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
    api_instance = canopy.openapi.DeploymentsApi(api_client)
    
    try:
        # Gets a list of deployments for invoice bot processing.
        api_response = api_instance.deployments_get_invoice_bot_deployments()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentsApi->deployments_get_invoice_bot_deployments: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetInvoiceBotDeploymentsQueryResult**](GetInvoiceBotDeploymentsQueryResult.md)

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

# **deployments_get_subscription_level**
> GetSubscriptionLevelQueryResult deployments_get_subscription_level(subscription_level_id)

Gets metadata about the specified subscription level.

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
    api_instance = canopy.openapi.DeploymentsApi(api_client)
    subscription_level_id = 56 # int | The subscription level ID.

    try:
        # Gets metadata about the specified subscription level.
        api_response = api_instance.deployments_get_subscription_level(subscription_level_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentsApi->deployments_get_subscription_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_level_id** | **int**| The subscription level ID. | 

### Return type

[**GetSubscriptionLevelQueryResult**](GetSubscriptionLevelQueryResult.md)

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

# **deployments_get_subscription_levels**
> GetSubscriptionLevelsQueryResult deployments_get_subscription_levels()

Gets a list of all subscription levels.

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
    api_instance = canopy.openapi.DeploymentsApi(api_client)
    
    try:
        # Gets a list of all subscription levels.
        api_response = api_instance.deployments_get_subscription_levels()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentsApi->deployments_get_subscription_levels: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSubscriptionLevelsQueryResult**](GetSubscriptionLevelsQueryResult.md)

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

# **deployments_post_deployment_note**
> DeploymentNoteResponse deployments_post_deployment_note(deployment_id, deployments_post_deployment_note_request=deployments_post_deployment_note_request)

Adds a note to the specified deployment.

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
    api_instance = canopy.openapi.DeploymentsApi(api_client)
    deployment_id = 56 # int | The deployment ID.
deployments_post_deployment_note_request = canopy.openapi.DeploymentsPostDeploymentNoteRequest() # DeploymentsPostDeploymentNoteRequest | A data structure containing the note text. (optional)

    try:
        # Adds a note to the specified deployment.
        api_response = api_instance.deployments_post_deployment_note(deployment_id, deployments_post_deployment_note_request=deployments_post_deployment_note_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentsApi->deployments_post_deployment_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**| The deployment ID. | 
 **deployments_post_deployment_note_request** | [**DeploymentsPostDeploymentNoteRequest**](DeploymentsPostDeploymentNoteRequest.md)| A data structure containing the note text. | [optional] 

### Return type

[**DeploymentNoteResponse**](DeploymentNoteResponse.md)

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

# **deployments_update_deployment**
> deployments_update_deployment(deployment_id, deployments_update_deployment_request=deployments_update_deployment_request)

Updates the specified deployment.

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
    api_instance = canopy.openapi.DeploymentsApi(api_client)
    deployment_id = 56 # int | The deployment ID.
deployments_update_deployment_request = canopy.openapi.DeploymentsUpdateDeploymentRequest() # DeploymentsUpdateDeploymentRequest | A data structure containing the deployment data to update. (optional)

    try:
        # Updates the specified deployment.
        api_instance.deployments_update_deployment(deployment_id, deployments_update_deployment_request=deployments_update_deployment_request)
    except ApiException as e:
        print("Exception when calling DeploymentsApi->deployments_update_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**| The deployment ID. | 
 **deployments_update_deployment_request** | [**DeploymentsUpdateDeploymentRequest**](DeploymentsUpdateDeploymentRequest.md)| A data structure containing the deployment data to update. | [optional] 

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

# **deployments_update_invoice_bot_deployment**
> deployments_update_invoice_bot_deployment(deployment_id, deployments_update_invoice_bot_deployment_request=deployments_update_invoice_bot_deployment_request)

Updates invoice bot fields for the specified deployment.

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
    api_instance = canopy.openapi.DeploymentsApi(api_client)
    deployment_id = 56 # int | The deployment ID.
deployments_update_invoice_bot_deployment_request = canopy.openapi.DeploymentsUpdateInvoiceBotDeploymentRequest() # DeploymentsUpdateInvoiceBotDeploymentRequest | A data structure containing the invoice bot fields to update. (optional)

    try:
        # Updates invoice bot fields for the specified deployment.
        api_instance.deployments_update_invoice_bot_deployment(deployment_id, deployments_update_invoice_bot_deployment_request=deployments_update_invoice_bot_deployment_request)
    except ApiException as e:
        print("Exception when calling DeploymentsApi->deployments_update_invoice_bot_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **int**| The deployment ID. | 
 **deployments_update_invoice_bot_deployment_request** | [**DeploymentsUpdateInvoiceBotDeploymentRequest**](DeploymentsUpdateInvoiceBotDeploymentRequest.md)| A data structure containing the invoice bot fields to update. | [optional] 

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

