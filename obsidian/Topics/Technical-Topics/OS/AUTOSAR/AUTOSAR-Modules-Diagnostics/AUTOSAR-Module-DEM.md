──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) Diagnostic Event Manager (DEM)* module, which resides in the Service layer, in functionality, API and configuration.
### Specification
---
...
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

	DemEnableCondition [C, 0..*]
		DemEnableConditionId [P]
		DemEnableConditionStatus [P]

	DemEnableConditionGroup [C, 0..*]
		DemEnableConditionRef [R, 1..*]

	DemStorageCondition [C, 0..*]
		DemStorageConditionId [P]
		DemStorageConditionStatus [P]

	DemStorageConditionGroup [C, 0..*]
		DemStorageConditionRef [R, 1..*]

	DemDataElementClass [C, 0..*]
		...

	DemDidClass [C, 0..*]
		DemDidIdentifier [P]
		DemDidDataElementClassRef [R, 1..*]

	DemFreezeFrameClass [C, 0..*]
		DemDidClassRef [R, 1..*]

	DemExtendedDataRecordClass [C, 0..*]
		DemExtendedDataRecordNumber [P]
		DemExtendedDataRecordTrigger [P]
		DemExtendedDataRecordUpdate [P]
		DemDataElementClassRef [R, 1..*]
	
	DemExtendedDataClass [C, 0..*]
		DemExtendedDataRecordClassRef [R, 1..*]

DemConfigSet [C, 1]

	DemEventParameter [C, 1..*]
		DemEventId [P]
		DemEventConfirmationThreshold [P]
		DemDTCRef [R, 1]
		DemEnableConditionGroupRef [R, 0..1]
		DemStorageConditionGroupRef [R, 0..1]
		DemOperationCycleRef [R, 1]
		
		DemDebounceAlgorithmClass [C, 1]
			...

	DemDTC [C, 1..*]
		DemDTCValue [P]
		DemNVStorageStrategy [P]
		DemDTCAttributesRef [R, 1]

	DemDTCAttributes [C, 1..*]
		DemDTCPriority [P]
		DemMaxNumberFreezeFrameRecords [P]
		DemAgingAllowed [P]
		DemAgingCycleCounterThreshold [P]
		DemAgingCycleRef [R, 1]
		DemFreezeFrameClassRef [R, 0..1]
		DemExtendedDataClassRef [R, 0..1]
		DemMemoryDestinationRef [R, 1]
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
###### `Dem<..>Memory`
---
```
Path: DemGeneral/DemEventMemorySet/Dem<..>Memory/DemEventMemoryEntryStorageTrigger
Range:
	TRIGGER_ON_CONFIRMED
	TRIGGER_ON_TEST_FAILED
	TRIGGER_ON_FDC_THRESHOLD
```
###### `Dem<..>Condition`
---
```
Path: DemGeneral/Dem<..>Condition/Dem<..>ConditionStatus
Description: Defines whether the condition is initialized as 'True', or 'False', upon start-up.
```
###### `DemDataElementClass`
---
```
Description: Specifies an internal, or an external data element.
```
###### `DemExtendedDataRecordClass`
---
```
Path: DemGeneral/DemExtendedDataRecordClass/DemExtendedDataRecordTrigger
Range:
	TRIGGER_ON_CONFIRMED
	TRIGGER_ON_TEST_FAILED
	TRIGGER_ON_FDC_THRESHOLD
	...
```
###### `DemDebounceAlgorithmClass`
---
```
Description: Specifies whether debouncing is counter-based, time-based, or internal.
```
## References
---
[1] Specification of Diagnostic Event Manager (DEM), AUTOSAR Classic Platform, R20-11