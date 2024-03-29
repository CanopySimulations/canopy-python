# canopy.openapi
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonLegacyClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import canopy.openapi
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import canopy.openapi
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    api_instance = canopy.openapi.AccountSettingsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
user_id = 'user_id_example' # str | 

    try:
        api_response = api_instance.account_settings_get(tenant_id, user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountSettingsApi->account_settings_get: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountSettingsApi* | [**account_settings_get**](docs/AccountSettingsApi.md#account_settings_get) | **GET** /account-settings/{tenantId}/{userId} | 
*AccountSettingsApi* | [**account_settings_put**](docs/AccountSettingsApi.md#account_settings_put) | **PUT** /account-settings/{tenantId}/{userId} | 
*AvailabilityApi* | [**availability_get**](docs/AvailabilityApi.md#availability_get) | **GET** /availability | 
*AvailabilityApi* | [**availability_head**](docs/AvailabilityApi.md#availability_head) | **HEAD** /availability | 
*ConfigApi* | [**config_decrypt**](docs/ConfigApi.md#config_decrypt) | **POST** /configs/decrypt | 
*ConfigApi* | [**config_decrypt_with_metadata**](docs/ConfigApi.md#config_decrypt_with_metadata) | **POST** /configs/decryptWithMetadata | 
*ConfigApi* | [**config_delete_config**](docs/ConfigApi.md#config_delete_config) | **DELETE** /configs/{tenantId}/{configId} | 
*ConfigApi* | [**config_delete_config_deprecated**](docs/ConfigApi.md#config_delete_config_deprecated) | **DELETE** /configs/{tenantId}/{userId}/{configId} | 
*ConfigApi* | [**config_encrypt**](docs/ConfigApi.md#config_encrypt) | **POST** /configs/encrypt | 
*ConfigApi* | [**config_encrypt_with_metadata**](docs/ConfigApi.md#config_encrypt_with_metadata) | **POST** /configs/encryptWithMetadata | 
*ConfigApi* | [**config_get_config**](docs/ConfigApi.md#config_get_config) | **GET** /configs/{tenantId}/{configId} | 
*ConfigApi* | [**config_get_config_deprecated**](docs/ConfigApi.md#config_get_config_deprecated) | **GET** /configs/{tenantId}/{userId}/{configId} | 
*ConfigApi* | [**config_get_config_names**](docs/ConfigApi.md#config_get_config_names) | **GET** /configs/{tenantId}/names | 
*ConfigApi* | [**config_get_config_versions**](docs/ConfigApi.md#config_get_config_versions) | **GET** /configs/{tenantId}/{configId}/versions | 
*ConfigApi* | [**config_get_config_versions_deprecated**](docs/ConfigApi.md#config_get_config_versions_deprecated) | **GET** /configs/{tenantId}/{userId}/{configId}/versions | 
*ConfigApi* | [**config_get_config_without_user_id_deprecated**](docs/ConfigApi.md#config_get_config_without_user_id_deprecated) | **GET** /configs/{tenantId}/auto/{configId} | 
*ConfigApi* | [**config_get_configs**](docs/ConfigApi.md#config_get_configs) | **GET** /configs/{tenantId} | 
*ConfigApi* | [**config_post_config**](docs/ConfigApi.md#config_post_config) | **POST** /configs/{tenantId} | 
*ConfigApi* | [**config_post_config_deprecated**](docs/ConfigApi.md#config_post_config_deprecated) | **POST** /configs/{tenantId}/{userId} | 
*ConfigApi* | [**config_post_configs**](docs/ConfigApi.md#config_post_configs) | **POST** /configs/{tenantId}/batch | 
*ConfigApi* | [**config_post_configs_deprecated**](docs/ConfigApi.md#config_post_configs_deprecated) | **POST** /configs/{tenantId}/{userId}/batch | 
*ConfigApi* | [**config_put_config**](docs/ConfigApi.md#config_put_config) | **PUT** /configs/{tenantId}/{configId} | 
*ConfigApi* | [**config_put_config_deprecated**](docs/ConfigApi.md#config_put_config_deprecated) | **PUT** /configs/{tenantId}/{userId}/{configId} | 
*ConfigApi* | [**config_put_config_owner**](docs/ConfigApi.md#config_put_config_owner) | **PUT** /configs/{tenantId}/{configId}/owner | 
*ConfigApi* | [**config_upgrade_config**](docs/ConfigApi.md#config_upgrade_config) | **POST** /configs/upgrade/{tenantId}/{targetSimVersion} | 
*ConfigApi* | [**config_upgrade_config_deprecated**](docs/ConfigApi.md#config_upgrade_config_deprecated) | **POST** /configs/upgrade/{targetSimVersion} | 
*EndToEndTestInboxApi* | [**end_to_end_test_inbox_get_latest_message_and_clear_mailbox**](docs/EndToEndTestInboxApi.md#end_to_end_test_inbox_get_latest_message_and_clear_mailbox) | **GET** /test-mailboxes/{mailboxName} | 
*ListFilterApi* | [**list_filter_upgrade_list_filter**](docs/ListFilterApi.md#list_filter_upgrade_list_filter) | **GET** /list-filters/upgrade | 
*MembershipApi* | [**membership_delete_refresh_tokens**](docs/MembershipApi.md#membership_delete_refresh_tokens) | **DELETE** /membership/refresh-tokens/{tenantId}/{userId} | 
*MembershipApi* | [**membership_get_password_reset_token_validity**](docs/MembershipApi.md#membership_get_password_reset_token_validity) | **GET** /membership/password-reset-tokens/{userId} | 
*MembershipApi* | [**membership_get_upvoty_token**](docs/MembershipApi.md#membership_get_upvoty_token) | **GET** /membership/upvoty-token/{tenantId}/{userId} | 
*MembershipApi* | [**membership_get_user_roles**](docs/MembershipApi.md#membership_get_user_roles) | **GET** /membership/roles/{tenantId}/{userId} | 
*MembershipApi* | [**membership_get_zendesk_token**](docs/MembershipApi.md#membership_get_zendesk_token) | **GET** /membership/zendesk-token/{tenantId}/{userId} | 
*MembershipApi* | [**membership_post_email_confirmation**](docs/MembershipApi.md#membership_post_email_confirmation) | **POST** /membership/email-confirmations | 
*MembershipApi* | [**membership_post_email_confirmation_request**](docs/MembershipApi.md#membership_post_email_confirmation_request) | **POST** /membership/email-confirmation-requests/{tenantId}/{userId} | 
*MembershipApi* | [**membership_post_identified_user**](docs/MembershipApi.md#membership_post_identified_user) | **POST** /membership/identified-users | 
*MembershipApi* | [**membership_post_initialize**](docs/MembershipApi.md#membership_post_initialize) | **POST** /membership/initialize | 
*MembershipApi* | [**membership_post_password_reset_confirmation**](docs/MembershipApi.md#membership_post_password_reset_confirmation) | **POST** /membership/password-reset-confirmations | 
*MembershipApi* | [**membership_post_password_reset_request**](docs/MembershipApi.md#membership_post_password_reset_request) | **POST** /membership/password-reset-requests | 
*MembershipApi* | [**membership_post_registration**](docs/MembershipApi.md#membership_post_registration) | **POST** /membership/registrations | 
*MembershipApi* | [**membership_put_user_role**](docs/MembershipApi.md#membership_put_user_role) | **PUT** /membership/roles/{tenantId}/{userId} | 
*PoolApi* | [**pool_get_pool_status**](docs/PoolApi.md#pool_get_pool_status) | **GET** /pools/{tenantId} | 
*PoolApi* | [**pool_get_pools**](docs/PoolApi.md#pool_get_pools) | **GET** /pools | 
*PoolApi* | [**pool_get_test_auto_scale_formula**](docs/PoolApi.md#pool_get_test_auto_scale_formula) | **GET** /pools/{tenantId}/autoscale/test | 
*SimVersionApi* | [**sim_version_get_document**](docs/SimVersionApi.md#sim_version_get_document) | **GET** /sim-versions/{simVersion}/documents/{documentPath} | 
*SimVersionApi* | [**sim_version_get_documents**](docs/SimVersionApi.md#sim_version_get_documents) | **GET** /sim-versions/{simVersion}/documents | 
*SimVersionApi* | [**sim_version_get_downloads**](docs/SimVersionApi.md#sim_version_get_downloads) | **GET** /sim-versions/{simVersion}/downloads | 
*SimVersionApi* | [**sim_version_get_sim_version**](docs/SimVersionApi.md#sim_version_get_sim_version) | **GET** /sim-versions/current | 
*SimVersionApi* | [**sim_version_get_wiki_document**](docs/SimVersionApi.md#sim_version_get_wiki_document) | **GET** /sim-versions/{wikiVersion}/wiki/{documentPath} | 
*SimVersionApi* | [**sim_version_post_sim_version**](docs/SimVersionApi.md#sim_version_post_sim_version) | **POST** /sim-versions/current | 
*StudyApi* | [**study_delete_study**](docs/StudyApi.md#study_delete_study) | **DELETE** /studies/{tenantId}/{studyId} | 
*StudyApi* | [**study_delete_study_deprecated**](docs/StudyApi.md#study_delete_study_deprecated) | **DELETE** /studies/{tenantId}/{userId}/{studyId} | 
*StudyApi* | [**study_get_all_tenants_study_statistics**](docs/StudyApi.md#study_get_all_tenants_study_statistics) | **GET** /studies/statistics | 
*StudyApi* | [**study_get_sim_type**](docs/StudyApi.md#study_get_sim_type) | **GET** /studies/types/sims/{simType} | 
*StudyApi* | [**study_get_studies**](docs/StudyApi.md#study_get_studies) | **GET** /studies/{tenantId} | 
*StudyApi* | [**study_get_study**](docs/StudyApi.md#study_get_study) | **GET** /studies/{tenantId}/{studyId} | 
*StudyApi* | [**study_get_study_deprecated**](docs/StudyApi.md#study_get_study_deprecated) | **GET** /studies/{tenantId}/{userId}/{studyId} | 
*StudyApi* | [**study_get_study_download**](docs/StudyApi.md#study_get_study_download) | **GET** /studies/{tenantId}/{studyId}/download | 
*StudyApi* | [**study_get_study_download_deprecated**](docs/StudyApi.md#study_get_study_download_deprecated) | **GET** /studies/{tenantId}/{userId}/{studyId}/download | 
*StudyApi* | [**study_get_study_download_url**](docs/StudyApi.md#study_get_study_download_url) | **GET** /studies/{tenantId}/{studyId}/download-url | 
*StudyApi* | [**study_get_study_download_url_deprecated**](docs/StudyApi.md#study_get_study_download_url_deprecated) | **GET** /studies/{tenantId}/{userId}/{studyId}/download-url | 
*StudyApi* | [**study_get_study_job**](docs/StudyApi.md#study_get_study_job) | **GET** /studies/{tenantId}/{studyId}/jobs/{jobId} | 
*StudyApi* | [**study_get_study_job_deprecated**](docs/StudyApi.md#study_get_study_job_deprecated) | **GET** /studies/{tenantId}/{userId}/{studyId}/jobs/{jobId} | 
*StudyApi* | [**study_get_study_job_download**](docs/StudyApi.md#study_get_study_job_download) | **GET** /studies/{tenantId}/{studyId}/jobs/{jobId}/download | 
*StudyApi* | [**study_get_study_job_download_deprecated**](docs/StudyApi.md#study_get_study_job_download_deprecated) | **GET** /studies/{tenantId}/{userId}/{studyId}/jobs/{jobId}/download | 
*StudyApi* | [**study_get_study_job_metadata**](docs/StudyApi.md#study_get_study_job_metadata) | **GET** /studies/{tenantId}/{studyId}/jobs/{jobId}/metadata | 
*StudyApi* | [**study_get_study_job_metadata_deprecated**](docs/StudyApi.md#study_get_study_job_metadata_deprecated) | **GET** /studies/{tenantId}/{userId}/{studyId}/jobs/{jobId}/metadata | 
*StudyApi* | [**study_get_study_jobs**](docs/StudyApi.md#study_get_study_jobs) | **GET** /studies/{tenantId}/{studyId}/jobs | 
*StudyApi* | [**study_get_study_jobs_deprecated**](docs/StudyApi.md#study_get_study_jobs_deprecated) | **GET** /studies/{tenantId}/{userId}/{studyId}/jobs | 
*StudyApi* | [**study_get_study_metadata**](docs/StudyApi.md#study_get_study_metadata) | **GET** /studies/{tenantId}/{studyId}/metadata | 
*StudyApi* | [**study_get_study_metadata_deprecated**](docs/StudyApi.md#study_get_study_metadata_deprecated) | **GET** /studies/{tenantId}/{userId}/{studyId}/metadata | 
*StudyApi* | [**study_get_study_metadata_without_user_id_deprecated**](docs/StudyApi.md#study_get_study_metadata_without_user_id_deprecated) | **GET** /studies/{tenantId}/auto/{studyId}/metadata | 
*StudyApi* | [**study_get_study_type**](docs/StudyApi.md#study_get_study_type) | **GET** /studies/types/{studyType} | 
*StudyApi* | [**study_get_study_types**](docs/StudyApi.md#study_get_study_types) | **GET** /studies/types | 
*StudyApi* | [**study_get_study_without_user_id_deprecated**](docs/StudyApi.md#study_get_study_without_user_id_deprecated) | **GET** /studies/{tenantId}/auto/{studyId} | 
*StudyApi* | [**study_get_tenant_access_information**](docs/StudyApi.md#study_get_tenant_access_information) | **GET** /studies/{tenantId}/access | 
*StudyApi* | [**study_get_tenant_billable_stored_simulation_count**](docs/StudyApi.md#study_get_tenant_billable_stored_simulation_count) | **GET** /studies/statistics/stored/{tenantId} | 
*StudyApi* | [**study_get_tenant_study_statistics**](docs/StudyApi.md#study_get_tenant_study_statistics) | **GET** /studies/statistics/{tenantId} | 
*StudyApi* | [**study_merge_study**](docs/StudyApi.md#study_merge_study) | **PATCH** /studies/{tenantId}/{studyId}/merge | 
*StudyApi* | [**study_merge_study_deprecated**](docs/StudyApi.md#study_merge_study_deprecated) | **PATCH** /studies/{tenantId}/{userId}/{studyId}/merge | 
*StudyApi* | [**study_post_study**](docs/StudyApi.md#study_post_study) | **POST** /studies/{tenantId} | 
*StudyApi* | [**study_post_study_deprecated**](docs/StudyApi.md#study_post_study_deprecated) | **POST** /studies/{tenantId}/{userId} | 
*StudyApi* | [**study_put_study**](docs/StudyApi.md#study_put_study) | **PUT** /studies/{tenantId}/{studyId} | 
*StudyApi* | [**study_put_study_deprecated**](docs/StudyApi.md#study_put_study_deprecated) | **PUT** /studies/{tenantId}/{userId}/{studyId} | 
*StudyApi* | [**study_put_study_owner**](docs/StudyApi.md#study_put_study_owner) | **PUT** /studies/{tenantId}/{studyId}/owner | 
*SupportSessionApi* | [**support_session_get_all_support_sessions**](docs/SupportSessionApi.md#support_session_get_all_support_sessions) | **GET** /support-sessions/all | 
*SupportSessionApi* | [**support_session_get_support_session**](docs/SupportSessionApi.md#support_session_get_support_session) | **GET** /support-sessions/{tenantId}/{documentId} | 
*SupportSessionApi* | [**support_session_get_support_session_deprecated**](docs/SupportSessionApi.md#support_session_get_support_session_deprecated) | **GET** /support-sessions/{tenantId}/{userId}/{documentId} | 
*SupportSessionApi* | [**support_session_put_support_session**](docs/SupportSessionApi.md#support_session_put_support_session) | **PUT** /support-sessions/{tenantId}/{documentId} | 
*SupportSessionApi* | [**support_session_put_support_session_deprecated**](docs/SupportSessionApi.md#support_session_put_support_session_deprecated) | **PUT** /support-sessions/{tenantId}/{userId}/{documentId} | 
*TenancyApi* | [**tenancy_delete_tenant**](docs/TenancyApi.md#tenancy_delete_tenant) | **DELETE** /tenants/{tenantId} | 
*TenancyApi* | [**tenancy_get_tenant**](docs/TenancyApi.md#tenancy_get_tenant) | **GET** /tenants/{tenantId} | 
*TenancyApi* | [**tenancy_get_tenant_users**](docs/TenancyApi.md#tenancy_get_tenant_users) | **GET** /tenants/{tenantId}/users | 
*TenancyApi* | [**tenancy_get_tenants**](docs/TenancyApi.md#tenancy_get_tenants) | **GET** /tenants | 
*TenancyApi* | [**tenancy_post_tenant**](docs/TenancyApi.md#tenancy_post_tenant) | **POST** /tenants | 
*TenancyApi* | [**tenancy_put_tenant**](docs/TenancyApi.md#tenancy_put_tenant) | **PUT** /tenants/{tenantId} | 
*TenantSettingsApi* | [**tenant_settings_get_admin_tenant_settings**](docs/TenantSettingsApi.md#tenant_settings_get_admin_tenant_settings) | **GET** /tenant-settings/admin/{tenantId} | 
*TenantSettingsApi* | [**tenant_settings_get_tenant_channel_import_mappings**](docs/TenantSettingsApi.md#tenant_settings_get_tenant_channel_import_mappings) | **GET** /tenant-settings/channel-import-mappings/{tenantId} | 
*TenantSettingsApi* | [**tenant_settings_get_tenant_channel_whitelists**](docs/TenantSettingsApi.md#tenant_settings_get_tenant_channel_whitelists) | **GET** /tenant-settings/channel-whitelists/{tenantId} | 
*TenantSettingsApi* | [**tenant_settings_get_tenant_default_custom_property_names**](docs/TenantSettingsApi.md#tenant_settings_get_tenant_default_custom_property_names) | **GET** /tenant-settings/default-custom-property-names/{tenantId} | 
*TenantSettingsApi* | [**tenant_settings_get_tenant_settings_sim_version**](docs/TenantSettingsApi.md#tenant_settings_get_tenant_settings_sim_version) | **GET** /tenant-settings/sim-version/{tenantId} | 
*TenantSettingsApi* | [**tenant_settings_get_tenant_worksheet_label_definitions**](docs/TenantSettingsApi.md#tenant_settings_get_tenant_worksheet_label_definitions) | **GET** /tenant-settings/worksheet-label-definitions/{tenantId} | 
*TenantSettingsApi* | [**tenant_settings_put_admin_tenant_settings**](docs/TenantSettingsApi.md#tenant_settings_put_admin_tenant_settings) | **PUT** /tenant-settings/admin/{tenantId} | 
*TenantSettingsApi* | [**tenant_settings_put_tenant_channel_import_mappings**](docs/TenantSettingsApi.md#tenant_settings_put_tenant_channel_import_mappings) | **PUT** /tenant-settings/channel-import-mappings/{tenantId} | 
*TenantSettingsApi* | [**tenant_settings_put_tenant_channel_whitelists**](docs/TenantSettingsApi.md#tenant_settings_put_tenant_channel_whitelists) | **PUT** /tenant-settings/channel-whitelists/{tenantId} | 
*TenantSettingsApi* | [**tenant_settings_put_tenant_default_custom_property_names**](docs/TenantSettingsApi.md#tenant_settings_put_tenant_default_custom_property_names) | **PUT** /tenant-settings/default-custom-property-names/{tenantId} | 
*TenantSettingsApi* | [**tenant_settings_put_tenant_settings_sim_version**](docs/TenantSettingsApi.md#tenant_settings_put_tenant_settings_sim_version) | **PUT** /tenant-settings/sim-version/{tenantId} | 
*TenantSettingsApi* | [**tenant_settings_put_tenant_worksheet_label_definitions**](docs/TenantSettingsApi.md#tenant_settings_put_tenant_worksheet_label_definitions) | **PUT** /tenant-settings/worksheet-label-definitions/{tenantId} | 
*TokenApi* | [**token_post_token**](docs/TokenApi.md#token_post_token) | **POST** /token | 
*UserSettingsApi* | [**user_settings_get_user_settings**](docs/UserSettingsApi.md#user_settings_get_user_settings) | **GET** /user-settings/{tenantId}/{userId} | 
*UserSettingsApi* | [**user_settings_put_user_settings**](docs/UserSettingsApi.md#user_settings_put_user_settings) | **PUT** /user-settings/{tenantId}/{userId} | 
*WorksheetApi* | [**worksheet_get_worksheet**](docs/WorksheetApi.md#worksheet_get_worksheet) | **GET** /worksheets/{tenantId}/{worksheetId} | 
*WorksheetApi* | [**worksheet_post_duplicate_configs**](docs/WorksheetApi.md#worksheet_post_duplicate_configs) | **POST** /worksheets/{tenantId}/{worksheetId}/duplicate | 
*WorksheetApi* | [**worksheet_post_worksheet**](docs/WorksheetApi.md#worksheet_post_worksheet) | **POST** /worksheets/{tenantId} | 
*WorksheetApi* | [**worksheet_put_worksheet**](docs/WorksheetApi.md#worksheet_put_worksheet) | **PUT** /worksheets/{tenantId}/{worksheetId} | 


## Documentation For Models

 - [AccountSettingsPutRequest](docs/AccountSettingsPutRequest.md)
 - [AdditionalTests](docs/AdditionalTests.md)
 - [AdminTenantSettings](docs/AdminTenantSettings.md)
 - [AdminTenantSettingsBuilder](docs/AdminTenantSettingsBuilder.md)
 - [AdminTenantSettingsPoolSettings](docs/AdminTenantSettingsPoolSettings.md)
 - [AllocationState](docs/AllocationState.md)
 - [AutoScaleRun](docs/AutoScaleRun.md)
 - [AutoScaleRunError](docs/AutoScaleRunError.md)
 - [AvailabilityResult](docs/AvailabilityResult.md)
 - [AvailabilityResultAdditionalTests](docs/AvailabilityResultAdditionalTests.md)
 - [BatchCreateConfigsResult](docs/BatchCreateConfigsResult.md)
 - [BlobAccessInformation](docs/BlobAccessInformation.md)
 - [CanopyDocument](docs/CanopyDocument.md)
 - [CanopyDocumentSupportSession](docs/CanopyDocumentSupportSession.md)
 - [ChannelImportMapping](docs/ChannelImportMapping.md)
 - [ChannelSettings](docs/ChannelSettings.md)
 - [ChartSettings](docs/ChartSettings.md)
 - [CollatedLabelDefinitions](docs/CollatedLabelDefinitions.md)
 - [CollatedLabelDefinitionsWorksheet](docs/CollatedLabelDefinitionsWorksheet.md)
 - [CollatedWorksheetLabels](docs/CollatedWorksheetLabels.md)
 - [CollatedWorksheetLabelsLabelDefinitions](docs/CollatedWorksheetLabelsLabelDefinitions.md)
 - [ComputeNodeResult](docs/ComputeNodeResult.md)
 - [ComputeNodeState](docs/ComputeNodeState.md)
 - [ConditionOperator](docs/ConditionOperator.md)
 - [ConfigColumnLabelDefinitions](docs/ConfigColumnLabelDefinitions.md)
 - [ConfigDecryptWithMetadataRequest](docs/ConfigDecryptWithMetadataRequest.md)
 - [ConfigEncryptWithMetadataRequest](docs/ConfigEncryptWithMetadataRequest.md)
 - [ConfigHash](docs/ConfigHash.md)
 - [ConfigOwnerData](docs/ConfigOwnerData.md)
 - [ConfigPostConfigRequest](docs/ConfigPostConfigRequest.md)
 - [ConfigPostConfigsRequest](docs/ConfigPostConfigsRequest.md)
 - [ConfigPutConfigOwnerRequest](docs/ConfigPutConfigOwnerRequest.md)
 - [ConfigPutConfigRequest](docs/ConfigPutConfigRequest.md)
 - [ConfigReference](docs/ConfigReference.md)
 - [ConfigReferenceDefault](docs/ConfigReferenceDefault.md)
 - [ConfigReferenceTenant](docs/ConfigReferenceTenant.md)
 - [ConfigResolvedLabels](docs/ConfigResolvedLabels.md)
 - [ConfigResolvedLabelsReference](docs/ConfigResolvedLabelsReference.md)
 - [ConfigResolvedReference](docs/ConfigResolvedReference.md)
 - [ConfigResolvedReferenceData](docs/ConfigResolvedReferenceData.md)
 - [ConfigTypeDefinition](docs/ConfigTypeDefinition.md)
 - [ConfigTypeMetadata](docs/ConfigTypeMetadata.md)
 - [ConfigTypeState](docs/ConfigTypeState.md)
 - [ConfigUpgradeConfigDeprecatedRequest](docs/ConfigUpgradeConfigDeprecatedRequest.md)
 - [DataToDecrypt](docs/DataToDecrypt.md)
 - [DataToEncrypt](docs/DataToEncrypt.md)
 - [DefaultConfigId](docs/DefaultConfigId.md)
 - [DefaultConfigReference](docs/DefaultConfigReference.md)
 - [DefaultCustomPropertyNames](docs/DefaultCustomPropertyNames.md)
 - [DocumentCustomPropertyData](docs/DocumentCustomPropertyData.md)
 - [DocumentCustomPropertyGroup](docs/DocumentCustomPropertyGroup.md)
 - [DocumentGroupResult](docs/DocumentGroupResult.md)
 - [DocumentNameResult](docs/DocumentNameResult.md)
 - [DocumentTypeCustomPropertyGroups](docs/DocumentTypeCustomPropertyGroups.md)
 - [DocumentUserInformation](docs/DocumentUserInformation.md)
 - [DocumentsAndContinuationToken](docs/DocumentsAndContinuationToken.md)
 - [DuplicateConfigsData](docs/DuplicateConfigsData.md)
 - [DuplicateConfigsResult](docs/DuplicateConfigsResult.md)
 - [EmailConfirmationData](docs/EmailConfirmationData.md)
 - [FileDownloadMetadata](docs/FileDownloadMetadata.md)
 - [GetAccountSettingsResult](docs/GetAccountSettingsResult.md)
 - [GetAdminTenantSettingsQueryResult](docs/GetAdminTenantSettingsQueryResult.md)
 - [GetAdminTenantSettingsQueryResultSettings](docs/GetAdminTenantSettingsQueryResultSettings.md)
 - [GetAllSupportSessionsQueryResult](docs/GetAllSupportSessionsQueryResult.md)
 - [GetAllSupportSessionsQueryResultUserInformation](docs/GetAllSupportSessionsQueryResultUserInformation.md)
 - [GetAllTenantsStudyStatisticsQueryResult](docs/GetAllTenantsStudyStatisticsQueryResult.md)
 - [GetConfigNamesQueryResult](docs/GetConfigNamesQueryResult.md)
 - [GetConfigQueryResult](docs/GetConfigQueryResult.md)
 - [GetConfigQueryResultConfig](docs/GetConfigQueryResultConfig.md)
 - [GetConfigVersionsQueryResult](docs/GetConfigVersionsQueryResult.md)
 - [GetConfigsQueryResult](docs/GetConfigsQueryResult.md)
 - [GetConfigsQueryResultQueryResults](docs/GetConfigsQueryResultQueryResults.md)
 - [GetDecryptedDataQueryResult](docs/GetDecryptedDataQueryResult.md)
 - [GetEncryptedDataQueryResult](docs/GetEncryptedDataQueryResult.md)
 - [GetPoolStatusQueryResult](docs/GetPoolStatusQueryResult.md)
 - [GetPoolsItem](docs/GetPoolsItem.md)
 - [GetPoolsItemInterval](docs/GetPoolsItemInterval.md)
 - [GetPoolsQueryResult](docs/GetPoolsQueryResult.md)
 - [GetSimVersionDocumentQueryResult](docs/GetSimVersionDocumentQueryResult.md)
 - [GetSimVersionDocumentQueryResultDocument](docs/GetSimVersionDocumentQueryResultDocument.md)
 - [GetSimVersionDocumentsQueryResult](docs/GetSimVersionDocumentsQueryResult.md)
 - [GetSimVersionDownloadsQueryResult](docs/GetSimVersionDownloadsQueryResult.md)
 - [GetStudiesQueryResult](docs/GetStudiesQueryResult.md)
 - [GetStudiesQueryResultQueryResults](docs/GetStudiesQueryResultQueryResults.md)
 - [GetStudyDownloadUrlQueryResult](docs/GetStudyDownloadUrlQueryResult.md)
 - [GetStudyJobMetadataQueryResult](docs/GetStudyJobMetadataQueryResult.md)
 - [GetStudyJobMetadataQueryResultAccessInformation](docs/GetStudyJobMetadataQueryResultAccessInformation.md)
 - [GetStudyJobQueryResult](docs/GetStudyJobQueryResult.md)
 - [GetStudyJobsQueryResult](docs/GetStudyJobsQueryResult.md)
 - [GetStudyJobsQueryResultQueryResults](docs/GetStudyJobsQueryResultQueryResults.md)
 - [GetStudyQueryResult](docs/GetStudyQueryResult.md)
 - [GetStudyQueryResultAccessInformation](docs/GetStudyQueryResultAccessInformation.md)
 - [GetStudyTypesQueryResult](docs/GetStudyTypesQueryResult.md)
 - [GetSupportSessionQueryResult](docs/GetSupportSessionQueryResult.md)
 - [GetTenantAccessInformationQueryResult](docs/GetTenantAccessInformationQueryResult.md)
 - [GetTenantBillableStoredSimulationCountQueryResult](docs/GetTenantBillableStoredSimulationCountQueryResult.md)
 - [GetTenantChannelImportMappingsQueryResult](docs/GetTenantChannelImportMappingsQueryResult.md)
 - [GetTenantChannelWhitelistsQueryResult](docs/GetTenantChannelWhitelistsQueryResult.md)
 - [GetTenantChannelWhitelistsQueryResultSettings](docs/GetTenantChannelWhitelistsQueryResultSettings.md)
 - [GetTenantDefaultCustomPropertyNamesQueryResult](docs/GetTenantDefaultCustomPropertyNamesQueryResult.md)
 - [GetTenantDefaultCustomPropertyNamesQueryResultSettings](docs/GetTenantDefaultCustomPropertyNamesQueryResultSettings.md)
 - [GetTenantQueryResult](docs/GetTenantQueryResult.md)
 - [GetTenantSettingsSimVersionQueryResult](docs/GetTenantSettingsSimVersionQueryResult.md)
 - [GetTenantStudyStatisticsQueryResult](docs/GetTenantStudyStatisticsQueryResult.md)
 - [GetTenantUsersQueryResult](docs/GetTenantUsersQueryResult.md)
 - [GetTenantUsersQueryResultUserItem](docs/GetTenantUsersQueryResultUserItem.md)
 - [GetTenantWorksheetLabelDefinitionsQueryResult](docs/GetTenantWorksheetLabelDefinitionsQueryResult.md)
 - [GetTenantWorksheetLabelDefinitionsQueryResultLabelDefinitions](docs/GetTenantWorksheetLabelDefinitionsQueryResultLabelDefinitions.md)
 - [GetTenantsQueryResult](docs/GetTenantsQueryResult.md)
 - [GetTenantsQueryResultTenantItem](docs/GetTenantsQueryResultTenantItem.md)
 - [GetUpvotyTokenQueryResult](docs/GetUpvotyTokenQueryResult.md)
 - [GetUserRolesQueryResult](docs/GetUserRolesQueryResult.md)
 - [GetUserSettingsQueryResult](docs/GetUserSettingsQueryResult.md)
 - [GetUserSettingsQueryResultSettings](docs/GetUserSettingsQueryResultSettings.md)
 - [GetWikiDocumentQueryResult](docs/GetWikiDocumentQueryResult.md)
 - [GetWorksheetQueryResult](docs/GetWorksheetQueryResult.md)
 - [GetWorksheetQueryResultWorksheet](docs/GetWorksheetQueryResultWorksheet.md)
 - [GetZendeskTokenQueryResult](docs/GetZendeskTokenQueryResult.md)
 - [GrantTypeHandlerResponse](docs/GrantTypeHandlerResponse.md)
 - [GroupOperator](docs/GroupOperator.md)
 - [IPreviousDefinitionSimTypeDefinition](docs/IPreviousDefinitionSimTypeDefinition.md)
 - [IPreviousDefinitionSimTypeDefinitionDefinition](docs/IPreviousDefinitionSimTypeDefinitionDefinition.md)
 - [IPreviousDefinitionStudyTypeDefinition](docs/IPreviousDefinitionStudyTypeDefinition.md)
 - [IPreviousDefinitionStudyTypeDefinitionDefinition](docs/IPreviousDefinitionStudyTypeDefinitionDefinition.md)
 - [IdentifiedUserData](docs/IdentifiedUserData.md)
 - [LabelDefinition](docs/LabelDefinition.md)
 - [LabelDefinitions](docs/LabelDefinitions.md)
 - [ListFilter](docs/ListFilter.md)
 - [ListFilterCondition](docs/ListFilterCondition.md)
 - [ListFilterGroup](docs/ListFilterGroup.md)
 - [ListFilterQuery](docs/ListFilterQuery.md)
 - [MembershipPostEmailConfirmationRequest](docs/MembershipPostEmailConfirmationRequest.md)
 - [MembershipPostIdentifiedUserRequest](docs/MembershipPostIdentifiedUserRequest.md)
 - [MembershipPostPasswordResetConfirmationRequest](docs/MembershipPostPasswordResetConfirmationRequest.md)
 - [MembershipPostPasswordResetRequestRequest](docs/MembershipPostPasswordResetRequestRequest.md)
 - [MembershipPostRegistrationRequest](docs/MembershipPostRegistrationRequest.md)
 - [MembershipPutUserRoleRequest](docs/MembershipPutUserRoleRequest.md)
 - [NameValuePair](docs/NameValuePair.md)
 - [NewBatchConfigData](docs/NewBatchConfigData.md)
 - [NewConfigData](docs/NewConfigData.md)
 - [NewSimVersionData](docs/NewSimVersionData.md)
 - [NewStudyData](docs/NewStudyData.md)
 - [NewStudyDataSource](docs/NewStudyDataSource.md)
 - [NewTenantData](docs/NewTenantData.md)
 - [NewWorksheetData](docs/NewWorksheetData.md)
 - [NewWorksheetDataOutline](docs/NewWorksheetDataOutline.md)
 - [OrderByProperty](docs/OrderByProperty.md)
 - [PasswordResetConfirmationData](docs/PasswordResetConfirmationData.md)
 - [PasswordResetRequestData](docs/PasswordResetRequestData.md)
 - [PoolSettings](docs/PoolSettings.md)
 - [PoolState](docs/PoolState.md)
 - [PoolType](docs/PoolType.md)
 - [PostStudyResult](docs/PostStudyResult.md)
 - [RegistrationData](docs/RegistrationData.md)
 - [ResolvedLabel](docs/ResolvedLabel.md)
 - [ResolvedLabelNumericStatistics](docs/ResolvedLabelNumericStatistics.md)
 - [ResolvedStatisticLabel](docs/ResolvedStatisticLabel.md)
 - [SimTypeDefinition](docs/SimTypeDefinition.md)
 - [SimTypeDefinitionInputTelemetryChannels](docs/SimTypeDefinitionInputTelemetryChannels.md)
 - [SimTypeInputTelemetryChannel](docs/SimTypeInputTelemetryChannel.md)
 - [SimTypeInputTelemetryChannelEvaluationDefinition](docs/SimTypeInputTelemetryChannelEvaluationDefinition.md)
 - [SimTypeInputTelemetryChannels](docs/SimTypeInputTelemetryChannels.md)
 - [SimTypeInputTelemetryEvaluatedChannel](docs/SimTypeInputTelemetryEvaluatedChannel.md)
 - [SimTypeInputTelemetryEvaluatedChannelSuffix](docs/SimTypeInputTelemetryEvaluatedChannelSuffix.md)
 - [SimTypeState](docs/SimTypeState.md)
 - [SimVersionDocumentNameResult](docs/SimVersionDocumentNameResult.md)
 - [SimVersionPostSimVersionRequest](docs/SimVersionPostSimVersionRequest.md)
 - [SimulationColumnLabelDefinitions](docs/SimulationColumnLabelDefinitions.md)
 - [SimulationInput](docs/SimulationInput.md)
 - [SimulationResolvedLabels](docs/SimulationResolvedLabels.md)
 - [StudyBlobAccessInformation](docs/StudyBlobAccessInformation.md)
 - [StudyDocument](docs/StudyDocument.md)
 - [StudyDocumentStudyDocumentDataSource](docs/StudyDocumentStudyDocumentDataSource.md)
 - [StudyDocumentsAndContinuationToken](docs/StudyDocumentsAndContinuationToken.md)
 - [StudyInputHash](docs/StudyInputHash.md)
 - [StudyInputHashes](docs/StudyInputHashes.md)
 - [StudyJobDocumentsAndContinuationToken](docs/StudyJobDocumentsAndContinuationToken.md)
 - [StudyPostStudyRequest](docs/StudyPostStudyRequest.md)
 - [StudyPutStudyRequest](docs/StudyPutStudyRequest.md)
 - [StudyReference](docs/StudyReference.md)
 - [StudyResolvedLabels](docs/StudyResolvedLabels.md)
 - [StudyResolvedLabelsReference](docs/StudyResolvedLabelsReference.md)
 - [StudyResolvedReference](docs/StudyResolvedReference.md)
 - [StudyResolvedReferenceData](docs/StudyResolvedReferenceData.md)
 - [StudyResolvedReferenceDataStudyDocument](docs/StudyResolvedReferenceDataStudyDocument.md)
 - [StudyState](docs/StudyState.md)
 - [StudyTypeDefinition](docs/StudyTypeDefinition.md)
 - [StudyTypeState](docs/StudyTypeState.md)
 - [SupportSession](docs/SupportSession.md)
 - [SupportSessionData](docs/SupportSessionData.md)
 - [SupportSessionPutSupportSessionRequest](docs/SupportSessionPutSupportSessionRequest.md)
 - [SupportSessionResponse](docs/SupportSessionResponse.md)
 - [SupportSessionsRequestMetadata](docs/SupportSessionsRequestMetadata.md)
 - [TenancyPostTenantRequest](docs/TenancyPostTenantRequest.md)
 - [TenancyPutTenantRequest](docs/TenancyPutTenantRequest.md)
 - [TenantChannelWhitelists](docs/TenantChannelWhitelists.md)
 - [TenantConfigReference](docs/TenantConfigReference.md)
 - [TenantDefaultCustomPropertyNames](docs/TenantDefaultCustomPropertyNames.md)
 - [TenantInformation](docs/TenantInformation.md)
 - [TenantSettingsPutAdminTenantSettingsRequest](docs/TenantSettingsPutAdminTenantSettingsRequest.md)
 - [TenantSettingsPutTenantChannelImportMappingsRequest](docs/TenantSettingsPutTenantChannelImportMappingsRequest.md)
 - [TenantSettingsPutTenantChannelWhitelistsRequest](docs/TenantSettingsPutTenantChannelWhitelistsRequest.md)
 - [TenantSettingsPutTenantDefaultCustomPropertyNamesRequest](docs/TenantSettingsPutTenantDefaultCustomPropertyNamesRequest.md)
 - [TenantSettingsPutTenantSettingsSimVersionRequest](docs/TenantSettingsPutTenantSettingsSimVersionRequest.md)
 - [TenantSettingsPutTenantWorksheetLabelDefinitionsRequest](docs/TenantSettingsPutTenantWorksheetLabelDefinitionsRequest.md)
 - [TenantStatistics](docs/TenantStatistics.md)
 - [TestAutoScaleFormulaQueryResult](docs/TestAutoScaleFormulaQueryResult.md)
 - [TestAutoScaleFormulaQueryResultAutoScaleRun](docs/TestAutoScaleFormulaQueryResultAutoScaleRun.md)
 - [TextDocument](docs/TextDocument.md)
 - [TextDocumentOptionalContent](docs/TextDocumentOptionalContent.md)
 - [UpdatedAccountSettings](docs/UpdatedAccountSettings.md)
 - [UpdatedAdminTenantSettings](docs/UpdatedAdminTenantSettings.md)
 - [UpdatedAdminTenantSettingsSettings](docs/UpdatedAdminTenantSettingsSettings.md)
 - [UpdatedChannelImportMappings](docs/UpdatedChannelImportMappings.md)
 - [UpdatedConfigData](docs/UpdatedConfigData.md)
 - [UpdatedStudyData](docs/UpdatedStudyData.md)
 - [UpdatedTenantChannelWhitelists](docs/UpdatedTenantChannelWhitelists.md)
 - [UpdatedTenantData](docs/UpdatedTenantData.md)
 - [UpdatedTenantDefaultCustomPropertyNames](docs/UpdatedTenantDefaultCustomPropertyNames.md)
 - [UpdatedTenantSettingsSimVersion](docs/UpdatedTenantSettingsSimVersion.md)
 - [UpdatedUserSettings](docs/UpdatedUserSettings.md)
 - [UpdatedUserSettingsSettings](docs/UpdatedUserSettingsSettings.md)
 - [UpdatedWorksheetData](docs/UpdatedWorksheetData.md)
 - [UpdatedWorksheetLabelDefinitions](docs/UpdatedWorksheetLabelDefinitions.md)
 - [UpgradeConfigData](docs/UpgradeConfigData.md)
 - [UpgradeConfigQueryResult](docs/UpgradeConfigQueryResult.md)
 - [UserInformation](docs/UserInformation.md)
 - [UserRoleData](docs/UserRoleData.md)
 - [UserSettings](docs/UserSettings.md)
 - [UserSettingsBuilder](docs/UserSettingsBuilder.md)
 - [UserSettingsPutUserSettingsRequest](docs/UserSettingsPutUserSettingsRequest.md)
 - [VersionedDocumentMetadata](docs/VersionedDocumentMetadata.md)
 - [Worksheet](docs/Worksheet.md)
 - [WorksheetConfig](docs/WorksheetConfig.md)
 - [WorksheetConfigReference](docs/WorksheetConfigReference.md)
 - [WorksheetOutline](docs/WorksheetOutline.md)
 - [WorksheetPostDuplicateConfigsRequest](docs/WorksheetPostDuplicateConfigsRequest.md)
 - [WorksheetPostWorksheetRequest](docs/WorksheetPostWorksheetRequest.md)
 - [WorksheetPutWorksheetRequest](docs/WorksheetPutWorksheetRequest.md)
 - [WorksheetResolvedLabels](docs/WorksheetResolvedLabels.md)
 - [WorksheetResolvedReferences](docs/WorksheetResolvedReferences.md)
 - [WorksheetRow](docs/WorksheetRow.md)
 - [WorksheetRowStudy](docs/WorksheetRowStudy.md)
 - [WorksheetStudy](docs/WorksheetStudy.md)
 - [WorksheetStudyReference](docs/WorksheetStudyReference.md)


## Documentation For Authorization


## Bearer

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: N/A


## Author




