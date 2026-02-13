# GetStudyQueryResult

The result of the query to get a study.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**study** | [**GetStudyQueryResultStudy**](GetStudyQueryResultStudy.md) |  | [optional] 
**converted_sim_version** | **str** | The sim version the study data was converted to. | [optional] 
**access_information** | [**GetStudyQueryResultAccessInformation**](GetStudyQueryResultAccessInformation.md) |  | [optional] 
**sim_types** | **list[str]** | The sim types which were detected in the first succeeded study job. | [optional] 
**user_information** | [**GetStudyQueryResultUserInformation**](GetStudyQueryResultUserInformation.md) |  | [optional] 
**priority** | **str** | The priority if the study is running. Otherwise null. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


