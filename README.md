# Generating API Client

Due to a bug in the python code generator, we cannot generate the client from the public API:

https://github.com/swagger-api/swagger-codegen-generators/issues/462

Instead we must first update `canopy-swagger-no-allof.json` to contain the latest swagger definition with 
the `allOf` references removed.

Currently the easiest way to do this is with access to the Canopy source code, which is internal to Canopy.
Therefore you should simply ask us to update this library if you find the generated API client is out of date.
 
For Canopy employees: To remove `allOf` references, comment out the line `c.SchemaFilter<FixReadOnlyRefSchemaFilter>();` in 
`Canopy.Api.Swagger.SwaggerConfig`, run locally, and copy the output of `https://localhost:44300/swagger/docs/v1`.

Don't forget to revert changes to `Canopy.Api.Swagger.SwaggerConfig`. 

Next you can use the Dockerfile in this repository to create a docker image to easily generate the new API stubs:
```
docker image build -t canopy-python-gen:1 .
docker container run -i -t --mount type=bind,src='c:\dev\canopy\canopy-python',dst=/usr/src/app/repo canopy-python-gen:1 /bin/bash

java -jar swagger-codegen-cli.jar generate -l python -i ./canopy-swagger-no-allof.json -o ./gen -DpackageName="canopy.swagger"
rsync -av gen/canopy.swagger/ gen/canopy/swagger/
rm -r repo/canopy/swagger
rm -r repo/docs
cp -r gen/canopy/swagger repo/canopy
cp -r gen/docs repo
```

## Requirements.

