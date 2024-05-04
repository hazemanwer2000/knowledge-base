──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#Definitions|Definitions]]
- [[#Specification|Specification]]
- [[#Function(s)|Function(s)]]
	- [[#Function(s)#API(s)|API(s)]]
			- [[#`Fls_Init`|`Fls_Init`]]
			- [[#`Fls_Erase`|`Fls_Erase`]]
			- [[#`Fls_Write`|`Fls_Write`]]
			- [[#`Fls_Read`|`Fls_Read`]]
			- [[#`Fls_Cancel`|`Fls_Cancel`]]
			- [[#`Fls_GetJobResult`|`Fls_GetJobResult`]]
			- [[#`Fls_GetStatus`|`Fls_GetStatus`]]
			- [[#`Fls_SetMode`|`Fls_SetMode`]]
	- [[#Function(s)#Scheduled Function(s)|Scheduled Function(s)]]
			- [[#`Fls_MainFunction`|`Fls_MainFunction`]]
	- [[#Function(s)#Interface(s)|Interface(s)]]
			- [[#`Fee_JobEndNotification`|`Fee_JobEndNotification`]]
			- [[#`Fee_JobErrorNotification`|`Fee_JobErrorNotification`]]
- [[#Configuration|Configuration]]
			- [[#`FlsGeneral`|`FlsGeneral`]]
			- [[#`FlsConfigSet`|`FlsConfigSet`]]
			- [[#`FlsSectorList`|`FlsSectorList`]]
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) Flash Driver (Fls)* module, in functionality, API and configuration.
### Definitions
---
* **Flash Sector:** Smallest amount of flash memory that can be erased in one pass.
* **Flash Page**: Smallest amount of flash memory that can be written (i.e., programmed) in one pass.
### Specification
---
* The module shall only erase a whole sector, or write a whole page.
* The module shall not provide any data integrity mechanism (e.g., checksum calculation).
* The module shall not buffer data, but rely on upper-layer provided buffers.
	* *Note:* The upper-layer is responsible for ensuring data consistency during the requested operation.
* The module shall combine all available flash memory regions into one linear (i.e., virtual) address space.
* The module shall execute a single job at any time, asynchronously.
	* When busy, the module status is set to `MEMIF_BUSY`.
	* When idle, the module status is set to `MEMIF_IDLE`.
* Job processing takes place within the `Fls_MainFunction`.
	* The number of bytes read/written within `Fls_MainFunction` shall be dependent on the current module mode, either `MEMIF_MODE_SLOW` or `MEMIF_MODE_FAST`.
### Function(s)
---
#### API(s)
---
###### `Fls_Init`
---
```
Name: 'Fls_Init'
Description: Initializes the module.
Sync/Async: Sync
Re-entrant: No
Parameters (in):
	[1] Pointer to the 'Fls' cfg.
```
###### `Fls_Erase`
---
```
Name: 'Fls_Erase'
Description: Erases flash sector(s).
Sync/Async: Async
Re-entrant: No
Parameters (in):
	[1] Target (virtual) flash address.
	[2] Length.
Return:
	E_OK - Request accepted.
	...
```
*Note:* Arguments `IN[1]` and `IN[2]` must be multiple of the flash sector size.
###### `Fls_Write`
---
```
Name: 'Fls_Write'
Description: Write flash page(s).
Sync/Async: Async
Re-entrant: No
Parameters (in):
	[1] Target (virtual) flash address.
	[2] Source pointer (i.e., data buffer pointer).
	[3] Length.
Return:
	E_OK - Request accepted.
	...	
```
*Note:* Arguments `IN[1]` and `IN[3]` must be multiple of the flash page size.
###### `Fls_Read`
---
```
Name: 'Fls_Read'
Description: Read from flash memory.
Sync/Async: Async
Re-entrant: No
Parameters (in):
	[1] Target (virtual) flash address.
	[2] Length.
Parameters (out):
	[1] Source pointer (i.e., data buffer pointer).
```
###### `Fls_Cancel`
---
```
Name: 'Fls_Cancel'
Description: Cancel the last-requested job.
Sync/Async: Sync
Re-entrant: No
	...
```
###### `Fls_GetJobResult`
---
```
Name: 'Fls_GetJobResult'
Description: Get the status of the last-requested job.
Sync/Async: Sync
Re-entrant: Yes
Return:
	MEMIF_JOB_OK - The job was successful.
	MEMIF_JOB_FAILED - The job failed.
	MEMIF_JOB_PENDING - The job has not yet finished.
	MEMIF_JOB_CANCELLED - The job has been cancelled.
	...
```
###### `Fls_GetStatus`
---
```
Name: 'Fls_GetStatus'
Description: Get the status of the module.
Sync/Async: Sync
Re-entrant: Yes
Return:
	MEMIF_UNINIT - Not yet initialized.
	MEMIF_IDLE - Idle, ready for a new request.
	MEMIF_BUSY - Busy, not ready for a new request.
	...
```
###### `Fls_SetMode`
---
```
Name: 'Fls_SetMode'
Description: Set the mode of the module.
Sync/Async: Sync
Re-entrant: No
Parameters (in):
	[1] Mode.
	...
```
#### Scheduled Function(s)
---
###### `Fls_MainFunction`
---
```
Name: 'Fls_MainFunction'
Description: Performs job processing.
```
#### Interface(s)
---
###### `Fee_JobEndNotification`
---
```
Name: 'Fee_JobEndNotification'
Description: Notifies the 'Fee' module that a job has ended successfully.
Interface Type: Configurable
```
###### `Fee_JobErrorNotification`
---
```
Name: 'Fee_JobErrorNotification'
Description: Notifies the 'Fee' module that a job has failed.
Interface Type: Configurable
```
### Configuration
---
```
FlsGeneral [C, 1]
	FlsTotalSize [P]
	FlsDriverIndex [P]
	FlsMainFunctionPeriod [P]
	
FlsConfigSet [C, 1]
	FlsAcErase [P]
	FlsAcWrite [P]
	FlsDefaultMode [P]
	FlsJobEndNotification [P]
	FlsJobErrorNotification [P]
	FlsMaxReadFastMode [P]
	FlsMaxReadNormalMode [P]
	FlsMaxWriteFastMode [P]
	FlsMaxWriteNormalMode [P]

	FlsSectorList [C, 1]
		FlsSector [C, 1..*]
			FlsNumberOfSectors [P]
			FlsPageSize [P]
			FlsSectorSize [P]
			FlsSectorStartAddress [P]
```
###### `FlsGeneral`
---
```
Path: FlsGeneral/FlsTotalSize
Description: Total size of the flash available.
```

```
Path: FlsGeneral/FlsDriverIndex
Description: Driver index, used by 'Fee' module.
```

```
Path: FlsGeneral/FlsMainFunctionPeriod
Description: Period of the main function.
```
###### `FlsConfigSet`
---
```
Path: FlsConfigSet/FlsAcXXX
Description: Address in RAM, in which the XXX-flash access code shall be loaded.
				Used as a function pointer.
```

```
Path: FlsConfigSet/FlsDefaultMode
Description: Default module mode.
```

```
Path: FlsConfigSet/FlsJobXXXNotification
Description: Specifies the (XXX)-notification configurable interface.  
```

```
Path: FlsConfigSet/FlsMaxXXXYYYMode
Description: Specifies the maximum number of bytes to (XXX) in one cycle,
				in (YYY) mode.
```

```
Path: FlsConfigSet/FlsSectorList
Description: Lists all flash regions.
```
###### `FlsSectorList`
---
```
Path: FlsConfigSet/FlsSectorList/FlsSector
Description: Describes a contiguous flash region.
```
## *References*
---
[1] Specification of Flash Driver, AUTOSAR Classic Platform, R23-11