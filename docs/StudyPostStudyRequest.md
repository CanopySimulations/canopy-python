# StudyPostStudyRequest

Represents data for creating a new study.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the study. | [optional] 
**is_transient** | **bool** | Whether the study is transient. | [optional] 
**study_type** | **str** | The type of the study. | [optional] 
**sources** | [**list[NewStudyDataSource]**](NewStudyDataSource.md) | The data sources for the study. | [optional] 
**properties** | [**list[DocumentCustomPropertyData]**](DocumentCustomPropertyData.md) | The custom properties of the study. | [optional] 
**study** | **object** | The JSON study data. | [optional] 
**notes** | **str** | The notes for the study. | [optional] 
**sim_version** | **str** | The sim version for the study. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


