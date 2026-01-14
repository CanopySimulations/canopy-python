# StudyBlobAccessInformation

The URL and access signature required to access the blobs for a study on the main storage  container, plus a list of URLs and access signatures for accessing the results for the study  jobs.  The job results are sharded across storage containers, with a random starting shard  picked for each study, and the jobs then distributed across the shards in sequence, wrapping  around to the start when the end is reached.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL of the folder in blob storage containing the blobs. | [optional] 
**access_signature** | **str** | The access signature for accessing the blob storage URL. | [optional] 
**jobs** | [**list[BlobAccessInformation]**](BlobAccessInformation.md) | The list of URLs and access signatures for accessing the results for the study jobs.  The list of job access information is at most the size of the number of shards, and jobs  beyond that can get their access information at the job index modulo the number of shards.  Each job&#39;s actual results will be in located located in a sub folder with the same name  as the job index. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


