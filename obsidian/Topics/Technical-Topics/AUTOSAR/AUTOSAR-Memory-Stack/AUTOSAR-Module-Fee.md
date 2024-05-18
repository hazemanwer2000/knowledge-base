## *Table of Contents*
- [[#Definitions|Definitions]]
- [[#Specification|Specification]]
- [[#Function(s)|Function(s)]]
	- [[#Function(s)#API(s)|API(s)]]
			- [[#`Fee_Init`|`Fee_Init`]]
			- [[#`Fee_Read`|`Fee_Read`]]
			- [[#`Fee_Write`|`Fee_Write`]]
			- [[#`Fee_Cancel`|`Fee_Cancel`]]
			- [[#`Fee_GetStatus`|`Fee_GetStatus`]]
			- [[#`Fee_GetJobResult`|`Fee_GetJobResult`]]
			- [[#`Fee_InvalidateBlock`|`Fee_InvalidateBlock`]]
			- [[#`Fee_EraseImmediateBlock`|`Fee_EraseImmediateBlock`]]
	- [[#Function(s)#Scheduled Function(s)|Scheduled Function(s)]]
			- [[#`Fee_MainFunction`|`Fee_MainFunction`]]
	- [[#Function(s)#Callback Notification(s)|Callback Notification(s)]]
			- [[#`Fee_JobEndNotification`|`Fee_JobEndNotification`]]
			- [[#`Fee_JobErrorNotification`|`Fee_JobErrorNotification`]]
	- [[#Function(s)#Interface(s)|Interface(s)]]
			- [[#`NvM_JobEndNotification`|`NvM_JobEndNotification`]]
			- [[#`NvM_JobErrorNotification`|`NvM_JobErrorNotification`]]
- [[#Configuration|Configuration]]
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) Flash EEPROM Emulation (Fee)* module, in functionality, API and configuration.

The *Fls* module is its lower-layer module, and it presents an EEPROM-like interface for upper-layer modules.
### Definitions
---
* **Flash Virtual Page**: An integer multiple of the flash physical page, used by the *Fee* module.
### Specification
---
* The module shall reserve the minimum number of flash virtual pages for each configured block.
	* The maximum block *residue* is, therefore, the size of a flash virtual page minus one.
* The block number is a 16-bit value, with 0x0 and 0xFFFF being prohibited.
* The maximum block size is 0xFFFF (i.e., 64 kB).
* The module shall differentiate between an inconsistent (i.e., never written before, or written incompletely), invalid (i.e., invalidated using `Fee_InvalidateBlock`) and valid/consistent blocks.
	* *Note:* This means that additional management information must be stored in flash.
* The module shall support configuring a block as *immediate*.
	* The flash area of an immediate block may be erased, by invoking `Fee_EraseImmediateBlock`.
	* Hence, the next `Fee_Write` invocation on this block would not entail any invocation of `Fls_Erase`.

Additionally, similar to the *Fls* module,

* The module shall not provide any data integrity mechanism (e.g., checksum calculation).
* The module shall not buffer data, but rely on upper-layer provided buffers.
	* *Note:* The upper-layer is responsible for ensuring data consistency during the requested operation.
* The module shall execute a single job at any time, asynchronously.
	* When busy, the module status is set to `MEMIF_BUSY`.
	* When idle, the module status is set to `MEMIF_IDLE`.
* Job processing takes place within the `Fee_MainFunction`.
### Function(s)
---
#### API(s)
---
###### `Fee_Init`
---
```
Name: 'Fee_Init'
Description: Initializes the module.
Sync/Async: Async
Re-entrant: No
Parameters (in):
	[1] Pointer to module cfg.
```
###### `Fee_Read`
---
```
Name: 'Fee_Read'
Description: Reads a block.
Sync/Async: Async
Re-entrant: No
Parameters (in):
	[1] Block number.
	[2] Offset, to read from.
	[3] Length to read.
Parameters (out):
	[1] Dest. pointer (i.e., data buffer pointer).
```
###### `Fee_Write`
---
```
Name: 'Fee_Write'
Description: Write a block.
Sync/Async: Async
Re-entrant: No
Parameters (in):
	[1] Block number.
	[2] Source. pointer (i.e., data buffer pointer).
```
###### `Fee_Cancel`
---
```
Name: 'Fee_Cancel'
Description: (...)
Sync/Async: Async
Re-entrant: No
...
```
###### `Fee_GetStatus`
---
```
Name: 'Fee_GetStatus'
Description: (...)
Sync/Async: Sync
Re-entrant: No
...
```
###### `Fee_GetJobResult`
---
```
Name: 'Fee_GetJobResult'
Description: (...)
Sync/Async: Sync
Re-entrant: No
Return:
	...
	MEMIF_BLOCK_INCONSISTENT - Requested block is inconsistent.
	MEMIF_BLOCK_INVALID - Requested block is invalid.
```
###### `Fee_InvalidateBlock`
---
```
Name: 'Fee_InvalidateBlock'
Description: (...)
Sync/Async: Async
Re-entrant: No
Parameters (in):
	[1] Block number.
```
###### `Fee_EraseImmediateBlock`
---
```
Name: 'Fee_EraseImmediateBlock'
Description: Erase the flash area of an immediate block. 
Sync/Async: Async
Re-entrant: No
Parameters (in):
	[1] Block number.
```
#### Scheduled Function(s)
---
###### `Fee_MainFunction`
---
```
Name: 'Fee_MainFunction'
Description: (...)
```
#### Callback Notification(s)
---
###### `Fee_JobEndNotification`
---
```
Name: 'Fee_JobEndNotification'
Description: (...)
```
###### `Fee_JobErrorNotification`
---
```
Name: 'Fee_JobErrorNotification'
Description: (...)
```
#### Interface(s)
---
###### `NvM_JobEndNotification`
---
```
Name: 'NvM_JobEndNotification'
Description: Notifies the 'NvM' module that a job has ended successfully.
Interface Type: Configurable
```
###### `NvM_JobErrorNotification`
---
```
Name: 'NvM_JobErrorNotification'
Description: Notifies the 'NvM' module that a job has failed.
Interface Type: Configurable
```
### Configuration
---
```
FeeGeneral [C, 1]
	FeeMainFunctionPeriod [P]
	FeeNvMJobEndNotification [P]
	FeeNvMJobErrorNotification [P]
	FeeVirtualPageSize [P]

FeeBlockConfiguration [C, 1..*]
	FeeBlockNumber [P]
	FeeBlockSize [P]
	FeeImmediateData [P]
```
## *References*
---
[1] Specification of Flash EEPROM Emulation, AUTOSAR Classic Platform, R20-11