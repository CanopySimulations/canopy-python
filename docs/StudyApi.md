# canopy.openapi.StudyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**study_delete_study**](StudyApi.md#study_delete_study) | **DELETE** /studies/{tenantId}/{studyId} | Deletes a study. If the study is in progress it will be aborted, although this may not  immediately free up the nodes.
[**study_delete_study_deprecated**](StudyApi.md#study_delete_study_deprecated) | **DELETE** /studies/{tenantId}/{userId}/{studyId} | 
[**study_get_all_tenants_study_statistics**](StudyApi.md#study_get_all_tenants_study_statistics) | **GET** /studies/statistics | Returns study statistics for all tenants.
[**study_get_job_full_download**](StudyApi.md#study_get_job_full_download) | **GET** /studies/{tenantId}/{studyId}/jobs/{jobId}/download/full | Downloads complete job data as a ZIP file.  This includes all inputs and results for a specific job.
[**study_get_job_vector_download**](StudyApi.md#study_get_job_vector_download) | **GET** /studies/{tenantId}/{studyId}/jobs/{jobId}/download/vector/{simType} | Downloads job vector results for a specific simulation type as CSV.  This provides time-series data for the specified sim type.
[**study_get_sim_type**](StudyApi.md#study_get_sim_type) | **GET** /studies/types/sims/{simType} | Gets information about a specific sim type for a tenant.  This returns a subset of the data from the GetStudyTypes method.
[**study_get_studies**](StudyApi.md#study_get_studies) | **GET** /studies/{tenantId} | Gets the list of studies for a tenant. The results will be paged.
[**study_get_study**](StudyApi.md#study_get_study) | **GET** /studies/{tenantId}/{studyId} | Gets the specified study data. Note that this does not return the study results,  but it returns the access signatures necessary to download the results.  It also returns mapping from relevant tenant and user IDs to their names.
[**study_get_study_deprecated**](StudyApi.md#study_get_study_deprecated) | **GET** /studies/{tenantId}/{userId}/{studyId} | 
[**study_get_study_download**](StudyApi.md#study_get_study_download) | **GET** /studies/{tenantId}/{studyId}/download | Downloads a ZIP file containing the requested study data.  It primarily exists for use by web browsers, which can&#39;t provide the authentication  headers and so must pass in an access signature instead.  If you are using this API method outside of the web browser, there is probably a better way  to download the required data.  Note: For the fastest and most reliable way to download studies, look in the documentation  for \&quot;Download Tokens\&quot;.  This method, while more convenient than Download Tokens, can be unreliable for large studies  as any connection issues can result in a truncated download.  The URL containing the required access signature can be obtained using the GetStudyDownloadUrlAsync (&#x60;download-url&#x60;) method.  When downloading study results programmatically it is faster and more efficient to read the required data directly  from blob storage.
[**study_get_study_download_deprecated**](StudyApi.md#study_get_study_download_deprecated) | **GET** /studies/{tenantId}/{userId}/{studyId}/download | 
[**study_get_study_download_url**](StudyApi.md#study_get_study_download_url) | **GET** /studies/{tenantId}/{studyId}/download-url | Gets the access signature and expiry to enable the browser to download a study.  This works around the fact that browsers can&#39;t provide authentication headers when downloading.
[**study_get_study_download_url_deprecated**](StudyApi.md#study_get_study_download_url_deprecated) | **GET** /studies/{tenantId}/{userId}/{studyId}/download-url | 
[**study_get_study_full_download**](StudyApi.md#study_get_study_full_download) | **GET** /studies/{tenantId}/{studyId}/download/full | Downloads the complete study including all jobs and results as a ZIP file.  This is the recommended endpoint for downloading everything in a study.
[**study_get_study_job**](StudyApi.md#study_get_study_job) | **GET** /studies/{tenantId}/{studyId}/jobs/{jobId} | Gets a study job, including the inputs and a mapping of relevant tenant and user IDs to their names.
[**study_get_study_job_count**](StudyApi.md#study_get_study_job_count) | **POST** /studies/{tenantId}/jobs-count | Gets the Variations Count for a study without scheduling it.
[**study_get_study_job_deprecated**](StudyApi.md#study_get_study_job_deprecated) | **GET** /studies/{tenantId}/{userId}/{studyId}/jobs/{jobId} | 
[**study_get_study_job_download**](StudyApi.md#study_get_study_job_download) | **GET** /studies/{tenantId}/{studyId}/jobs/{jobId}/download | Downloads a ZIP file containing the requested study data.  This method primarily exists for use by web browsers, which can&#39;t provide the authentication  headers and so must pass in an access signature instead.  If you are using this API method outside of the web browser, there is probably a better way  to download the required data.  Note: For the fastest and most reliable way to download studies, look in the documentation  for \&quot;Download Tokens\&quot;.  This method, while more convenient than Download Tokens, can be unreliable for large studies  as any connection issues can result in a truncated download.  The URL containing the required access signature can be obtained using the GetStudyDownloadUrlAsync (&#x60;download-url&#x60;) method.  When downloading study results programmatically it is faster and more efficient to read the required data directly  from blob storage.
[**study_get_study_job_download_deprecated**](StudyApi.md#study_get_study_job_download_deprecated) | **GET** /studies/{tenantId}/{userId}/{studyId}/jobs/{jobId}/download | 
[**study_get_study_job_metadata**](StudyApi.md#study_get_study_job_metadata) | **GET** /studies/{tenantId}/{studyId}/jobs/{jobId}/metadata | Gets the metadata for a study job, which excludes certain information  such as the job inputs to keep the data smaller.
[**study_get_study_job_metadata_deprecated**](StudyApi.md#study_get_study_job_metadata_deprecated) | **GET** /studies/{tenantId}/{userId}/{studyId}/jobs/{jobId}/metadata | 
[**study_get_study_jobs**](StudyApi.md#study_get_study_jobs) | **GET** /studies/{tenantId}/{studyId}/jobs | Gets the list of study jobs for a study. The results may be paged.
[**study_get_study_jobs_deprecated**](StudyApi.md#study_get_study_jobs_deprecated) | **GET** /studies/{tenantId}/{userId}/{studyId}/jobs | 
[**study_get_study_merged_scalar_download**](StudyApi.md#study_get_study_merged_scalar_download) | **GET** /studies/{tenantId}/{studyId}/download/scalar/merged | Downloads merged scalar results as a single CSV file.  This contains all scalar results merged into one file by the post-processor.
[**study_get_study_metadata**](StudyApi.md#study_get_study_metadata) | **GET** /studies/{tenantId}/{studyId}/metadata | Gets the metadata for a study, which excludes certain information  such as the study definition to keep the data smaller.
[**study_get_study_metadata_deprecated**](StudyApi.md#study_get_study_metadata_deprecated) | **GET** /studies/{tenantId}/{userId}/{studyId}/metadata | 
[**study_get_study_metadata_without_user_id_deprecated**](StudyApi.md#study_get_study_metadata_without_user_id_deprecated) | **GET** /studies/{tenantId}/auto/{studyId}/metadata | 
[**study_get_study_scalar_download**](StudyApi.md#study_get_study_scalar_download) | **GET** /studies/{tenantId}/{studyId}/download/scalar | Downloads study scalar results as a ZIP file containing individual job results.  Use /download/scalar/merged for a single merged CSV file.
[**study_get_study_type**](StudyApi.md#study_get_study_type) | **GET** /studies/types/{studyType} | Gets a study type definition for a tenant.
[**study_get_study_types**](StudyApi.md#study_get_study_types) | **GET** /studies/types | Gets the study type information for a specific tenant.  This method also returns information about the simulations and config types  which are indirectly available to the tenant through their set of  study types.
[**study_get_study_without_user_id_deprecated**](StudyApi.md#study_get_study_without_user_id_deprecated) | **GET** /studies/{tenantId}/auto/{studyId} | 
[**study_get_tenant_access_information**](StudyApi.md#study_get_tenant_access_information) | **GET** /studies/{tenantId}/access | Gets the URL and shared access signature for a tenant&#39;s primary blob storage container.
[**study_get_tenant_billable_stored_simulation_count**](StudyApi.md#study_get_tenant_billable_stored_simulation_count) | **GET** /studies/statistics/stored/{tenantId} | Gets the number of billable stored simulations for a tenant.
[**study_get_tenant_study_statistics**](StudyApi.md#study_get_tenant_study_statistics) | **GET** /studies/statistics/{tenantId} | Returns the study statistics for a tenant.
[**study_merge_study**](StudyApi.md#study_merge_study) | **PATCH** /studies/{tenantId}/{studyId}/merge | Merges a study baseline definition into the main study document.  This is used by Canopy personnel only.
[**study_merge_study_deprecated**](StudyApi.md#study_merge_study_deprecated) | **PATCH** /studies/{tenantId}/{userId}/{studyId}/merge | 
[**study_post_study**](StudyApi.md#study_post_study) | **POST** /studies/{tenantId} | Creates a new study which will be scheduled to run on the platform.  The study will not be complete when this method returns, but you can  use the returned Study ID to poll the status of the study.
[**study_post_study_deprecated**](StudyApi.md#study_post_study_deprecated) | **POST** /studies/{tenantId}/{userId} | 
[**study_put_study**](StudyApi.md#study_put_study) | **PUT** /studies/{tenantId}/{studyId} | Updates a previously created study.  This can be used to rename a study, or to add custom properties or notes.  If any data isn&#39;t provided then it will be removed from the study.
[**study_put_study_deprecated**](StudyApi.md#study_put_study_deprecated) | **PUT** /studies/{tenantId}/{userId}/{studyId} | 
[**study_put_study_owner**](StudyApi.md#study_put_study_owner) | **PUT** /studies/{tenantId}/{studyId}/owner | Changes the owner of a study. This can be called while the study is still in progress.
[**study_put_study_priority**](StudyApi.md#study_put_study_priority) | **PUT** /studies/{tenantId}/{studyId}/priority | Set the highest priority for a running study.


# **study_delete_study**
> study_delete_study(tenant_id, study_id, undelete=undelete)

Deletes a study. If the study is in progress it will be aborted, although this may not  immediately free up the nodes.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.
study_id = 'study_id_example' # str | The study ID.
undelete = False # bool | Whether the study should be deleted or undeleted. (optional) (default to False)

    try:
        # Deletes a study. If the study is in progress it will be aborted, although this may not  immediately free up the nodes.
        api_instance.study_delete_study(tenant_id, study_id, undelete=undelete)
    except ApiException as e:
        print("Exception when calling StudyApi->study_delete_study: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 
 **study_id** | **str**| The study ID. | 
 **undelete** | **bool**| Whether the study should be deleted or undeleted. | [optional] [default to False]

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_get_all_tenants_study_statistics**
> GetAllTenantsStudyStatisticsQueryResult study_get_all_tenants_study_statistics(start_date=start_date, end_date=end_date)

Returns study statistics for all tenants.

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
    start_date = 'start_date_example' # str | The start date for the range of the statistics. (optional)
end_date = 'end_date_example' # str | The end date for the range of the statistics. (optional)

    try:
        # Returns study statistics for all tenants.
        api_response = api_instance.study_get_all_tenants_study_statistics(start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_all_tenants_study_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| The start date for the range of the statistics. | [optional] 
 **end_date** | **str**| The end date for the range of the statistics. | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_get_job_full_download**
> study_get_job_full_download(tenant_id, study_id, job_id, access_signature, expiry, file_name=file_name, channels_as_csv=channels_as_csv)

Downloads complete job data as a ZIP file.  This includes all inputs and results for a specific job.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID of the study.
study_id = 'study_id_example' # str | The study ID.
job_id = 'job_id_example' # str | The job ID.
access_signature = 'access_signature_example' # str | The access signature provided by the `download-url` method.
expiry = 'expiry_example' # str | The access signature expiry.
file_name = 'file_name_example' # str | The preferred file name. (optional)
channels_as_csv = False # bool | Whether to convert the vector channel data to CSV files from individual binary files. (optional) (default to False)

    try:
        # Downloads complete job data as a ZIP file.  This includes all inputs and results for a specific job.
        api_instance.study_get_job_full_download(tenant_id, study_id, job_id, access_signature, expiry, file_name=file_name, channels_as_csv=channels_as_csv)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_job_full_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID of the study. | 
 **study_id** | **str**| The study ID. | 
 **job_id** | **str**| The job ID. | 
 **access_signature** | **str**| The access signature provided by the &#x60;download-url&#x60; method. | 
 **expiry** | **str**| The access signature expiry. | 
 **file_name** | **str**| The preferred file name. | [optional] 
 **channels_as_csv** | **bool**| Whether to convert the vector channel data to CSV files from individual binary files. | [optional] [default to False]

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

# **study_get_job_vector_download**
> study_get_job_vector_download(tenant_id, study_id, job_id, sim_type, access_signature, expiry, file_name=file_name, x_domain=x_domain)

Downloads job vector results for a specific simulation type as CSV.  This provides time-series data for the specified sim type.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID of the study.
study_id = 'study_id_example' # str | The study ID.
job_id = 'job_id_example' # str | The job ID.
sim_type = 'sim_type_example' # str | The simulation type (e.g., \"DynamicLap\", \"StraightLine\").
access_signature = 'access_signature_example' # str | The access signature provided by the `download-url` method.
expiry = 'expiry_example' # str | The access signature expiry.
file_name = 'file_name_example' # str | The preferred file name. (optional)
x_domain = 'x_domain_example' # str | The xDomain to filter vector results by. If null or empty, all xDomains are included. (optional)

    try:
        # Downloads job vector results for a specific simulation type as CSV.  This provides time-series data for the specified sim type.
        api_instance.study_get_job_vector_download(tenant_id, study_id, job_id, sim_type, access_signature, expiry, file_name=file_name, x_domain=x_domain)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_job_vector_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID of the study. | 
 **study_id** | **str**| The study ID. | 
 **job_id** | **str**| The job ID. | 
 **sim_type** | **str**| The simulation type (e.g., \&quot;DynamicLap\&quot;, \&quot;StraightLine\&quot;). | 
 **access_signature** | **str**| The access signature provided by the &#x60;download-url&#x60; method. | 
 **expiry** | **str**| The access signature expiry. | 
 **file_name** | **str**| The preferred file name. | [optional] 
 **x_domain** | **str**| The xDomain to filter vector results by. If null or empty, all xDomains are included. | [optional] 

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

# **study_get_sim_type**
> SimTypeDefinition study_get_sim_type(sim_type, tenant_id=tenant_id)

Gets information about a specific sim type for a tenant.  This returns a subset of the data from the GetStudyTypes method.

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
    sim_type = 'sim_type_example' # str | The sim type whose data should be returned.
tenant_id = 'tenant_id_example' # str | The tenant ID. (optional)

    try:
        # Gets information about a specific sim type for a tenant.  This returns a subset of the data from the GetStudyTypes method.
        api_response = api_instance.study_get_sim_type(sim_type, tenant_id=tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_sim_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_type** | **str**| The sim type whose data should be returned. | 
 **tenant_id** | **str**| The tenant ID. | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_get_studies**
> GetStudiesQueryResult study_get_studies(tenant_id, filter=filter, include_transient=include_transient, result_type=result_type)

Gets the list of studies for a tenant. The results will be paged.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.
filter = 'filter_example' # str | The filter. This should be a JSON serialized Canopy.Api.Controllers.Simulations.ListFilterData. (optional)
include_transient = False # bool | Whether transient studies (such as Verify Car) should be included. (optional) (default to False)
result_type = 'result_type_example' # str | The result type. This can be `queryOnly` (return the list of studies),  `groupOnly` (return the groups which can be used for further filtering and sorting),  or `all` (return both the list of studies and the groups). (optional)

    try:
        # Gets the list of studies for a tenant. The results will be paged.
        api_response = api_instance.study_get_studies(tenant_id, filter=filter, include_transient=include_transient, result_type=result_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_studies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 
 **filter** | **str**| The filter. This should be a JSON serialized Canopy.Api.Controllers.Simulations.ListFilterData. | [optional] 
 **include_transient** | **bool**| Whether transient studies (such as Verify Car) should be included. | [optional] [default to False]
 **result_type** | **str**| The result type. This can be &#x60;queryOnly&#x60; (return the list of studies),  &#x60;groupOnly&#x60; (return the groups which can be used for further filtering and sorting),  or &#x60;all&#x60; (return both the list of studies and the groups). | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_get_study**
> GetStudyQueryResult study_get_study(tenant_id, study_id, sim_version=sim_version)

Gets the specified study data. Note that this does not return the study results,  but it returns the access signatures necessary to download the results.  It also returns mapping from relevant tenant and user IDs to their names.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.
study_id = 'study_id_example' # str | The study ID.
sim_version = 'sim_version_example' # str | The required sim version.  This will upgrade or downgrade the study definition to conform to  the specified sim version. (optional)

    try:
        # Gets the specified study data. Note that this does not return the study results,  but it returns the access signatures necessary to download the results.  It also returns mapping from relevant tenant and user IDs to their names.
        api_response = api_instance.study_get_study(tenant_id, study_id, sim_version=sim_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 
 **study_id** | **str**| The study ID. | 
 **sim_version** | **str**| The required sim version.  This will upgrade or downgrade the study definition to conform to  the specified sim version. | [optional] 

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
**200** | OK |  -  |

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_get_study_download**
> study_get_study_download(tenant_id, study_id, access_signature, expiry, file_name=file_name, full=full, channels_as_csv=channels_as_csv, merged_scalar_results_only=merged_scalar_results_only)

Downloads a ZIP file containing the requested study data.  It primarily exists for use by web browsers, which can't provide the authentication  headers and so must pass in an access signature instead.  If you are using this API method outside of the web browser, there is probably a better way  to download the required data.  Note: For the fastest and most reliable way to download studies, look in the documentation  for \"Download Tokens\".  This method, while more convenient than Download Tokens, can be unreliable for large studies  as any connection issues can result in a truncated download.  The URL containing the required access signature can be obtained using the GetStudyDownloadUrlAsync (`download-url`) method.  When downloading study results programmatically it is faster and more efficient to read the required data directly  from blob storage.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID of the study.
study_id = 'study_id_example' # str | The study ID.
access_signature = 'access_signature_example' # str | The access signature provided by the `download-url` method.
expiry = 'expiry_example' # str | The access signature expiry.
file_name = 'file_name_example' # str | The preferred file name. (optional)
full = False # bool | Whether to download the full study. (optional) (default to False)
channels_as_csv = False # bool | Whether to convert the vector channel data to CSV files from individual binary files. (optional) (default to False)
merged_scalar_results_only = False # bool | Whether to only download the merged scalar results. (optional) (default to False)

    try:
        # Downloads a ZIP file containing the requested study data.  It primarily exists for use by web browsers, which can't provide the authentication  headers and so must pass in an access signature instead.  If you are using this API method outside of the web browser, there is probably a better way  to download the required data.  Note: For the fastest and most reliable way to download studies, look in the documentation  for \"Download Tokens\".  This method, while more convenient than Download Tokens, can be unreliable for large studies  as any connection issues can result in a truncated download.  The URL containing the required access signature can be obtained using the GetStudyDownloadUrlAsync (`download-url`) method.  When downloading study results programmatically it is faster and more efficient to read the required data directly  from blob storage.
        api_instance.study_get_study_download(tenant_id, study_id, access_signature, expiry, file_name=file_name, full=full, channels_as_csv=channels_as_csv, merged_scalar_results_only=merged_scalar_results_only)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID of the study. | 
 **study_id** | **str**| The study ID. | 
 **access_signature** | **str**| The access signature provided by the &#x60;download-url&#x60; method. | 
 **expiry** | **str**| The access signature expiry. | 
 **file_name** | **str**| The preferred file name. | [optional] 
 **full** | **bool**| Whether to download the full study. | [optional] [default to False]
 **channels_as_csv** | **bool**| Whether to convert the vector channel data to CSV files from individual binary files. | [optional] [default to False]
 **merged_scalar_results_only** | **bool**| Whether to only download the merged scalar results. | [optional] [default to False]

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_get_study_download_url**
> GetStudyDownloadUrlQueryResult study_get_study_download_url(tenant_id, study_id)

Gets the access signature and expiry to enable the browser to download a study.  This works around the fact that browsers can't provide authentication headers when downloading.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.
study_id = 'study_id_example' # str | The study ID.

    try:
        # Gets the access signature and expiry to enable the browser to download a study.  This works around the fact that browsers can't provide authentication headers when downloading.
        api_response = api_instance.study_get_study_download_url(tenant_id, study_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_download_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 
 **study_id** | **str**| The study ID. | 

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
**200** | OK |  -  |

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_get_study_full_download**
> study_get_study_full_download(tenant_id, study_id, access_signature, expiry, file_name=file_name, channels_as_csv=channels_as_csv)

Downloads the complete study including all jobs and results as a ZIP file.  This is the recommended endpoint for downloading everything in a study.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID of the study.
study_id = 'study_id_example' # str | The study ID.
access_signature = 'access_signature_example' # str | The access signature provided by the `download-url` method.
expiry = 'expiry_example' # str | The access signature expiry.
file_name = 'file_name_example' # str | The preferred file name. (optional)
channels_as_csv = False # bool | Whether to convert the vector channel data to CSV files from individual binary files. (optional) (default to False)

    try:
        # Downloads the complete study including all jobs and results as a ZIP file.  This is the recommended endpoint for downloading everything in a study.
        api_instance.study_get_study_full_download(tenant_id, study_id, access_signature, expiry, file_name=file_name, channels_as_csv=channels_as_csv)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_full_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID of the study. | 
 **study_id** | **str**| The study ID. | 
 **access_signature** | **str**| The access signature provided by the &#x60;download-url&#x60; method. | 
 **expiry** | **str**| The access signature expiry. | 
 **file_name** | **str**| The preferred file name. | [optional] 
 **channels_as_csv** | **bool**| Whether to convert the vector channel data to CSV files from individual binary files. | [optional] [default to False]

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

# **study_get_study_job**
> GetStudyJobQueryResult study_get_study_job(tenant_id, study_id, job_id, sim_version=sim_version)

Gets a study job, including the inputs and a mapping of relevant tenant and user IDs to their names.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.
study_id = 'study_id_example' # str | The study ID.
job_id = 'job_id_example' # str | The job ID.
sim_version = 'sim_version_example' # str | The required sim version. The job inputs will be upgraded or downgraded to this version if necessary. (optional)

    try:
        # Gets a study job, including the inputs and a mapping of relevant tenant and user IDs to their names.
        api_response = api_instance.study_get_study_job(tenant_id, study_id, job_id, sim_version=sim_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 
 **study_id** | **str**| The study ID. | 
 **job_id** | **str**| The job ID. | 
 **sim_version** | **str**| The required sim version. The job inputs will be upgraded or downgraded to this version if necessary. | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_get_study_job_count**
> GetStudyJobCountResult study_get_study_job_count(tenant_id, study_post_study_request)

Gets the Variations Count for a study without scheduling it.

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
    tenant_id = 'tenant_id_example' # str | The id of the tenant.
study_post_study_request = canopy.openapi.StudyPostStudyRequest() # StudyPostStudyRequest | The data representing the new study.

    try:
        # Gets the Variations Count for a study without scheduling it.
        api_response = api_instance.study_get_study_job_count(tenant_id, study_post_study_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_job_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The id of the tenant. | 
 **study_post_study_request** | [**StudyPostStudyRequest**](StudyPostStudyRequest.md)| The data representing the new study. | 

### Return type

[**GetStudyJobCountResult**](GetStudyJobCountResult.md)

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_get_study_job_download**
> study_get_study_job_download(tenant_id, study_id, job_id, access_signature, expiry, file_name=file_name, channels_as_csv=channels_as_csv, sim_type_channels=sim_type_channels, x_domain=x_domain)

Downloads a ZIP file containing the requested study data.  This method primarily exists for use by web browsers, which can't provide the authentication  headers and so must pass in an access signature instead.  If you are using this API method outside of the web browser, there is probably a better way  to download the required data.  Note: For the fastest and most reliable way to download studies, look in the documentation  for \"Download Tokens\".  This method, while more convenient than Download Tokens, can be unreliable for large studies  as any connection issues can result in a truncated download.  The URL containing the required access signature can be obtained using the GetStudyDownloadUrlAsync (`download-url`) method.  When downloading study results programmatically it is faster and more efficient to read the required data directly  from blob storage.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID of the study.
study_id = 'study_id_example' # str | The study ID.
job_id = 'job_id_example' # str | The job ID.
access_signature = 'access_signature_example' # str | The access signature provided by the `download-url` method.
expiry = 'expiry_example' # str | The access signature expiry.
file_name = 'file_name_example' # str | The preferred file name. (optional)
channels_as_csv = False # bool | Whether to convert the vector channel data to CSV files from individual binary files. (optional) (default to False)
sim_type_channels = 'sim_type_channels_example' # str | The sim type to download channels for. (optional)
x_domain = 'x_domain_example' # str | The xDomain to filter vector results by. If null or empty, all xDomains are included. (optional)

    try:
        # Downloads a ZIP file containing the requested study data.  This method primarily exists for use by web browsers, which can't provide the authentication  headers and so must pass in an access signature instead.  If you are using this API method outside of the web browser, there is probably a better way  to download the required data.  Note: For the fastest and most reliable way to download studies, look in the documentation  for \"Download Tokens\".  This method, while more convenient than Download Tokens, can be unreliable for large studies  as any connection issues can result in a truncated download.  The URL containing the required access signature can be obtained using the GetStudyDownloadUrlAsync (`download-url`) method.  When downloading study results programmatically it is faster and more efficient to read the required data directly  from blob storage.
        api_instance.study_get_study_job_download(tenant_id, study_id, job_id, access_signature, expiry, file_name=file_name, channels_as_csv=channels_as_csv, sim_type_channels=sim_type_channels, x_domain=x_domain)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_job_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID of the study. | 
 **study_id** | **str**| The study ID. | 
 **job_id** | **str**| The job ID. | 
 **access_signature** | **str**| The access signature provided by the &#x60;download-url&#x60; method. | 
 **expiry** | **str**| The access signature expiry. | 
 **file_name** | **str**| The preferred file name. | [optional] 
 **channels_as_csv** | **bool**| Whether to convert the vector channel data to CSV files from individual binary files. | [optional] [default to False]
 **sim_type_channels** | **str**| The sim type to download channels for. | [optional] 
 **x_domain** | **str**| The xDomain to filter vector results by. If null or empty, all xDomains are included. | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_get_study_job_metadata**
> GetStudyJobMetadataQueryResult study_get_study_job_metadata(tenant_id, study_id, job_id)

Gets the metadata for a study job, which excludes certain information  such as the job inputs to keep the data smaller.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID of the study.
study_id = 'study_id_example' # str | The study ID.
job_id = 'job_id_example' # str | The job ID.

    try:
        # Gets the metadata for a study job, which excludes certain information  such as the job inputs to keep the data smaller.
        api_response = api_instance.study_get_study_job_metadata(tenant_id, study_id, job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_job_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID of the study. | 
 **study_id** | **str**| The study ID. | 
 **job_id** | **str**| The job ID. | 

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
**200** | OK |  -  |

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_get_study_jobs**
> GetStudyJobsQueryResult study_get_study_jobs(tenant_id, study_id, filter=filter)

Gets the list of study jobs for a study. The results may be paged.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID of the study.
study_id = 'study_id_example' # str | The study ID.
filter = 'filter_example' # str | The JSON serialized filter data. (optional)

    try:
        # Gets the list of study jobs for a study. The results may be paged.
        api_response = api_instance.study_get_study_jobs(tenant_id, study_id, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID of the study. | 
 **study_id** | **str**| The study ID. | 
 **filter** | **str**| The JSON serialized filter data. | [optional] 

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
**200** | OK |  -  |

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_get_study_merged_scalar_download**
> study_get_study_merged_scalar_download(tenant_id, study_id, access_signature, expiry, file_name=file_name)

Downloads merged scalar results as a single CSV file.  This contains all scalar results merged into one file by the post-processor.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID of the study.
study_id = 'study_id_example' # str | The study ID.
access_signature = 'access_signature_example' # str | The access signature provided by the `download-url` method.
expiry = 'expiry_example' # str | The access signature expiry.
file_name = 'file_name_example' # str | The preferred file name. (optional)

    try:
        # Downloads merged scalar results as a single CSV file.  This contains all scalar results merged into one file by the post-processor.
        api_instance.study_get_study_merged_scalar_download(tenant_id, study_id, access_signature, expiry, file_name=file_name)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_merged_scalar_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID of the study. | 
 **study_id** | **str**| The study ID. | 
 **access_signature** | **str**| The access signature provided by the &#x60;download-url&#x60; method. | 
 **expiry** | **str**| The access signature expiry. | 
 **file_name** | **str**| The preferred file name. | [optional] 

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

# **study_get_study_metadata**
> GetStudyQueryResult study_get_study_metadata(tenant_id, study_id)

Gets the metadata for a study, which excludes certain information  such as the study definition to keep the data smaller.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.
study_id = 'study_id_example' # str | The study ID.

    try:
        # Gets the metadata for a study, which excludes certain information  such as the study definition to keep the data smaller.
        api_response = api_instance.study_get_study_metadata(tenant_id, study_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 
 **study_id** | **str**| The study ID. | 

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
**200** | OK |  -  |

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
**200** | OK |  -  |

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_get_study_scalar_download**
> study_get_study_scalar_download(tenant_id, study_id, access_signature, expiry, file_name=file_name)

Downloads study scalar results as a ZIP file containing individual job results.  Use /download/scalar/merged for a single merged CSV file.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID of the study.
study_id = 'study_id_example' # str | The study ID.
access_signature = 'access_signature_example' # str | The access signature provided by the `download-url` method.
expiry = 'expiry_example' # str | The access signature expiry.
file_name = 'file_name_example' # str | The preferred file name. (optional)

    try:
        # Downloads study scalar results as a ZIP file containing individual job results.  Use /download/scalar/merged for a single merged CSV file.
        api_instance.study_get_study_scalar_download(tenant_id, study_id, access_signature, expiry, file_name=file_name)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_scalar_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID of the study. | 
 **study_id** | **str**| The study ID. | 
 **access_signature** | **str**| The access signature provided by the &#x60;download-url&#x60; method. | 
 **expiry** | **str**| The access signature expiry. | 
 **file_name** | **str**| The preferred file name. | [optional] 

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

# **study_get_study_type**
> StudyTypeDefinition study_get_study_type(study_type, tenant_id=tenant_id)

Gets a study type definition for a tenant.

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
    study_type = 'study_type_example' # str | The study type.
tenant_id = 'tenant_id_example' # str | The tenant ID. (optional)

    try:
        # Gets a study type definition for a tenant.
        api_response = api_instance.study_get_study_type(study_type, tenant_id=tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_type** | **str**| The study type. | 
 **tenant_id** | **str**| The tenant ID. | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_get_study_types**
> GetStudyTypesQueryResult study_get_study_types(tenant_id=tenant_id)

Gets the study type information for a specific tenant.  This method also returns information about the simulations and config types  which are indirectly available to the tenant through their set of  study types.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID. (optional)

    try:
        # Gets the study type information for a specific tenant.  This method also returns information about the simulations and config types  which are indirectly available to the tenant through their set of  study types.
        api_response = api_instance.study_get_study_types(tenant_id=tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_study_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | [optional] 

### Return type

[**GetStudyTypesQueryResult**](GetStudyTypesQueryResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_get_tenant_access_information**
> GetTenantAccessInformationQueryResult study_get_tenant_access_information(tenant_id)

Gets the URL and shared access signature for a tenant's primary blob storage container.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.

    try:
        # Gets the URL and shared access signature for a tenant's primary blob storage container.
        api_response = api_instance.study_get_tenant_access_information(tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_tenant_access_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_get_tenant_billable_stored_simulation_count**
> GetTenantBillableStoredSimulationCountQueryResult study_get_tenant_billable_stored_simulation_count(tenant_id)

Gets the number of billable stored simulations for a tenant.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.

    try:
        # Gets the number of billable stored simulations for a tenant.
        api_response = api_instance.study_get_tenant_billable_stored_simulation_count(tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_tenant_billable_stored_simulation_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_get_tenant_study_statistics**
> GetTenantStudyStatisticsQueryResult study_get_tenant_study_statistics(tenant_id, start_date=start_date, end_date=end_date)

Returns the study statistics for a tenant.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.
start_date = 'start_date_example' # str | The start date for the range of the statistics. (optional)
end_date = 'end_date_example' # str | The end date for the range of the statistics. (optional)

    try:
        # Returns the study statistics for a tenant.
        api_response = api_instance.study_get_tenant_study_statistics(tenant_id, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_get_tenant_study_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 
 **start_date** | **str**| The start date for the range of the statistics. | [optional] 
 **end_date** | **str**| The end date for the range of the statistics. | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_merge_study**
> study_merge_study(tenant_id, study_id, force_merge_from_baseline=force_merge_from_baseline)

Merges a study baseline definition into the main study document.  This is used by Canopy personnel only.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.
study_id = 'study_id_example' # str | The study ID.
force_merge_from_baseline = False # bool | Whether to force merging from the baseline, even if not necessary. (optional) (default to False)

    try:
        # Merges a study baseline definition into the main study document.  This is used by Canopy personnel only.
        api_instance.study_merge_study(tenant_id, study_id, force_merge_from_baseline=force_merge_from_baseline)
    except ApiException as e:
        print("Exception when calling StudyApi->study_merge_study: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 
 **study_id** | **str**| The study ID. | 
 **force_merge_from_baseline** | **bool**| Whether to force merging from the baseline, even if not necessary. | [optional] [default to False]

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_post_study**
> PostStudyResult study_post_study(tenant_id, study_post_study_request, run_inline=run_inline)

Creates a new study which will be scheduled to run on the platform.  The study will not be complete when this method returns, but you can  use the returned Study ID to poll the status of the study.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.
study_post_study_request = canopy.openapi.StudyPostStudyRequest() # StudyPostStudyRequest | The data representing the new study.
run_inline = False # bool | Whether to run the study inline. Inline studies are no longer supported. (optional) (default to False)

    try:
        # Creates a new study which will be scheduled to run on the platform.  The study will not be complete when this method returns, but you can  use the returned Study ID to poll the status of the study.
        api_response = api_instance.study_post_study(tenant_id, study_post_study_request, run_inline=run_inline)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudyApi->study_post_study: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 
 **study_post_study_request** | [**StudyPostStudyRequest**](StudyPostStudyRequest.md)| The data representing the new study. | 
 **run_inline** | **bool**| Whether to run the study inline. Inline studies are no longer supported. | [optional] [default to False]

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
**200** | OK |  -  |

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_put_study**
> study_put_study(tenant_id, study_id, study_put_study_request)

Updates a previously created study.  This can be used to rename a study, or to add custom properties or notes.  If any data isn't provided then it will be removed from the study.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.
study_id = 'study_id_example' # str | The study ID.
study_put_study_request = canopy.openapi.StudyPutStudyRequest() # StudyPutStudyRequest | The updated study data.

    try:
        # Updates a previously created study.  This can be used to rename a study, or to add custom properties or notes.  If any data isn't provided then it will be removed from the study.
        api_instance.study_put_study(tenant_id, study_id, study_put_study_request)
    except ApiException as e:
        print("Exception when calling StudyApi->study_put_study: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 
 **study_id** | **str**| The study ID. | 
 **study_put_study_request** | [**StudyPutStudyRequest**](StudyPutStudyRequest.md)| The updated study data. | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_put_study_owner**
> study_put_study_owner(tenant_id, study_id, config_put_config_owner_request)

Changes the owner of a study. This can be called while the study is still in progress.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.
study_id = 'study_id_example' # str | The study ID.
config_put_config_owner_request = canopy.openapi.ConfigPutConfigOwnerRequest() # ConfigPutConfigOwnerRequest | The new study owner.

    try:
        # Changes the owner of a study. This can be called while the study is still in progress.
        api_instance.study_put_study_owner(tenant_id, study_id, config_put_config_owner_request)
    except ApiException as e:
        print("Exception when calling StudyApi->study_put_study_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 
 **study_id** | **str**| The study ID. | 
 **config_put_config_owner_request** | [**ConfigPutConfigOwnerRequest**](ConfigPutConfigOwnerRequest.md)| The new study owner. | 

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

# **study_put_study_priority**
> study_put_study_priority(tenant_id, study_id, body)

Set the highest priority for a running study.

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
    tenant_id = 'tenant_id_example' # str | The tenant ID.
study_id = 'study_id_example' # str | The study ID.
body = 56 # int | The priority.

    try:
        # Set the highest priority for a running study.
        api_instance.study_put_study_priority(tenant_id, study_id, body)
    except ApiException as e:
        print("Exception when calling StudyApi->study_put_study_priority: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant ID. | 
 **study_id** | **str**| The study ID. | 
 **body** | **int**| The priority. | 

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

