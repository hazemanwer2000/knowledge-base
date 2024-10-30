──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#Specification|Specification]]
	- [[#Specification#Enable/Storage Condition(s)|Enable/Storage Condition(s)]]
	- [[#Specification#Displacement Strategy|Displacement Strategy]]
- [[#Function(s)|Function(s)]]
	- [[#Function(s)#General|General]]
	- [[#Function(s)#Client-Specific|Client-Specific]]
- [[#Configuration|Configuration]]
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) Diagnostic Event Manager (DEM)* module, which resides in the Service layer, in functionality, API and configuration.
### Specification
---
#### Enable/Storage Condition(s)
---
For a specific event (i.e., `DemEventParameter`),
* If any (referenced) enable condition is not satisfied while `Dem_SetEventStatus` is invoked, the reported event status is ignored.
* If any (referenced) storage condition is not satisfied, no event-memory entry is allocated (i.e., for freeze-frame, or extended-data record storage).

*Note:* `Dem<..>ConditionStatus` specifies the initial value of the condition, upon start-up.
#### Displacement Strategy
---
When no event-memory entries are available, and a new entry must be allocated, a displacement strategy determines which (existing) entry shall be overwritten by the new entry, if any.

If displacement strategy is `FULL`, entries shall take precedence based on the following criteria, in the specified order:
* Associated priority of entry, which derives from `DemDTCPriority`.
* Associated `TF` bit-value (i.e., `TF == 1` takes precedence).
* Time of occurrence (i.e., newer entries take precedence).

If displacement strategy is `NONE`, no displacement takes place.
### Function(s)
---
#### General
---

| Name                      | Type      | Description                                                                                                       |
| ------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------- |
| `Dem_(Pre)Init`           | API       | Initializes module.                                                                                               |
| `Dem_MainFunction`        | Scheduled | Handles cyclic activities.                                                                                        |
| `Dem_SetEventStatus`      | API       | Reports the status of an event, as `FAILED`/`PASSED`, or `PREFAILED`/`PREPASSED` (i.e., non-internal debouncing). |
| `Dem_SetEnableCondition`  | API       | Sets an enable condition.                                                                                         |
| `Dem_SetStorageCondition` | API       | Sets a storage condition.                                                                                         |
#### Client-Specific
---

| Name            | Type | Description                                                                              |
| --------------- | ---- | ---------------------------------------------------------------------------------------- |
| `Dem_SelectDTC` | API  | Selects an individual/group DTC, from a specific event memory, for further operation(s). |
| `Dem_ClearDTC`  | API  | Clears (previously selected) DTC(s).                                                     |
*Note:* Client-specific API(s) are re-entrant for different client(s), and non-re-entrant for the same client.
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

		DemUserDefinedMemory [C, 0..*]
			DemEventDisplacementStrategy [P]
			DemEventMemoryEntryStorageTrigger [P]
			DemMaxNumberEventEntryUserDefined [P]
			DemUserDefinedMemoryIdentifier [P]

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
###### `DemDataElementClass`
---
```
Description: Specifies an internal, or an external data element.
```
###### `DemDebounceAlgorithmClass`
---
```
Description: Specifies whether debouncing is counter-based, time-based, or internal.
```
## References
---
[1] Specification of Diagnostic Event Manager (DEM), AUTOSAR Classic Platform, R20-11