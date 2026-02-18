# GetPoolStatusQueryResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_id** | **str** |  | [optional] 
**pool_state** | [**PoolState**](PoolState.md) |  | [optional] 
**allocation_state** | [**AllocationState**](AllocationState.md) |  | [optional] 
**current_dedicated** | **int** |  | [optional] 
**target_dedicated** | **int** |  | [optional] 
**current_low_priority** | **int** |  | [optional] 
**target_low_priority** | **int** |  | [optional] 
**maximum_tasks_per_node** | **int** |  | [optional] 
**schedulable_compute_nodes** | **int** |  | [optional] 
**running_tasks** | **int** |  | [optional] 
**compute_nodes** | [**list[ComputeNodeResult]**](ComputeNodeResult.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


