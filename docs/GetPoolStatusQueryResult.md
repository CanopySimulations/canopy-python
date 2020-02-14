# GetPoolStatusQueryResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_id** | **str** |  | [optional] 
**pool_state** | **str** |  | [optional] [readonly] 
**allocation_state** | **str** |  | [optional] [readonly] 
**current_dedicated** | **int** |  | [optional] [readonly] 
**target_dedicated** | **int** |  | [optional] [readonly] 
**current_low_priority** | **int** |  | [optional] [readonly] 
**target_low_priority** | **int** |  | [optional] [readonly] 
**maximum_tasks_per_node** | **int** |  | [optional] [readonly] 
**schedulable_compute_nodes** | **int** |  | [optional] [readonly] 
**running_tasks** | **int** |  | [optional] [readonly] 
**compute_nodes** | [**list[ComputeNodeResult]**](ComputeNodeResult.md) |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


