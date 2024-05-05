──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) NVRAM Manager (NvM)* module, in functionality, API and configuration.
### Definitions
---
...
### Specification
---
#### Introduction
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
* Each NVRAM block specifies which memory abstraction module it shall be accessed through (i.e., *Fee*, *Ea*), to be used when calling *MemIf* API(s).
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
* If a non-`NULL` pointer is provided, then `NvM_ReadBlock` shall use this buffer instead of the permanent RAM block (if configured), or explicit synchronization callback(s) (if configured).
* If successful, the NVRAM block status is set to `NVM_REQ_OK`. Otherwise, it is set to `NVM_REQ_NOT_OK`.
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
	* At last, if the status of the reserved NVRAM block is not set to `NVM_REQ_OK`, the RAM block of the reserved NVRAM block is updated with the compiled configuration ID, and the NVRAM block is marked as `VALID-CHANGED`, to be written during the next `NvM_WriteAll`.

* `NvM_ReadAll`, when processing NVRAM blocks with ID `> 1` (in all other cases):
	* If *MemIf* reports `MEMIF_BLOCK_INVALID`, the NVRAM block status is set to `NVM_REQ_NV_INVALIDATED`.
	* If *MemIf* reports `MEMIF_BLOCK_INCONSISTENT`, or `MEMIF_JOB_OK` but CRC check fails, the NVRAM block status is set to `NVM_REQ_INTEGRITY_FAILED`.
	* If *MemIf* reports `MEMIF_JOB_NOT_OK`, the NVRAM block status is set to `NVM_REQ_NOT_OK`.
	* In any of the cases aforementioned, if the NVRAM block has either `NvMInitBlockCallback` or `NvMRomBlockDataAddress` configured, then the status is set to `NVM_REQ_RESTORED_DEFAULTS`, and the RAM block is updated from ROM.
		* *Note:* In this case, the NVRAM block is marked as `VALID-CHANGED`, to be written during the next `NvM_WriteAll`.
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

* ...
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
## *References*
---
[1] Specification of Flash Driver, AUTOSAR Classic Platform, R23-11