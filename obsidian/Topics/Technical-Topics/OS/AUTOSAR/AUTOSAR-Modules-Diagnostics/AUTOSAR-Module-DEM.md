──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) Diagnostic Event Manager (DEM)* module, which resides in the Service layer, in functionality, API and configuration.
### Specification
---

### Configuration
---
```
DemGeneral [C, 1]
	DemAgingRequiresNotFailedCycle [P]
	DemAgingRequiresTestedCycle [P]
	DemClearDTCBehavior [P]
	DemClearDTCLimitation [P]

	DemClient [C, 1..*]
		DemClientId [P]
		DemEventMemorySetRef [R, 1]

	DemEventMemorySet [C, 1..*]

		DemPrimaryMemory [C, 1]
			DemEventDisplacementStrategy [P]
			DemEventMemoryEntryStorageTrigger [P]
			DemMaxNumberEventEntryPrimary [P]

				DemGroupOfDTC [C, 0..*]
					DemGroupOfDTCs [P]

		DemUserDefinedMemory [C, 0..*]
			DemEventDisplacementStrategy [P]
			DemEventMemoryEntryStorageTrigger [P]
			DemMaxNumberEventEntryUserDefined [P]
			DemUserDefinedMemoryIdentifier [P]

				DemGroupOfDTC [C, 0..*]
					DemGroupOfDTCs [P]

	DemOperationCycle [C, 1..*]
		DemOperationCycleId [P]

	DemDataElementClass [C, 0..*]
	DemDidClass [C, 0..*]
	DemExtendedDataClass [C, 0..*]
	DemExtendedDataRecordClass [C, 0..*]
	DemFreezeFrameClass [C, 0..*]
	DemEnableCondition [C, 0..*]
	DemEnableConditionGroup [C, 0..*]
	DemStorageCondition [C, 0..*]
	DemStorageConditionGroup [C, 0..*]

DemConfigSet [C, 1]
```
###### `DemGeneral`
---
```
Path: DemGeneral/DemClearDTCBehavior
Description: Specifies when a client is notified of 'ClearDTC' operation completion.
Range:
	NONVOLATILE_FINISH
	NONVOLATILE_TRIGGER
	VOLATILE
```

```
Path: DemGeneral/DemClearDTCLimitation
Description: Specifies which DTC value(s) are supported for 'ClearDTC' operation.
Range:
	ALL_SUPPORTED_DTCS
	ONLY_CLEAR_ALL_DTCS
```
###### `DemPrimaryMemory`
---
```
Path: DemGeneral/DemEventMemorySet/DemPrimaryMemory/DemEventMemoryEntryStorageTrigger
Range:
	TRIGGER_ON_CONFIRMED
	TRIGGER_ON_TEST_FAILED
	TRIGGER_ON_FDC_THRESHOLD
```
## References
---
[1] Specification of Diagnostic Event Manager (DEM), AUTOSAR Classic Platform, R20-11