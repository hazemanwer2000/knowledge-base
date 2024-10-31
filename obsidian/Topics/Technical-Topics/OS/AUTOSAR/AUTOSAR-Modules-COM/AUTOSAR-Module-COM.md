──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) Communication (COM)* module, which resides in the Service layer, in functionality, API and configuration.
### Specification
---
#### Minimum Delay Time (MDT)
---
...
### Configuration
---
```
ComGeneral [C, 1]
	ComEnableMDTForCyclicTransmission [P]

ComConfig [C, 1]

	ComIPdu [C, 0..*]
		ComIPduHandleId [P]
		ComIPduDirection [P]
		ComIPduSignalProcessing [P]
		ComIPduType [P]
		ComIPduMainFunctionRef [R, 1]
		ComIPduGroupRef [R, 0..*]
		ComIPduSignalRef [R, 0..*]
		ComIPduSignalGroupRef [R, 0..*]
		ComPduIdRef [R, 1]

		ComTxIPdu [C, 0..1]
			ComMinimumDelayTime [P]
			ComTxIPduClearUpdateBit [P]
			ComTxIPduUnusedAreasDefault [P]

			ComTxMode(True/False) [C, 0..1]

				ComTxMode [C, 1]
					ComTxModeMode [P]
					ComTxModeNumberOfRepetitions [P]
					ComTxModeRepetitionPeriod [P]
					ComTxModeTimeOffset [P]
					ComTxModeTimePeriod [P]

	ComIPduGroup [C, 0..*]
		ComIPduGroupHandleId [P]
		ComIPduGroupGroupRef [R, 0..*]

	ComSignal [C, 0..*]
		ComHandleId [P]
		ComSignalType [P]
		ComBitPosition [P]
		ComBitSize [P]
		ComSignalLength [P]
		ComSignalDataInvalidValue [P]
		ComSignalInitValue [P]
		ComDataInvalidAction [P]
		ComInvalidNotification [P]
		ComNotification [P]
		ComTransferProperty [P]
		ComUpdateBitPosition [P, 0..1]

		ComFilter [C, 0..1]
			ComFilterAlgorithm [P]
			...

	ComSignalGroup [C, 0..*]
		ComHandleId [P]
		ComDataInvalidAction [P]
		ComInvalidNotification [P]
		ComNotification [P]
		ComTransferProperty [P]
		ComUpdateBitPosition [P, 0..1]

		ComGroupSignal [C, 0..*]
			ComHandleId [P]
			ComSignalType [P]
			ComBitPosition [P]
			ComBitSize [P]
			ComSignalLength [P]
			ComSignalDataInvalidValue [P]
			ComSignalInitValue [P]
			ComTransferProperty [P] (*)

			ComFilter [C, 0..1]
				ComFilterAlgorithm [P]
				...
```
###### `ComGeneral`
---
```
Path: ComGeneral/ComEnableMDTForCyclicTransmission
Description: 'MDT' mechanism does not apply to cyclic, or repeated transmission(s).
```
###### `ComIPdu`
---
```
Path: ComConfig/ComIPdu/ComIPduDirection
Range:
	SEND
	RECEIVE
```
## References
---
[1] Specification of Communication (COM), AUTOSAR Classic Platform, R20-11