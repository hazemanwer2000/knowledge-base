──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
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
* The module shall execute a single job at any time.
	* When busy, the module status is set to `MEMIF_BUSY`.
	* When idle, the module status is set to `MEMIF_IDLE`.
### API(s)
---
###### `Fls_Init`
---
```
Name: 'Fls_Init'
Description: Initializes the 'Fls' module.
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
	E_NOK - Request denied.	
```
*Note:* Arguments `[1]` and `[2]` must be multiple of the flash sector size.
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
	E_NOK - Request denied.	
```
*Note:* Arguments `[1]` and `[3]` must be multiple of the flash sector size.
###### `Fls_GetJobResult`
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
	E_NOK - Request denied.	
```
## *References*
---
[1] Specification of Flash Driver, AUTOSAR Classic Platform, R23-11