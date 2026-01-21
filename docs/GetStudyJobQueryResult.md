# GetStudyJobQueryResult

The result of the query to get study job.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**study_job** | [**GetStudyJobQueryResultStudyJob**](GetStudyJobQueryResultStudyJob.md) |  | [optional] 
**study_job_input** | **object** | The JSON input to the study job, also referred to as the job definition.  This will be null for post processor jobs and failed validation jobs. | [optional] 
**converted_sim_version** | **object** | The sim version which the study definition was converted to. | [optional] 
**sim_types** | **list[str]** | The sim types detected in this study job. | [optional] 
**access_information** | [**GetStudyJobQueryResultAccessInformation**](GetStudyJobQueryResultAccessInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