This has currently been tested on Python 3.6 and higher.

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/CanopySimulations/canopy-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/CanopySimulations/canopy-python.git`)

Then see `canopy/__main__.py` for example usage.

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then see `canopy/__main__.py` for example usage.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

Then see `canopy/__main__.py` for example usage.

## Documentation for API Endpoints

All URIs are relative to *https://api.canopysimulations.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountSettingsApi* | [**account_settings_get**](docs/AccountSettingsApi.md#account_settings_get) | **GET** /account-settings/{tenantId}/{userId} | 
*AccountSettingsApi* | [**account_settings_put**](docs/AccountSettingsApi.md#account_settings_put) | **PUT** /account-settings/{tenantId}/{userId} | 
*AvailabilityApi* | [**availability_get**](docs/AvailabilityApi.md#availability_get) | **GET** /Availability | 
*AvailabilityApi* | [**availability_head**](docs/AvailabilityApi.md#availability_head) | **HEAD** /Availability | 
*ConfigApi* | [**config_decrypt**](docs/ConfigApi.md#config_decrypt) | **POST** /configs/decrypt | 
*ConfigApi* | [**config_delete_config**](docs/ConfigApi.md#config_delete_config) | **DELETE** /configs/{tenantId}/{configId} | 
*ConfigApi* | [**config_delete_config_deprecated**](docs/ConfigApi.md#config_delete_config_deprecated) | **DELETE** /configs/{tenantId}/{userId}/{configId} | 
*ConfigApi* | [**config_encrypt**](docs/ConfigApi.md#config_encrypt) | **POST** /configs/encrypt | 
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
*MembershipApi* | [**membership_get_user_roles**](docs/MembershipApi.md#membership_get_user_roles) | **GET** /membership/roles/{tenantId}/{userId} | 
*MembershipApi* | [**membership_post_identified_user**](docs/MembershipApi.md#membership_post_identified_user) | **POST** /membership/identified-users | 
*MembershipApi* | [**membership_post_initialize**](docs/MembershipApi.md#membership_post_initialize) | **POST** /membership/initialize | 
*MembershipApi* | [**membership_post_password_reset_confirmation**](docs/MembershipApi.md#membership_post_password_reset_confirmation) | **POST** /membership/password-reset-confirmations | 
*MembershipApi* | [**membership_post_password_reset_request**](docs/MembershipApi.md#membership_post_password_reset_request) | **POST** /membership/password-reset-requests | 
*MembershipApi* | [**membership_post_registration**](docs/MembershipApi.md#membership_post_registration) | **POST** /membership/registrations | 
*MembershipApi* | [**membership_put_user_role**](docs/MembershipApi.md#membership_put_user_role) | **PUT** /membership/roles/{tenantId}/{userId} | 
*PoolApi* | [**pool_get_pool_status**](docs/PoolApi.md#pool_get_pool_status) | **GET** /pools/{tenantId} | 
*PoolApi* | [**pool_get_pools**](docs/PoolApi.md#pool_get_pools) | **GET** /pools | 
*PoolApi* | [**pool_get_test_auto_scale_formula**](docs/PoolApi.md#pool_get_test_auto_scale_formula) | **GET** /pools/autoscale/test | 
*SimVersionApi* | [**sim_version_get_document**](docs/SimVersionApi.md#sim_version_get_document) | **GET** /sim-versions/{simVersion}/documents/{documentPath} | 
*SimVersionApi* | [**sim_version_get_documents**](docs/SimVersionApi.md#sim_version_get_documents) | **GET** /sim-versions/{simVersion}/documents | 
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
*StudyApi* | [**study_put_config_owner**](docs/StudyApi.md#study_put_config_owner) | **PUT** /studies/{tenantId}/{studyId}/owner | 
*StudyApi* | [**study_put_study**](docs/StudyApi.md#study_put_study) | **PUT** /studies/{tenantId}/{studyId} | 
*StudyApi* | [**study_put_study_deprecated**](docs/StudyApi.md#study_put_study_deprecated) | **PUT** /studies/{tenantId}/{userId}/{studyId} | 
*SupportSessionApi* | [**support_session_get_all_support_sessions**](docs/SupportSessionApi.md#support_session_get_all_support_sessions) | **GET** /support-sessions/all | 
*SupportSessionApi* | [**support_session_get_support_session**](docs/SupportSessionApi.md#support_session_get_support_session) | **GET** /support-sessions/{tenantId}/{documentId} | 
*SupportSessionApi* | [**support_session_get_support_session_deprecated**](docs/SupportSessionApi.md#support_session_get_support_session_deprecated) | **GET** /support-sessions/{tenantId}/{userId}/{documentId} | 
*SupportSessionApi* | [**support_session_put_support_session**](docs/SupportSessionApi.md#support_session_put_support_session) | **PUT** /support-sessions/{tenantId}/{documentId} | 
*SupportSessionApi* | [**support_session_put_support_session_deprecated**](docs/SupportSessionApi.md#support_session_put_support_session_deprecated) | **PUT** /support-sessions/{tenantId}/{userId}/{documentId} | 
*TenancyApi* | [**tenancy_get_tenant**](docs/TenancyApi.md#tenancy_get_tenant) | **GET** /tenants/{tenantId} | 
*TenancyApi* | [**tenancy_get_tenant_users**](docs/TenancyApi.md#tenancy_get_tenant_users) | **GET** /tenants/{tenantId}/users | 
*TenancyApi* | [**tenancy_get_tenants**](docs/TenancyApi.md#tenancy_get_tenants) | **GET** /tenants | 
*TenancyApi* | [**tenancy_post_tenant**](docs/TenancyApi.md#tenancy_post_tenant) | **POST** /tenants | 
*TenancyApi* | [**tenancy_put_tenant**](docs/TenancyApi.md#tenancy_put_tenant) | **PUT** /tenants/{tenantId} | 
*TenantSettingsApi* | [**tenant_settings_get_admin_tenant_settings**](docs/TenantSettingsApi.md#tenant_settings_get_admin_tenant_settings) | **GET** /tenant-settings/admin/{tenantId} | 
*TenantSettingsApi* | [**tenant_settings_get_tenant_channel_import_mappings**](docs/TenantSettingsApi.md#tenant_settings_get_tenant_channel_import_mappings) | **GET** /tenant-settings/channel-import-mappings/{tenantId} | 
*TenantSettingsApi* | [**tenant_settings_get_tenant_default_custom_property_names**](docs/TenantSettingsApi.md#tenant_settings_get_tenant_default_custom_property_names) | **GET** /tenant-settings/default-custom-property-names/{tenantId} | 
*TenantSettingsApi* | [**tenant_settings_get_tenant_settings_sim_version**](docs/TenantSettingsApi.md#tenant_settings_get_tenant_settings_sim_version) | **GET** /tenant-settings/sim-version/{tenantId} | 
*TenantSettingsApi* | [**tenant_settings_get_tenant_worksheet_label_definitions**](docs/TenantSettingsApi.md#tenant_settings_get_tenant_worksheet_label_definitions) | **GET** /tenant-settings/worksheet-label-definitions/{tenantId} | 
*TenantSettingsApi* | [**tenant_settings_put_admin_tenant_settings**](docs/TenantSettingsApi.md#tenant_settings_put_admin_tenant_settings) | **PUT** /tenant-settings/admin/{tenantId} | 
*TenantSettingsApi* | [**tenant_settings_put_tenant_channel_import_mappings**](docs/TenantSettingsApi.md#tenant_settings_put_tenant_channel_import_mappings) | **PUT** /tenant-settings/channel-import-mappings/{tenantId} | 
*TenantSettingsApi* | [**tenant_settings_put_tenant_default_custom_property_names**](docs/TenantSettingsApi.md#tenant_settings_put_tenant_default_custom_property_names) | **PUT** /tenant-settings/default-custom-property-names/{tenantId} | 
*TenantSettingsApi* | [**tenant_settings_put_tenant_settings_sim_version**](docs/TenantSettingsApi.md#tenant_settings_put_tenant_settings_sim_version) | **PUT** /tenant-settings/sim-version/{tenantId} | 
*TenantSettingsApi* | [**tenant_settings_put_tenant_worksheet_label_definitions**](docs/TenantSettingsApi.md#tenant_settings_put_tenant_worksheet_label_definitions) | **PUT** /tenant-settings/worksheet-label-definitions/{tenantId} | 
*UserSettingsApi* | [**user_settings_get_user_settings**](docs/UserSettingsApi.md#user_settings_get_user_settings) | **GET** /user-settings/{tenantId}/{userId} | 
*UserSettingsApi* | [**user_settings_put_user_settings**](docs/UserSettingsApi.md#user_settings_put_user_settings) | **PUT** /user-settings/{tenantId}/{userId} | 
*WorksheetApi* | [**worksheet_get_worksheet**](docs/WorksheetApi.md#worksheet_get_worksheet) | **GET** /worksheets/{tenantId}/{worksheetId} | 
*WorksheetApi* | [**worksheet_post_duplicate_configs**](docs/WorksheetApi.md#worksheet_post_duplicate_configs) | **POST** /worksheets/{tenantId}/{worksheetId}/duplicate | 
*WorksheetApi* | [**worksheet_post_worksheet**](docs/WorksheetApi.md#worksheet_post_worksheet) | **POST** /worksheets/{tenantId} | 
*WorksheetApi* | [**worksheet_put_worksheet**](docs/WorksheetApi.md#worksheet_put_worksheet) | **PUT** /worksheets/{tenantId}/{worksheetId} | 


## Documentation For Models

 - [AdditionalTests](docs/AdditionalTests.md)
 - [AdminTenantSettings](docs/AdminTenantSettings.md)
 - [AdminTenantSettingsBuilder](docs/AdminTenantSettingsBuilder.md)
 - [AutoScaleRun](docs/AutoScaleRun.md)
 - [AutoScaleRunError](docs/AutoScaleRunError.md)
 - [AvailabilityResult](docs/AvailabilityResult.md)
 - [BatchCreateConfigsResult](docs/BatchCreateConfigsResult.md)
 - [BlobAccessInformation](docs/BlobAccessInformation.md)
 - [CanopyDocument](docs/CanopyDocument.md)
 - [ChannelImportMapping](docs/ChannelImportMapping.md)
 - [ChannelSettings](docs/ChannelSettings.md)
 - [ChartSettings](docs/ChartSettings.md)
 - [CollatedLabelDefinitions](docs/CollatedLabelDefinitions.md)
 - [CollatedWorksheetLabels](docs/CollatedWorksheetLabels.md)
 - [ComputeNodeResult](docs/ComputeNodeResult.md)
 - [ConfigColumnLabelDefinitions](docs/ConfigColumnLabelDefinitions.md)
 - [ConfigHash](docs/ConfigHash.md)
 - [ConfigOwnerData](docs/ConfigOwnerData.md)
 - [ConfigReference](docs/ConfigReference.md)
 - [ConfigResolvedLabels](docs/ConfigResolvedLabels.md)
 - [ConfigResolvedReference](docs/ConfigResolvedReference.md)
 - [ConfigResolvedReferenceData](docs/ConfigResolvedReferenceData.md)
 - [ConfigTypeDefinition](docs/ConfigTypeDefinition.md)
 - [DefaultConfigId](docs/DefaultConfigId.md)
 - [DefaultConfigReference](docs/DefaultConfigReference.md)
 - [DefaultCustomPropertyNames](docs/DefaultCustomPropertyNames.md)
 - [DocumentCustomPropertyData](docs/DocumentCustomPropertyData.md)
 - [DocumentCustomPropertyGroup](docs/DocumentCustomPropertyGroup.md)
 - [DocumentGroupResult](docs/DocumentGroupResult.md)
 - [DocumentId](docs/DocumentId.md)
 - [DocumentName](docs/DocumentName.md)
 - [DocumentNameResult](docs/DocumentNameResult.md)
 - [DocumentSubType](docs/DocumentSubType.md)
 - [DocumentTypeCustomPropertyGroups](docs/DocumentTypeCustomPropertyGroups.md)
 - [DocumentUserInformation](docs/DocumentUserInformation.md)
 - [DocumentsAndContinuationToken](docs/DocumentsAndContinuationToken.md)
 - [DuplicateConfigsData](docs/DuplicateConfigsData.md)
 - [DuplicateConfigsResult](docs/DuplicateConfigsResult.md)
 - [Email](docs/Email.md)
 - [GetAccountSettingsResult](docs/GetAccountSettingsResult.md)
 - [GetAdminTenantSettingsQueryResult](docs/GetAdminTenantSettingsQueryResult.md)
 - [GetAllSupportSessionsQueryResult](docs/GetAllSupportSessionsQueryResult.md)
 - [GetAllTenantsStudyStatisticsQueryResult](docs/GetAllTenantsStudyStatisticsQueryResult.md)
 - [GetConfigNamesQueryResult](docs/GetConfigNamesQueryResult.md)
 - [GetConfigQueryResult](docs/GetConfigQueryResult.md)
 - [GetConfigVersionsQueryResult](docs/GetConfigVersionsQueryResult.md)
 - [GetConfigsQueryResult](docs/GetConfigsQueryResult.md)
 - [GetPoolStatusQueryResult](docs/GetPoolStatusQueryResult.md)
 - [GetPoolsItem](docs/GetPoolsItem.md)
 - [GetPoolsItemInterval](docs/GetPoolsItemInterval.md)
 - [GetPoolsQueryResult](docs/GetPoolsQueryResult.md)
 - [GetSimVersionDocumentQueryResult](docs/GetSimVersionDocumentQueryResult.md)
 - [GetSimVersionDocumentsQueryResult](docs/GetSimVersionDocumentsQueryResult.md)
 - [GetStudiesQueryResult](docs/GetStudiesQueryResult.md)
 - [GetStudyDownloadUrlQueryResult](docs/GetStudyDownloadUrlQueryResult.md)
 - [GetStudyJobMetadataQueryResult](docs/GetStudyJobMetadataQueryResult.md)
 - [GetStudyJobQueryResult](docs/GetStudyJobQueryResult.md)
 - [GetStudyJobsQueryResult](docs/GetStudyJobsQueryResult.md)
 - [GetStudyQueryResult](docs/GetStudyQueryResult.md)
 - [GetStudyTypesQueryResult](docs/GetStudyTypesQueryResult.md)
 - [GetSupportSessionQueryResult](docs/GetSupportSessionQueryResult.md)
 - [GetTenantAccessInformationQueryResult](docs/GetTenantAccessInformationQueryResult.md)
 - [GetTenantBillableStoredSimulationCountQueryResult](docs/GetTenantBillableStoredSimulationCountQueryResult.md)
 - [GetTenantChannelImportMappingsQueryResult](docs/GetTenantChannelImportMappingsQueryResult.md)
 - [GetTenantDefaultCustomPropertyNamesQueryResult](docs/GetTenantDefaultCustomPropertyNamesQueryResult.md)
 - [GetTenantQueryResult](docs/GetTenantQueryResult.md)
 - [GetTenantSettingsSimVersionQueryResult](docs/GetTenantSettingsSimVersionQueryResult.md)
 - [GetTenantStudyStatisticsQueryResult](docs/GetTenantStudyStatisticsQueryResult.md)
 - [GetTenantUsersQueryResult](docs/GetTenantUsersQueryResult.md)
 - [GetTenantUsersQueryResultUserItem](docs/GetTenantUsersQueryResultUserItem.md)
 - [GetTenantWorksheetLabelDefinitionsQueryResult](docs/GetTenantWorksheetLabelDefinitionsQueryResult.md)
 - [GetTenantsQueryResult](docs/GetTenantsQueryResult.md)
 - [GetTenantsQueryResultTenantItem](docs/GetTenantsQueryResultTenantItem.md)
 - [GetUserRolesQueryResult](docs/GetUserRolesQueryResult.md)
 - [GetUserSettingsQueryResult](docs/GetUserSettingsQueryResult.md)
 - [GetWikiDocumentQueryResult](docs/GetWikiDocumentQueryResult.md)
 - [GetWorksheetQueryResult](docs/GetWorksheetQueryResult.md)
 - [IPreviousDefinitionSimTypeDefinition](docs/IPreviousDefinitionSimTypeDefinition.md)
 - [IPreviousDefinitionStudyTypeDefinition](docs/IPreviousDefinitionStudyTypeDefinition.md)
 - [IdentifiedUserData](docs/IdentifiedUserData.md)
 - [LabelDefinition](docs/LabelDefinition.md)
 - [LabelDefinitions](docs/LabelDefinitions.md)
 - [ListFilter](docs/ListFilter.md)
 - [ListFilterCondition](docs/ListFilterCondition.md)
 - [ListFilterGroup](docs/ListFilterGroup.md)
 - [NameValuePair](docs/NameValuePair.md)
 - [NewBatchConfigData](docs/NewBatchConfigData.md)
 - [NewConfigData](docs/NewConfigData.md)
 - [NewSimVersionData](docs/NewSimVersionData.md)
 - [NewStudyData](docs/NewStudyData.md)
 - [NewStudyDataSource](docs/NewStudyDataSource.md)
 - [NewTenantData](docs/NewTenantData.md)
 - [NewWorksheetData](docs/NewWorksheetData.md)
 - [PasswordResetConfirmationData](docs/PasswordResetConfirmationData.md)
 - [PasswordResetRequestData](docs/PasswordResetRequestData.md)
 - [PoolId](docs/PoolId.md)
 - [PoolSettings](docs/PoolSettings.md)
 - [PostStudyResult](docs/PostStudyResult.md)
 - [RegistrationData](docs/RegistrationData.md)
 - [ResolvedLabel](docs/ResolvedLabel.md)
 - [ResolvedStatisticLabel](docs/ResolvedStatisticLabel.md)
 - [SimTypeDefinition](docs/SimTypeDefinition.md)
 - [SimTypeInputTelemetryChannel](docs/SimTypeInputTelemetryChannel.md)
 - [SimTypeInputTelemetryChannels](docs/SimTypeInputTelemetryChannels.md)
 - [SimTypeInputTelemetryEvaluatedChannel](docs/SimTypeInputTelemetryEvaluatedChannel.md)
 - [SimTypeInputTelemetryEvaluatedChannelSuffix](docs/SimTypeInputTelemetryEvaluatedChannelSuffix.md)
 - [SimVersion](docs/SimVersion.md)
 - [SimVersionDocumentNameResult](docs/SimVersionDocumentNameResult.md)
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
 - [StudyReference](docs/StudyReference.md)
 - [StudyResolvedLabels](docs/StudyResolvedLabels.md)
 - [StudyResolvedReference](docs/StudyResolvedReference.md)
 - [StudyResolvedReferenceData](docs/StudyResolvedReferenceData.md)
 - [StudyTypeDefinition](docs/StudyTypeDefinition.md)
 - [SupportSession](docs/SupportSession.md)
 - [SupportSessionData](docs/SupportSessionData.md)
 - [SupportSessionResponse](docs/SupportSessionResponse.md)
 - [TenantConfigReference](docs/TenantConfigReference.md)
 - [TenantDefaultCustomPropertyNames](docs/TenantDefaultCustomPropertyNames.md)
 - [TenantDocumentDatabaseId](docs/TenantDocumentDatabaseId.md)
 - [TenantId](docs/TenantId.md)
 - [TenantInformation](docs/TenantInformation.md)
 - [TenantName](docs/TenantName.md)
 - [TenantStatistics](docs/TenantStatistics.md)
 - [TestAutoScaleFormulaQueryResult](docs/TestAutoScaleFormulaQueryResult.md)
 - [TextDocument](docs/TextDocument.md)
 - [TextDocumentOptionalContent](docs/TextDocumentOptionalContent.md)
 - [UpdatedAccountSettings](docs/UpdatedAccountSettings.md)
 - [UpdatedAdminTenantSettings](docs/UpdatedAdminTenantSettings.md)
 - [UpdatedChannelImportMappings](docs/UpdatedChannelImportMappings.md)
 - [UpdatedConfigData](docs/UpdatedConfigData.md)
 - [UpdatedStudyData](docs/UpdatedStudyData.md)
 - [UpdatedTenantData](docs/UpdatedTenantData.md)
 - [UpdatedTenantDefaultCustomPropertyNames](docs/UpdatedTenantDefaultCustomPropertyNames.md)
 - [UpdatedTenantSettingsSimVersion](docs/UpdatedTenantSettingsSimVersion.md)
 - [UpdatedUserSettings](docs/UpdatedUserSettings.md)
 - [UpdatedWorksheetData](docs/UpdatedWorksheetData.md)
 - [UpdatedWorksheetLabelDefinitions](docs/UpdatedWorksheetLabelDefinitions.md)
 - [UpgradeConfigData](docs/UpgradeConfigData.md)
 - [UpgradeConfigQueryResult](docs/UpgradeConfigQueryResult.md)
 - [UserId](docs/UserId.md)
 - [UserInformation](docs/UserInformation.md)
 - [UserRoleData](docs/UserRoleData.md)
 - [UserSettings](docs/UserSettings.md)
 - [UserSettingsBuilder](docs/UserSettingsBuilder.md)
 - [Username](docs/Username.md)
 - [ValidDocumentCustomPropertyName](docs/ValidDocumentCustomPropertyName.md)
 - [VersionedDocumentMetadata](docs/VersionedDocumentMetadata.md)
 - [Worksheet](docs/Worksheet.md)
 - [WorksheetConfig](docs/WorksheetConfig.md)
 - [WorksheetOutline](docs/WorksheetOutline.md)
 - [WorksheetResolvedReferences](docs/WorksheetResolvedReferences.md)
 - [WorksheetRow](docs/WorksheetRow.md)
 - [WorksheetStudy](docs/WorksheetStudy.md)

## Documentation For Authorization

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: https://api.canopysimulations.com/token
- **Scopes**: N/A

