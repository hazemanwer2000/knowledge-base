──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) Communication (COM)* module, which resides in the Service layer, in functionality, API and configuration.
### Specification
---
#### Transmission
---
For all TX I-PDU(s),
* `ComTxIPduUnusedAreasDefault` specifies a byte-value, used to fill the buffer during initialization. Afterwards, `ComSignalInitValue` is written.
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

			ComTxMode(True/False) [C, 0..1]

				ComTxMode [C, 1]
					ComTxModeMode [P]
					ComTxModeTimePeriod [P]
					ComTxModeNumberOfRepetitions [P]
					ComTxModeRepetitionPeriod [P]

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
		ComTransferProperty [P]
		ComUpdateBitPosition [P, 0..1]

		ComFilter [C, 0..1]
			ComFilterAlgorithm [P]
			...

	ComSignalGroup [C, 0..*]
		ComHandleId [P]
		ComDataInvalidAction [P]
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
Description: Specifies whether MDT applies to cyclic, or repeated transmission(s).
```
###### `ComIPdu`
---
```
Path: ComConfig/ComIPdu/ComIPduDirection
Range:
	SEND
	RECEIVE
```

```
Path: ComConfig/ComIPdu/ComIPduType
Range:
	NORMAL
	TP
```

```
Path: ComConfig/ComIPdu/ComIPduSignalProcessing
Description: Specifies when signal indication/confirmation is made.
Range:
	DEFERRED - Deferred to the scheduled 'ComIPduMainFunctionRef'.
	IMMEDIATE - Handled directly in the context of 'Com_RxIndication'/'Com_TxConfirmation'.
```
###### `ComTxIPdu`
---
```
Path: ComConfig/ComIPdu/ComTxIPdu/ComMinimumDelayTime
Description: Specifies the Minimum-Delay-Time (MDT) between transmission(s) of the I-PDU.
```

*Note:* In `DIRECT` or `MIXED` TX mode, multiple triggering within an MDT triggers only a single transmission of the associated I-PDU, after the MDT ends.
###### `ComTxMode`
---
```
Path: ComConfig/ComIPdu/ComTxIPdu/ComTxMode(True/False)/ComTxMode/ComTxModeMode
Description: Specifies the TX mode of the I-PDU.
Range:
	DIRECT - Triggered when an associated signal, with non-'PENDING' transfer-property is sent.
	PERIODIC - Triggered cyclically, every `ComTxModeTimePeriod`.
	MIXED - Combines 'DIRECT' and 'PERIODIC' TX mode(s).
```

*Note:* I-PDU transmission is always deferred to the scheduled `ComIPduMainFunctionRef`.

```
Path: ComConfig/ComIPdu/ComTxIPdu/ComTxMode(True/False)/ComTxMode/ComTxModeNumberOfRepetitions
Description: Specifies the number of (additional) repeated transmission(s), in-case of 'DIRECT'-triggering.
```

```
Path: ComConfig/ComIPdu/ComTxIPdu/ComTxMode(True/False)/ComTxMode/ComTxModeRepetitionPeriod
Description: Specifies the periodicity of repeated transmission(s), if any.
```
###### `ComSignal`
---
```
Path: ComConfig/ComSignal/ComSignalType
Description: Specifies the type of signal.
Range:
	(U/S)INT(8/16/32/64)
	FLOAT(32/64)
	UINT8_N
	UINT8_DYN
```

```
Path: ComConfig/ComSignal/ComBitPosition
Description: Specifies the bit position of the signal within its associated I-PDU.
```

*Note:* Signal(s) of type `UINT8_N` and `UINT8_DYN` must begin and end at a byte-boundary.

*Note:* Signal(s) of type `UINT8_DYN` must reside at the end of an I-PDU.

```
Path: ComConfig/ComSignal/ComBitSize
Description: Specifies the size of the signal, in bit(s), for signal-types '(U/S)INT(8/16/32/64)'.
```

```
Path: ComConfig/ComSignal/ComSignalLength
Description: Specifies the (maximum) size of the signal, in byte(s), for signal-types 'UINT8_N' and 'UINT8_DYN'.
```
## References
---
[1] Specification of Communication (COM), AUTOSAR Classic Platform, R20-11
[2] Communication Specification, OSEK, 3.0.3