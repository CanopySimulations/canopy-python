# EncryptionReEncryptRequest

Contains the data to be re-encrypted and other options.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** | The data to be re-encrypted. | [optional] 
**sim_version** | **str** | The sim version of the data being re-encrypted.              This should match the sim version of the data, but also determines the encryption key used. | [optional] 
**decrypting_tenant_short_name** | **str** | The short name of the tenant which needs to decrypt the data.              The encryption key of this tenant will be used to encrypt the data. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


