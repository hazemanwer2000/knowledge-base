──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*

- [[#Specification|Specification]]
	- [[#Specification#Addressing|Addressing]]
- [[#Function(s)|Function(s)]]
	- [[#Function(s)#Synchronous Request(s)|Synchronous Request(s)]]
			- [[#`NvM_Init`|`NvM_Init`]]
			- [[#`NvM_GetErrorStatus`|`NvM_GetErrorStatus`]]
			- [[#`NvM_SetRamBlockStatus`|`NvM_SetRamBlockStatus`]]
	- [[#Function(s)#Asynchronous Single-Block Request(s)|Asynchronous Single-Block Request(s)]]
			- [[#`NvM_ReadBlock`|`NvM_ReadBlock`]]
			- [[#`NvM_WriteBlock`|`NvM_WriteBlock`]]
			- [[#`NvM_RestoreBlockDefaults`|`NvM_RestoreBlockDefaults`]]
			- [[#`NvM_EraseNvBlock`|`NvM_EraseNvBlock`]]
			- [[#`NvM_InvalidateNvBlock`|`NvM_InvalidateNvBlock`]]
	- [[#Function(s)#Asynchronous Multi-Block Request(s)|Asynchronous Multi-Block Request(s)]]
			- [[#`NvM_ReadAll`|`NvM_ReadAll`]]
			- [[#`NvM_WriteAll`|`NvM_WriteAll`]]
			- [[#`NvM_CancelWriteAll`|`NvM_CancelWriteAll`]]
			- [[#`NvM_ValidateAll`|`NvM_ValidateAll`]]
			- [[#`NvM_FirstInitAll`|`NvM_FirstInitAll`]]
	- [[#Function(s)#Scheduled Function(s)|Scheduled Function(s)]]
			- [[#`NvM_MainFunction`|`NvM_MainFunction`]]
	- [[#Function(s)#Callback Notification(s)|Callback Notification(s)]]
			- [[#`NvM_JobEndNotification`|`NvM_JobEndNotification`]]
			- [[#`NvM_JobErrorNotification`|`NvM_JobErrorNotification`]]
- [[#Data Types|Data Types]]
			- [[#`NvM_RequestResultType`|`NvM_RequestResultType`]]
- [[#Configuration|Configuration]]
			- [[#`NvMCommon`|`NvMCommon`]]
			- [[#`NvMBlockDescriptor`|`NvMBlockDescriptor`]]
- [[#Additional Features|Additional Features]]
	- [[#Additional Features#Configuration: `NvMStaticBlockIDCheck`|Configuration: `NvMStaticBlockIDCheck`]]
	- [[#Additional Features#Configuration: `NvMWriteVerification`|Configuration: `NvMWriteVerification`]]
	- [[#Additional Features#Configuration: `NvMCalcRamBlockCrc`|Configuration: `NvMCalcRamBlockCrc`]]
	- [[#Additional Features#Configuration: `NvMBlockUseCRCCompMechanism`|Configuration: `NvMBlockUseCRCCompMechanism`]]
	- [[#Additional Features#Job Priority and Queuing|Job Priority and Queuing]]
	- [[#Additional Features#Dataset NVRAM Block(s)|Dataset NVRAM Block(s)]]
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) NVRAM Manager (NvM)* module, in functionality, API and configuration.
### Specification
---
* The module shall manage entities, called *NVRAM blocks*. Each NVRAM block constitutes of a number of  *basic storage objects*. There are four types of *basic storage objects*:
	* *RAM block*, which represents the part of the NVRAM block that resides in RAM.
	* *NV block*, which represents the part of the NVRAM block that resides in NV memory.
	* *ROM block*, which represents the part of the NVRAM block that resides in ROM.
	* *Administrative block*, which is used to store run-time management information about the NVRAM block. It resides in RAM.

* Each NVRAM block has a *block management type*. There are three different block management types:
	* `NVM_BLOCK_NATIVE`, which mandates:
		```
		RAM block(s): 1
		NV Block(s): 1
		ROM block(s): 0..1
		Admininstrative block(s): 1
		```
	* `NVM_BLOCK_REDUNDANT`, which mandates:
		```
		RAM block(s): 1
		NV Block(s): 2
		ROM block(s): 0..1
		Admininstrative block(s): 1
		```
	* `NVM_BLOCK_DATASET`, discussed later.
#### Addressing
---
* Each NVRAM block has a base number. To calculate the address required to access an NV block using *MemIf* API(s),
	```
	MemIf Block Number = 
		(NVRAM Block Base Number << Data Selection Bits) + NV Block Index 
	```
* Each NVRAM block specifies which memory abstraction module it shall be accessed through (e.g., *Fee*), to be used when calling *MemIf* API(s).
### Function(s)
---
#### Synchronous Request(s)
---
###### `NvM_Init`
---
```
Name: 'NvM_Init'
Description: Initializes the module.
Re-entrant: No
Parameters (in):
	[1] Pointer to module cfg.
```
###### `NvM_GetErrorStatus`
---
```
Name: 'NvM_GetErrorStatus'
Description: Gets the status of the last-requested async. job, executed on the referenced block.
Re-entrant: Yes
Parameters (in):
	[1] NVRAM block ID.
Parameters (out):
	[1] Pointer to buffer [Type: NvM_RequestResultType].
```

*Additional notes:*

* To get the status of the last-requested multi-block async. job, block ID zero (reserved) is used.
###### `NvM_SetRamBlockStatus`
---
```
Name: 'NvM_SetRamBlockStatus'
Description: Marks an NVRAM block as either 'VALID-CHANGED' (i.e., true), and vice-versa.
Re-entrant: Yes
Parameters (in):
	[1] NVRAM block ID.
	[2] Boolean, whether block changed.
```
#### Asynchronous Single-Block Request(s)
###### `NvM_ReadBlock`
---
```
Name: 'NvM_ReadBlock'
Description: Attempts to read an NVRAM block (i.e., load from NV to RAM) [see further below].
Re-entrant: Yes
Parameters (in):
	[1] NVRAM block ID.
Parameters (out):
	[1] Pointer to buffer.
```

*Additional notes:*

* If a non-`NULL` pointer is provided, then `NvM_ReadBlock` shall use this buffer instead of the permanent RAM block (if configured), or explicit synchronization callback(s) (if configured).

* `NvM_ReadBlock` behaves similar to how `NvM_ReadAll` does for NVRAM blocks (i.e., if configuration ID (mis-)matches were irrelevant).
###### `NvM_WriteBlock`
---
```
Name: 'NvM_WriteBlock'
Description: Attempts to write an NVRAM block (i.e., store from RAM to NV) [see further below].
Re-entrant: Yes
Parameters (in):
	[1] NVRAM block ID.
	[2] Pointer to buffer.
```

*Additional notes:*

* If a non-`NULL` pointer is provided, then `NvM_WriteBlock` shall use this buffer instead of the permanent RAM block (if configured), or explicit synchronization callback(s) (if configured).

* If successful, the NVRAM block status is set to `NVM_REQ_OK`. Otherwise, it is set to `NVM_REQ_NOT_OK`.
###### `NvM_RestoreBlockDefaults`
---
```
Name: 'NvM_RestoreBlockDefaults'
Description: For the NVRAM block referenced, read into the RAM block from ROM.
Re-entrant: No
Parameters (in):
	[1] NVRAM block ID.
Parameters (out):
	[2] Pointer to buffer.
```

*Additional notes:*

* If a non-`NULL` pointer is provided, then `NvM_RestoreBlockDefaults` shall use this buffer instead of the permanent RAM block (if configured), or explicit synchronization callback(s) (if configured).

* If successful, the NVRAM block status is set to `NVM_REQ_OK`, in which case, if a `NULL` pointer was provided, the NVRAM block is marked as `VALID-CHANGED`. Otherwise, it is set to `NVM_REQ_NOT_OK`.
###### `NvM_EraseNvBlock`
---
```
Name: 'NvM_EraseNvBlock'
Description: For the NVRAM block referenced, erase associated NV block(s).
Re-entrant: No
Parameters (in):
	[1] NVRAM block ID.
```
###### `NvM_InvalidateNvBlock`
---
```
Name: 'NvM_InvalidateNvBlock'
Description: For the NVRAM block referenced, invalidate the associated NV block(s).
Re-entrant: No
Parameters (in):
	[1] NVRAM block ID.
```
#### Asynchronous Multi-Block Request(s)
---
###### `NvM_ReadAll`
---
```
Name: 'NvM_ReadAll'
Description: Attempts to read all NVRAM blocks (i.e., load from NV to RAM) [see further below], usually executed on start-up.
Re-entrant: No
```

*Additional notes:*

* `NvM_ReadAll` processes only NVRAM blocks that meet the following requirements:
	* The NVRAM block is configured with, either, a permanent RAM block, or explicit synchronization callback(s).
	* The NVRAM block is configured to be processed in `NvM_ReadAll` (i.e., `NvMSelectBlockForReadAll = True`).

* NVRAM block ID one is reserved for the NVRAM block that stores the module's configuration ID. 
	* This block must be of block management type `NVM_BLOCK_REDUNDANT`, and uses CRC.
		* If the reserved NVRAM block couldn't be read due to an error in the lower-layer(s), its status is set to `NVM_REQ_NV_INVALIDATED`.
			* In this case, the behavior is as if a configuration match occurred.
		* If the reserved NVRAM block fails CRC check, its status is set to `NVM_REQ_INTEGRITY_FAILED`.
			* In this case, the behavior is as if a configuration mismatch occurred.
		* If the reserved NVRAM block is read successfully, but a configuration ID mismatch is detected, its status is set to `NVM_REQ_NOT_OK`.
		* Otherwise, its status is set to `NVM_REQ_OK`.
	* In case of configuration ID mismatch, for NVRAM blocks with ID `> 1`, if,
		* `NvMDynamicConfiguration = True`, and,
		* the block is configured as `NvMResistantToChangedSw = False`, and,
		* the block is configured with either `NvMInitBlockCallback` or `NvMRomBlockDataAddress`,
		* then, the RAM block is restored to its default value (from ROM), its status is set to `NVM_REQ_RESTORED_DEFAULTS`.
	* At last, if the status of the reserved NVRAM block is not set to `NVM_REQ_OK`, the RAM block of the reserved NVRAM block is updated with the compiled configuration ID, and the NVRAM block is marked as `VALID-CHANGED`.

* `NvM_ReadAll`, when processing NVRAM blocks with ID `> 1` (in all other cases):
	* If *MemIf* reports `MEMIF_BLOCK_INVALID`, the NVRAM block status is set to `NVM_REQ_NV_INVALIDATED`.
	* If *MemIf* reports `MEMIF_BLOCK_INCONSISTENT`, or `MEMIF_JOB_OK` but CRC check fails, the NVRAM block status is set to `NVM_REQ_INTEGRITY_FAILED`.
	* If *MemIf* reports `MEMIF_JOB_NOT_OK`, the NVRAM block status is set to `NVM_REQ_NOT_OK`.
	* In any of the cases aforementioned, if the NVRAM block has either `NvMInitBlockCallback` or `NvMRomBlockDataAddress` configured, then the status is set to `NVM_REQ_RESTORED_DEFAULTS`, and the RAM block is updated from ROM.
		* *Note:* In this case, the NVRAM block is marked as `VALID-CHANGED`.
	* Otherwise, the NVRAM block status is set to `NVM_REQ_OK`, and the RAM block is updated from the NV block.

* The multi-block request status is set to `NVM_REQ_OK` if all relevant NVRAM block statuses are also set to `NVM_REQ_OK`. Otherwise, it is set to `NVM_REQ_NOT_OK`.

*Note:* The design of the *NvM* module uses the status of the NVRAM block inconsistently (i.e., between NVRAM blocks with ID `= 1` and `> 1`).
###### `NvM_WriteAll`
---
```
Name: 'NvM_WriteAll'
Description: Attempts to write all NVRAM blocks (i.e., store from RAM to NV) [see further below], usually executed on shutdown.
Re-entrant: No
```

*Additional notes:*

* `NvM_WriteAll` processes only NVRAM blocks that meet the following requirements:
	* The NVRAM block is configured with, either, a permanent RAM block, or explicit synchronization callback(s).
	* The NVRAM block is configured to be processed in `NvM_WriteAll` (i.e., `NvMSelectBlockForWriteAll = True`).

* For each `VALID-CHANGED` NVRAM block, if successful, the NVRAM block status is set to `NVM_REQ_OK`. Otherwise, it is set to `NVM_REQ_NOT_OK`. 
	* *Note:* For each non-`VALID-CHANGED` NVRAM block, the NVRAM block status is set to `NVM_REQ_BLOCK_SKIPPED`.
###### `NvM_CancelWriteAll`
---
```
Name: 'NvM_CancelWriteAll'
Description: Cancels an on-going `NvM_WriteAll` request.
Re-entrant: No
```

*Additional notes:*

* When `NvM_CancelWriteAll` is requested, the current NVRAM block being handled is processed to completion. The status of all remaining NVRAM blocks is set to `NVM_REQ_CANCELED`, as well as, the multi-block request status.
###### `NvM_ValidateAll`
---
```
Name: 'NvM_ValidateAll'
Description: Mark all (applicable [see below]) NVRAM blocks as 'VALID-CHANGED'.
Re-entrant: No
```

*Additional notes:*

* `NvM_ValidateAll` processes only NVRAM blocks that meet the following requirements:
	* The NVRAM block is configured with, either, a permanent RAM block, or explicit synchronization callback(s).
	* The NVRAM block is configured with `NvMBlockUseAutoValidation = True`.
###### `NvM_FirstInitAll`
---
```
Name: 'NvM_FirstInitAll'
Description: Write all NV and RAM blocks with data from ROM, for (applicable [see below]) NVRAM blocks, or invalidate NV blocks if missing from ROM.
Re-entrant: No
```

*Additional notes:*

* Usually, if this request is made, it is executed before `NvM_ReadAll`.

* `NvM_FirstInitAll` deals only with NVRAM blocks configured with `NvMSelectBlockForFirstInitAll = True`.
#### Scheduled Function(s)
---
###### `NvM_MainFunction`
---
```
Name: 'NvM_MainFunction'
Description: Performs job processing.
```
#### Callback Notification(s)
---
###### `NvM_JobEndNotification`
---
```
Name: 'NvM_JobEndNotification'
Description: Notifies the 'NvM' module that a job has ended successfully.
```
###### `NvM_JobErrorNotification`
---
```
Name: 'NvM_JobErrorNotification'
Description: Notifies the 'NvM' module that a job has failed.
```
### Data Types
---
###### `NvM_RequestResultType`
---
```
Name: NvM_RequestResultType
Range:
	NVM_REQ_OK
	NVM_REQ_NOT_OK 
	NVM_REQ_PENDING
	NVM_REQ_INTEGRITY_FAILED  
	NVM_REQ_BLOCK_SKIPPED
	NVM_REQ_NV_INVALIDATED
	NVM_REQ_CANCELED
	NVM_REQ_RESTORED_DEFAULTS
```
### Configuration
---
```
NvMCommon [C, 1]
	NvMCompiledConfigId [P]
	NvMCrcNumOfBytes [P]
	NvMDatasetSelectionBits [P]
	NvMDrvModeSwitch [P]
	NvMDynamicConfiguration [P]
	NvMMainFunctionPeriod [P]
	NvMMultiBlockCallback [P]

NvMBlockDescriptor [C, 1..*]
	NvMBlockUseCrc [P]
	NvMBlockCrcType [P]
	NvMBlockHeaderInclude [P]
	NvMBlockManagementType [P]
	NvMResistantToChangedSw [P]
	NvMBlockUseAutoValidation [P]
	NvMBlockUseSyncMechanism [P]
	NvMNvBlockBaseNumber [P]
	NvMNvBlockLength [P]
	NvMNvramBlockIdentifier [P]
	NvMNvramDeviceId [P]
	NvMRamBlockDataAddress [P]
	NvMReadRamBlockFromNvCallback [P]
	NvMWriteRamBlockToNvCallback [P]
	NvMRomBlockDataAddress [P]
	NvMSelectBlockForFirstInitAll [P]
	NvMSelectBlockForReadAll [P]
	NvMSelectBlockForWriteAll [P]

	NvMInitBlockCallback [C, 0..1]
		NvMInitBlockCallbackFnc [P]
		
	NvMSingleBlockCallback [C, 0..1]
		NvMSingleBlockCallbackFnc [P]

	NvMTargetBlockReference [C, 1]
		NvMFeeRef [R, 0..1]
		NvMEaRef [R, 0..1]
```
###### `NvMCommon`
---
```
Path: NvMCommon/NvMCrcNumOfBytes
Description: The maximum number of bytes to process, when calculating the CRC, within every cycle (i.e., main function call).
```

```
Path: NvMCommon/NvMDatasetSelectionBits
Description: The number of dataset selection bits (0 to 8).
```

```
Path: NvMCommon/NvMDrvModeSwitch
Description: Enables switching memory drivers to fast mode, while executing 'NvM_ReadAll' and 'NvM_WriteAll'.
```
###### `NvMBlockDescriptor`
---
```
Path: NvMBlockDescriptor/NvMBlockCrcType
Description: CRC type used, if 'NvMBlockUseCrc = True' [CRC8, CRC16, CRC32].
```

```
Path: NvMBlockDescriptor/NvMBlockHeaderInclude
Description: Header file that contains declarations of any RAM/ROM variable, or callback functions, referenced in this NVRAM block.
```

```
Path: NvMBlockDescriptor/NvMBlockUseSyncMechanism
Description: Enables explicit synchronization for this NVRAM block.
```
### Additional Features
---
#### Configuration: `NvMStaticBlockIDCheck` 
---
* For each NVRAM block, if `NvMStaticBlockIDCheck = True`, then the ID of the NVRAM block becomes part of the NV block.
* When reading the NV block, the stored block ID is compared to the configured block ID, as an additional mechanism to detect hardware failures (i.e., in-addition to CRC check).
#### Configuration: `NvMWriteVerification` 
---
* For each NVRAM block, if `NvMWriteVerification = True`, then after a write request is executed, the NV block is read back and compared to the RAM block.
	* *Note:* Each cycle, `NvMWriteVerificationDataSize` bytes are compared.
#### Configuration: `NvMCalcRamBlockCrc` 
---
* For each NVRAM block, if `NvMCalcRamBlockCrc = True`, then a CRC value is maintained for the RAM block.
* During `NvM_ReadAll`, RAM blocks (that belong to applicable NVRAM blocks) with valid CRC will not be updated.
* During `NvM_WriteAll`, an (applicable) NVRAM block with a RAM block with invalid CRC is not written successfully.
* `NvM_SetRamBlockStatus` API is used to trigger RAM block CRC re-calculation, upon modification of the RAM block.
#### Configuration: `NvMBlockUseCRCCompMechanism` 
---
* For each NVRAM block, if `NvMBlockUseCRCCompMechanism = True`, then, any write request is skipped if the calculated CRC of the RAM block is equal to the CRC in the NV block.
#### Job Priority and Queuing
---
* If `NvMCommon/NvMJobPrioritization = True`, the module shall maintain two separate queues; one for immediate (i.e., `NvMBlockDescriptor/NvMBlockJobPriority = 0`) (async.) single-block write requests, and another for all other single-block requests.
	* The size of both queues is determined by `NvMCommon/NvMSizeImmediateJobQueue` and `NvMCommon/NvMSizeStandardJobQueue`, respectively.
	* Immediate single-block write requests (i.e., from the first queue) are prioritized, and may preempt any other executing single-block request (i.e., from the second queue).
	* Further prioritization between requests is determined by `NvMBlockDescriptor/NvMBlockJobPriority`.

* If `NvMCommon/NvMJobPrioritization = False`, the module shall maintain only a single queue.
	* The size of the queue is determined by `NvMCommon/NvMSizeStandardJobQueue`.

* Multi-block requests are maintained in a separate queue, of size one. For a multi-block request to execute, all other queues must be empty. However, multi-block requests may not be preempted, except by immediate single-block write requests.

* The `NvM_CancelJobs` synchronous request may be used to cancel all pending jobs for a specific NVRAM block.
	* *Notes*: A single async. request must execute to completion, before another single async. request can be issued, if both reference the same NVRAM block (i.e., with the same ID).
#### Dataset NVRAM Block(s)
---
* A *dataset* NVRAM block (i.e., with block management type set to `NVM_BLOCK_DATASET`) mandates:
	```
	RAM block(s): 1
	NV Block(s): 1..*
	ROM block(s): 0..*
	Admininstrative block(s): 1
	```
	* `NvMBlockDescriptor/NvMNvBlockNum`, and `NvMBlockDescriptor/NvMRomBlockNum` denote the number of NV and ROM block(s), respectively.

* Both `NvM_ReadAll`, and `NvM_WriteAll` ignore dataset NVRAM blocks.

* Inside its administration block, a *data index* is maintained, that points at a specific NV/ROM block.
	* The data index may be set to any value from `0` to `NvMNvBlockNum - 1`, to access NV blocks, or from `NvMNvBlockNum` to `NvMNvBlockNum + NvMRomBlockNum - 1`, to access ROM blocks.
	* `NvM_Init` sets the data index for all dataset NVRAM blocks to zero.
	* `NvM_(Set/Get)DataIndex` API(s) may be used to set/get the data index of an NVRAM block.
	* During `NvM_ReadBlock`, the referenced NV/ROM block is read from, to the RAM block.
	* During `NvM_WriteBlock`, the referenced NV block is written to, from the RAM block.
## *References*
---
[1] Specification of Flash Driver, AUTOSAR Classic Platform, R20-11