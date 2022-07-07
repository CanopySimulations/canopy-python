# canopy.openapi.StudyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**study_delete_study**](StudyApi.md#study_delete_study) | **DELETE** /studies/{tenantId}/{studyId} | 
[**study_delete_study_deprecated**](StudyApi.md#study_delete_study_deprecated) | **DELETE** /studies/{tenantId}/{userId}/{studyId} | 
[**study_get_all_tenants_study_statistics**](StudyApi.md#study_get_all_tenants_study_statistics) | **GET** /studies/statistics | 
[**study_get_sim_type**](StudyApi.md#study_get_sim_type) | **GET** /studies/types/sims/{simType} | 
[**study_get_studies**](StudyApi.md#study_get_studies) | **GET** /studies/{tenantId} | 
[**study_get_study**](StudyApi.md#study_get_study) | **GET** /studies/{tenantId}/{studyId} | 
[**study_get_study_deprecated**](StudyApi.md#study_get_study_deprecated) | **GET** /studies/{tenantId}/{userId}/{studyId} | 
[**study_get_study_download**](StudyApi.md#study_get_study_download) | **GET** /studies/{tenantId}/{studyId}/download | 
[**study_get_study_download_deprecated**](StudyApi.md#study_get_study_download_deprecated) | **GET** /studies/{tenantId}/{userId}/{studyId}/download | 
[**study_get_study_download_url**](StudyApi.md#study_get_study_download_url) | **GET** /studies/{tenantId}/{studyId}/download-url | 
[**study_get_study_download_url_deprecated**](StudyApi.md#study_get_study_download_url_deprecated) | **GET** /studies/{tenantId}/{userId}/{studyId}/download-url | 
[**study_get_study_job**](StudyApi.md#study_get_study_job) | **GET** /studies/{tenantId}/{studyId}/jobs/{jobId} | 
[**study_get_study_job_deprecated**](StudyApi.md#study_get_study_job_deprecated) | **GET** /studies/{tenantId}/{userId}/{studyId}/jobs/{jobId} | 
[**study_get_study_job_download**](StudyApi.md#study_get_study_job_download) | **GET** /studies/{tenantId}/{studyId}/jobs/{jobId}/download | 
[**study_get_study_job_download_deprecated**](StudyApi.md#study_get_study_job_download_deprecated) | **GET** /studies/{tenantId}/{userId}/{studyId}/jobs/{jobId}/download | 
[**study_get_study_job_metadata**](StudyApi.md#study_get_study_job_metadata) | **GET** /studies/{tenantId}/{studyId}/jobs/{jobId}/metadata | 
[**study_get_study_job_metadata_deprecated**](StudyApi.md#study_get_study_job_metadata_deprecated) | **GET** /studies/{tenantId}/{userId}/{studyId}/jobs/{jobId}/metadata | 
[**study_get_study_jobs**](StudyApi.md#study_get_study_jobs) | **GET** /studies/{tenantId}/{studyId}/jobs | 
[**study_get_study_jobs_deprecated**](StudyApi.md#study_get_study_jobs_deprecated) | **GET** /studies/{tenantId}/{userId}/{studyId}/jobs | 
[**study_get_study_metadata**](StudyApi.md#study_get_study_metadata) | **GET** /studies/{tenantId}/{studyId}/metadata | 
[**study_get_study_metadata_deprecated**](StudyApi.md#study_get_study_metadata_deprecated) | **GET** /studies/{tenantId}/{userId}/{studyId}/metadata | 
[**study_get_study_metadata_without_user_id_deprecated**](StudyApi.md#study_get_study_metadata_without_user_id_deprecated) | **GET** /studies/{tenantId}/auto/{studyId}/metadata | 
[**study_get_study_type**](StudyApi.md#study_get_study_type) | **GET** /studies/types/{studyType} | 
[**study_get_study_types**](StudyApi.md#study_get_study_types) | **GET** /studies/types | 
[**study_get_study_without_user_id_deprecated**](StudyApi.md#study_get_study_without_user_id_deprecated) | **GET** /studies/{tenantId}/auto/{studyId} | 
[**study_get_tenant_access_information**](StudyApi.md#study_get_tenant_access_information) | **GET** /studies/{tenantId}/access | 
[**study_get_tenant_billable_stored_simulation_count**](StudyApi.md#study_get_tenant_billable_stored_simulation_count) | **GET** /studies/statistics/stored/{tenantId} | 
[**study_get_tenant_study_statistics**](StudyApi.md#study_get_tenant_study_statistics) | **GET** /studies/statistics/{tenantId} | 
[**study_merge_study**](StudyApi.md#study_merge_study) | **PATCH** /studies/{tenantId}/{studyId}/merge | 
[**study_merge_study_deprecated**](StudyApi.md#study_merge_study_deprecated) | **PATCH** /studies/{tenantId}/{userId}/{studyId}/merge | 
[**study_post_study**](StudyApi.md#study_post_study) | **POST** /studies/{tenantId} | 
[**study_post_study_deprecated**](StudyApi.md#study_post_study_deprecated) | **POST** /studies/{tenantId}/{userId} | 
[**study_put_study**](StudyApi.md#study_put_study) | **PUT** /studies/{tenantId}/{studyId} | 
[**study_put_study_deprecated**](StudyApi.md#study_put_study_deprecated) | **PUT** /studies/{tenantId}/{userId}/{studyId} | 
[**study_put_study_owner**](StudyApi.md#study_put_study_owner) | **PUT** /studies/{tenantId}/{studyId}/owner | 


# **study_delete_study**
> study_delete_study(tenant_id, study_id, undelete=undelete)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
study_id = 'study_id_example' # str | 
undelete = False # bool |  (optional) (default to False)

    try:
        api_instance.study_delete_study(tenant_id, study_id, undelete=undelete)
    except ApiException as e:
        print("Exception when calling StudyApi->study_delete_study: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **study_id** | **str**|  | 
 **undelete** | **bool**|  | [optional] [default to False]

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_delete_study_deprecated**
> study_delete_study_deprecated(tenant_id, user_id, study_id, undelete=undelete)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
study_id = 'study_id_example' # str | 
undelete = False # bool |  (optional) (default to False)

    try:
        api_instance.study_delete_study_deprecated(tenant_id, user_id, study_id, undelete=undelete)
    except ApiException as e:
        print("Exception when calling StudyApi->study_delete_study_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **study_id** | **str**|  | 
 **undelete** | **bool**|  | [optional] [default to False]

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_get_all_tenants_study_statistics**
> GetAllTenantsStudyStatisticsQueryResult study_get_all_tenants_study_statistics(start_date=start_date, end_date=end_date)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)

    try:
        api_response = api_instance.study_get_all_tenants_study_statistics(start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_all_tenants_study_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 

### Return type

[**GetAllTenantsStudyStatisticsQueryResult**](GetAllTenantsStudyStatisticsQueryResult.md)

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

# **study_get_sim_type**
> SimTypeDefinition study_get_sim_type(sim_type, tenant_id=tenant_id)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    sim_type = 'sim_type_example' # str | 
tenant_id = 'tenant_id_example' # str |  (optional)

    try:
        api_response = api_instance.study_get_sim_type(sim_type, tenant_id=tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_sim_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_type** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 

### Return type

[**SimTypeDefinition**](SimTypeDefinition.md)

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

# **study_get_studies**
> GetStudiesQueryResult study_get_studies(tenant_id, filter=filter, include_transient=include_transient, result_type=result_type)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
filter = 'filter_example' # str |  (optional)
include_transient = False # bool |  (optional) (default to False)
result_type = 'result_type_example' # str |  (optional)

    try:
        api_response = api_instance.study_get_studies(tenant_id, filter=filter, include_transient=include_transient, result_type=result_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_studies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **filter** | **str**|  | [optional] 
 **include_transient** | **bool**|  | [optional] [default to False]
 **result_type** | **str**|  | [optional] 

### Return type

[**GetStudiesQueryResult**](GetStudiesQueryResult.md)

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

# **study_get_study**
> GetStudyQueryResult study_get_study(tenant_id, study_id, sim_version=sim_version)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
study_id = 'study_id_example' # str | 
sim_version = 'sim_version_example' # str |  (optional)

    try:
        api_response = api_instance.study_get_study(tenant_id, study_id, sim_version=sim_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **study_id** | **str**|  | 
 **sim_version** | **str**|  | [optional] 

### Return type

[**GetStudyQueryResult**](GetStudyQueryResult.md)

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

# **study_get_study_deprecated**
> GetStudyQueryResult study_get_study_deprecated(tenant_id, user_id, study_id, sim_version=sim_version)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
study_id = 'study_id_example' # str | 
sim_version = 'sim_version_example' # str |  (optional)

    try:
        api_response = api_instance.study_get_study_deprecated(tenant_id, user_id, study_id, sim_version=sim_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **study_id** | **str**|  | 
 **sim_version** | **str**|  | [optional] 

### Return type

[**GetStudyQueryResult**](GetStudyQueryResult.md)

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

# **study_get_study_download**
> study_get_study_download(tenant_id, study_id, access_signature, expiry, file_name=file_name, full=full, channels_as_csv=channels_as_csv, merged_scalar_results_only=merged_scalar_results_only)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
study_id = 'study_id_example' # str | 
access_signature = 'access_signature_example' # str | 
expiry = 'expiry_example' # str | 
file_name = 'file_name_example' # str |  (optional)
full = False # bool |  (optional) (default to False)
channels_as_csv = False # bool |  (optional) (default to False)
merged_scalar_results_only = False # bool |  (optional) (default to False)

    try:
        api_instance.study_get_study_download(tenant_id, study_id, access_signature, expiry, file_name=file_name, full=full, channels_as_csv=channels_as_csv, merged_scalar_results_only=merged_scalar_results_only)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **study_id** | **str**|  | 
 **access_signature** | **str**|  | 
 **expiry** | **str**|  | 
 **file_name** | **str**|  | [optional] 
 **full** | **bool**|  | [optional] [default to False]
 **channels_as_csv** | **bool**|  | [optional] [default to False]
 **merged_scalar_results_only** | **bool**|  | [optional] [default to False]

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

# **study_get_study_download_deprecated**
> study_get_study_download_deprecated(tenant_id, user_id, study_id, access_signature=access_signature, expiry=expiry, file_name=file_name, full=full, channels_as_csv=channels_as_csv, merged_scalar_results_only=merged_scalar_results_only)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
study_id = 'study_id_example' # str | 
access_signature = 'access_signature_example' # str |  (optional)
expiry = 'expiry_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)
full = False # bool |  (optional) (default to False)
channels_as_csv = False # bool |  (optional) (default to False)
merged_scalar_results_only = False # bool |  (optional) (default to False)

    try:
        api_instance.study_get_study_download_deprecated(tenant_id, user_id, study_id, access_signature=access_signature, expiry=expiry, file_name=file_name, full=full, channels_as_csv=channels_as_csv, merged_scalar_results_only=merged_scalar_results_only)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_download_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **study_id** | **str**|  | 
 **access_signature** | **str**|  | [optional] 
 **expiry** | **str**|  | [optional] 
 **file_name** | **str**|  | [optional] 
 **full** | **bool**|  | [optional] [default to False]
 **channels_as_csv** | **bool**|  | [optional] [default to False]
 **merged_scalar_results_only** | **bool**|  | [optional] [default to False]

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

# **study_get_study_download_url**
> GetStudyDownloadUrlQueryResult study_get_study_download_url(tenant_id, study_id)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
study_id = 'study_id_example' # str | 

    try:
        api_response = api_instance.study_get_study_download_url(tenant_id, study_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_download_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **study_id** | **str**|  | 

### Return type

[**GetStudyDownloadUrlQueryResult**](GetStudyDownloadUrlQueryResult.md)

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

# **study_get_study_download_url_deprecated**
> GetStudyDownloadUrlQueryResult study_get_study_download_url_deprecated(tenant_id, user_id, study_id)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
study_id = 'study_id_example' # str | 

    try:
        api_response = api_instance.study_get_study_download_url_deprecated(tenant_id, user_id, study_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_download_url_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **study_id** | **str**|  | 

### Return type

[**GetStudyDownloadUrlQueryResult**](GetStudyDownloadUrlQueryResult.md)

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

# **study_get_study_job**
> GetStudyJobQueryResult study_get_study_job(tenant_id, study_id, job_id, sim_version=sim_version)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
study_id = 'study_id_example' # str | 
job_id = 'job_id_example' # str | 
sim_version = 'sim_version_example' # str |  (optional)

    try:
        api_response = api_instance.study_get_study_job(tenant_id, study_id, job_id, sim_version=sim_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **study_id** | **str**|  | 
 **job_id** | **str**|  | 
 **sim_version** | **str**|  | [optional] 

### Return type

[**GetStudyJobQueryResult**](GetStudyJobQueryResult.md)

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

# **study_get_study_job_deprecated**
> GetStudyJobQueryResult study_get_study_job_deprecated(tenant_id, user_id, study_id, job_id, sim_version=sim_version)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
study_id = 'study_id_example' # str | 
job_id = 'job_id_example' # str | 
sim_version = 'sim_version_example' # str |  (optional)

    try:
        api_response = api_instance.study_get_study_job_deprecated(tenant_id, user_id, study_id, job_id, sim_version=sim_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_job_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **study_id** | **str**|  | 
 **job_id** | **str**|  | 
 **sim_version** | **str**|  | [optional] 

### Return type

[**GetStudyJobQueryResult**](GetStudyJobQueryResult.md)

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

# **study_get_study_job_download**
> study_get_study_job_download(tenant_id, study_id, job_id, access_signature, expiry, file_name=file_name, channels_as_csv=channels_as_csv, sim_type_channels=sim_type_channels)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
study_id = 'study_id_example' # str | 
job_id = 'job_id_example' # str | 
access_signature = 'access_signature_example' # str | 
expiry = 'expiry_example' # str | 
file_name = 'file_name_example' # str |  (optional)
channels_as_csv = False # bool |  (optional) (default to False)
sim_type_channels = 'sim_type_channels_example' # str |  (optional)

    try:
        api_instance.study_get_study_job_download(tenant_id, study_id, job_id, access_signature, expiry, file_name=file_name, channels_as_csv=channels_as_csv, sim_type_channels=sim_type_channels)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_job_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **study_id** | **str**|  | 
 **job_id** | **str**|  | 
 **access_signature** | **str**|  | 
 **expiry** | **str**|  | 
 **file_name** | **str**|  | [optional] 
 **channels_as_csv** | **bool**|  | [optional] [default to False]
 **sim_type_channels** | **str**|  | [optional] 

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

# **study_get_study_job_download_deprecated**
> study_get_study_job_download_deprecated(tenant_id, user_id, study_id, job_id, access_signature=access_signature, expiry=expiry, file_name=file_name, channels_as_csv=channels_as_csv, sim_type_channels=sim_type_channels)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
study_id = 'study_id_example' # str | 
job_id = 'job_id_example' # str | 
access_signature = 'access_signature_example' # str |  (optional)
expiry = 'expiry_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)
channels_as_csv = False # bool |  (optional) (default to False)
sim_type_channels = 'sim_type_channels_example' # str |  (optional)

    try:
        api_instance.study_get_study_job_download_deprecated(tenant_id, user_id, study_id, job_id, access_signature=access_signature, expiry=expiry, file_name=file_name, channels_as_csv=channels_as_csv, sim_type_channels=sim_type_channels)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_job_download_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **study_id** | **str**|  | 
 **job_id** | **str**|  | 
 **access_signature** | **str**|  | [optional] 
 **expiry** | **str**|  | [optional] 
 **file_name** | **str**|  | [optional] 
 **channels_as_csv** | **bool**|  | [optional] [default to False]
 **sim_type_channels** | **str**|  | [optional] 

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

# **study_get_study_job_metadata**
> GetStudyJobMetadataQueryResult study_get_study_job_metadata(tenant_id, study_id, job_id)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
study_id = 'study_id_example' # str | 
job_id = 'job_id_example' # str | 

    try:
        api_response = api_instance.study_get_study_job_metadata(tenant_id, study_id, job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_job_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **study_id** | **str**|  | 
 **job_id** | **str**|  | 

### Return type

[**GetStudyJobMetadataQueryResult**](GetStudyJobMetadataQueryResult.md)

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

# **study_get_study_job_metadata_deprecated**
> GetStudyJobMetadataQueryResult study_get_study_job_metadata_deprecated(tenant_id, user_id, study_id, job_id)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
study_id = 'study_id_example' # str | 
job_id = 'job_id_example' # str | 

    try:
        api_response = api_instance.study_get_study_job_metadata_deprecated(tenant_id, user_id, study_id, job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_job_metadata_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **study_id** | **str**|  | 
 **job_id** | **str**|  | 

### Return type

[**GetStudyJobMetadataQueryResult**](GetStudyJobMetadataQueryResult.md)

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

# **study_get_study_jobs**
> GetStudyJobsQueryResult study_get_study_jobs(tenant_id, study_id, filter=filter)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
study_id = 'study_id_example' # str | 
filter = 'filter_example' # str |  (optional)

    try:
        api_response = api_instance.study_get_study_jobs(tenant_id, study_id, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **study_id** | **str**|  | 
 **filter** | **str**|  | [optional] 

### Return type

[**GetStudyJobsQueryResult**](GetStudyJobsQueryResult.md)

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

# **study_get_study_jobs_deprecated**
> GetStudyJobsQueryResult study_get_study_jobs_deprecated(tenant_id, user_id, study_id, filter=filter)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
study_id = 'study_id_example' # str | 
filter = 'filter_example' # str |  (optional)

    try:
        api_response = api_instance.study_get_study_jobs_deprecated(tenant_id, user_id, study_id, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_jobs_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **study_id** | **str**|  | 
 **filter** | **str**|  | [optional] 

### Return type

[**GetStudyJobsQueryResult**](GetStudyJobsQueryResult.md)

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

# **study_get_study_metadata**
> GetStudyQueryResult study_get_study_metadata(tenant_id, study_id)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
study_id = 'study_id_example' # str | 

    try:
        api_response = api_instance.study_get_study_metadata(tenant_id, study_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **study_id** | **str**|  | 

### Return type

[**GetStudyQueryResult**](GetStudyQueryResult.md)

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

# **study_get_study_metadata_deprecated**
> GetStudyQueryResult study_get_study_metadata_deprecated(tenant_id, user_id, study_id)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
study_id = 'study_id_example' # str | 

    try:
        api_response = api_instance.study_get_study_metadata_deprecated(tenant_id, user_id, study_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_metadata_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **study_id** | **str**|  | 

### Return type

[**GetStudyQueryResult**](GetStudyQueryResult.md)

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

# **study_get_study_metadata_without_user_id_deprecated**
> GetStudyQueryResult study_get_study_metadata_without_user_id_deprecated(tenant_id, study_id)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
study_id = 'study_id_example' # str | 

    try:
        api_response = api_instance.study_get_study_metadata_without_user_id_deprecated(tenant_id, study_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_metadata_without_user_id_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **study_id** | **str**|  | 

### Return type

[**GetStudyQueryResult**](GetStudyQueryResult.md)

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

# **study_get_study_type**
> StudyTypeDefinition study_get_study_type(study_type, tenant_id=tenant_id)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    study_type = 'study_type_example' # str | 
tenant_id = 'tenant_id_example' # str |  (optional)

    try:
        api_response = api_instance.study_get_study_type(study_type, tenant_id=tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_type** | **str**|  | 
 **tenant_id** | **str**|  | [optional] 

### Return type

[**StudyTypeDefinition**](StudyTypeDefinition.md)

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

# **study_get_study_types**
> GetStudyTypesQueryResult study_get_study_types(tenant_id=tenant_id)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)

    try:
        api_response = api_instance.study_get_study_types(tenant_id=tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 

### Return type

[**GetStudyTypesQueryResult**](GetStudyTypesQueryResult.md)

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

# **study_get_study_without_user_id_deprecated**
> GetStudyQueryResult study_get_study_without_user_id_deprecated(tenant_id, study_id, sim_version=sim_version)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
study_id = 'study_id_example' # str | 
sim_version = 'sim_version_example' # str |  (optional)

    try:
        api_response = api_instance.study_get_study_without_user_id_deprecated(tenant_id, study_id, sim_version=sim_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_without_user_id_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **study_id** | **str**|  | 
 **sim_version** | **str**|  | [optional] 

### Return type

[**GetStudyQueryResult**](GetStudyQueryResult.md)

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

# **study_get_tenant_access_information**
> GetTenantAccessInformationQueryResult study_get_tenant_access_information(tenant_id)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        api_response = api_instance.study_get_tenant_access_information(tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_tenant_access_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**GetTenantAccessInformationQueryResult**](GetTenantAccessInformationQueryResult.md)

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

# **study_get_tenant_billable_stored_simulation_count**
> GetTenantBillableStoredSimulationCountQueryResult study_get_tenant_billable_stored_simulation_count(tenant_id)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        api_response = api_instance.study_get_tenant_billable_stored_simulation_count(tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_tenant_billable_stored_simulation_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**GetTenantBillableStoredSimulationCountQueryResult**](GetTenantBillableStoredSimulationCountQueryResult.md)

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

# **study_get_tenant_study_statistics**
> GetTenantStudyStatisticsQueryResult study_get_tenant_study_statistics(tenant_id, start_date=start_date, end_date=end_date)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
start_date = 'start_date_example' # str |  (optional)
end_date = 'end_date_example' # str |  (optional)

    try:
        api_response = api_instance.study_get_tenant_study_statistics(tenant_id, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_tenant_study_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 

### Return type

[**GetTenantStudyStatisticsQueryResult**](GetTenantStudyStatisticsQueryResult.md)

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

# **study_merge_study**
> study_merge_study(tenant_id, study_id, force_merge_from_baseline=force_merge_from_baseline)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
study_id = 'study_id_example' # str | 
force_merge_from_baseline = False # bool |  (optional) (default to False)

    try:
        api_instance.study_merge_study(tenant_id, study_id, force_merge_from_baseline=force_merge_from_baseline)
    except ApiException as e:
        print("Exception when calling StudyApi->study_merge_study: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **study_id** | **str**|  | 
 **force_merge_from_baseline** | **bool**|  | [optional] [default to False]

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_merge_study_deprecated**
> study_merge_study_deprecated(tenant_id, user_id, study_id, force_merge_from_baseline=force_merge_from_baseline)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
study_id = 'study_id_example' # str | 
force_merge_from_baseline = False # bool |  (optional) (default to False)

    try:
        api_instance.study_merge_study_deprecated(tenant_id, user_id, study_id, force_merge_from_baseline=force_merge_from_baseline)
    except ApiException as e:
        print("Exception when calling StudyApi->study_merge_study_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **study_id** | **str**|  | 
 **force_merge_from_baseline** | **bool**|  | [optional] [default to False]

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_post_study**
> PostStudyResult study_post_study(tenant_id, study_post_study_request, run_inline=run_inline)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
study_post_study_request = canopy.openapi.StudyPostStudyRequest() # StudyPostStudyRequest | 
run_inline = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.study_post_study(tenant_id, study_post_study_request, run_inline=run_inline)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_post_study: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **study_post_study_request** | [**StudyPostStudyRequest**](StudyPostStudyRequest.md)|  | 
 **run_inline** | **bool**|  | [optional] [default to False]

### Return type

[**PostStudyResult**](PostStudyResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_post_study_deprecated**
> PostStudyResult study_post_study_deprecated(tenant_id, user_id, study_post_study_request, run_inline=run_inline)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
study_post_study_request = canopy.openapi.StudyPostStudyRequest() # StudyPostStudyRequest | 
run_inline = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.study_post_study_deprecated(tenant_id, user_id, study_post_study_request, run_inline=run_inline)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_post_study_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **study_post_study_request** | [**StudyPostStudyRequest**](StudyPostStudyRequest.md)|  | 
 **run_inline** | **bool**|  | [optional] [default to False]

### Return type

[**PostStudyResult**](PostStudyResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_put_study**
> study_put_study(tenant_id, study_id, study_put_study_request)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
study_id = 'study_id_example' # str | 
study_put_study_request = canopy.openapi.StudyPutStudyRequest() # StudyPutStudyRequest | 

    try:
        api_instance.study_put_study(tenant_id, study_id, study_put_study_request)
    except ApiException as e:
        print("Exception when calling StudyApi->study_put_study: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **study_id** | **str**|  | 
 **study_put_study_request** | [**StudyPutStudyRequest**](StudyPutStudyRequest.md)|  | 

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

# **study_put_study_deprecated**
> study_put_study_deprecated(tenant_id, user_id, study_id, study_put_study_request)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 
study_id = 'study_id_example' # str | 
study_put_study_request = canopy.openapi.StudyPutStudyRequest() # StudyPutStudyRequest | 

    try:
        api_instance.study_put_study_deprecated(tenant_id, user_id, study_id, study_put_study_request)
    except ApiException as e:
        print("Exception when calling StudyApi->study_put_study_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **user_id** | **str**|  | 
 **study_id** | **str**|  | 
 **study_put_study_request** | [**StudyPutStudyRequest**](StudyPutStudyRequest.md)|  | 

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

# **study_put_study_owner**
> study_put_study_owner(tenant_id, study_id, config_put_config_owner_request)



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
    api_instance = canopy.openapi.StudyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
study_id = 'study_id_example' # str | 
config_put_config_owner_request = canopy.openapi.ConfigPutConfigOwnerRequest() # ConfigPutConfigOwnerRequest | 

    try:
        api_instance.study_put_study_owner(tenant_id, study_id, config_put_config_owner_request)
    except ApiException as e:
        print("Exception when calling StudyApi->study_put_study_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **study_id** | **str**|  | 
 **config_put_config_owner_request** | [**ConfigPutConfigOwnerRequest**](ConfigPutConfigOwnerRequest.md)|  | 

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

