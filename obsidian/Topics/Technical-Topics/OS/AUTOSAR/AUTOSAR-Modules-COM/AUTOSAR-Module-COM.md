──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) Communication (COM)* module, which resides in the Service layer, in functionality, API and configuration.
### Function(s)
---

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
		ComSignalInitValue [P]
		ComTransferProperty [P]
		ComUpdateBitPosition [P, 0..1]
		ComSignalDataInvalidValue [P]
		ComDataInvalidAction [P]

		ComFilter [C, 0..1]
			ComFilterAlgorithm [P]
			...

	ComSignalGroup [C, 0..*]
		ComHandleId [P]
		ComTransferProperty [P]
		ComUpdateBitPosition [P, 0..1]
		ComDataInvalidAction [P]

		ComGroupSignal [C, 0..*]
			ComHandleId [P]
			ComSignalType [P]
			ComBitPosition [P]
			ComBitSize [P]
			ComSignalLength [P]
			ComSignalInitValue [P]
			ComTransferProperty [P] (*)
			ComSignalDataInvalidValue [P]

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
###### `ComTxMode(True/False)`
---
```
Description: 
	Specifies the TX mode of the I-PDU, in-case the Transmission-Mode Selector (TMS) evaluates to 'True'/'False'.
	The TMS is a logical-'OR' of all Transmission-Mode Condition(s) (TMC) of all associated signal(s).
	The TMC of a signal is 'True' if 'ComFilter' evaluates to true, or is missing.
```
###### `ComTxMode`
---
```
Path: ComConfig/ComIPdu/ComTxIPdu/ComTxMode(True/False)/ComTxMode/ComTxModeMode
Description: Specifies the TX mode of the I-PDU.
Range:
	DIRECT - Triggered when an associated signal, with non-'PENDING' transfer-property is sent.
	PERIODIC - Triggered cyclically, every `ComTxModeTimePeriod`.
	MIXED - Combines 'DIRECT' and 'PERIODIC' TX mode(s).
	NONE - Never triggered.
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

```
Path: ComConfig/ComSignal/ComTransferProperty
Range:
	PENDING
	TRIGGERED
	TRIGGERED_ON_CHANGE
	...
```

*Note:* Transfer property of a signal is relevant only for non-(`PERIODIC`/`NONE`) TX mode(s) of the associated I-PDU.

```
Path: ComConfig/ComSignal/ComUpdateBitPosition
Description: Specifies the bit position of the update-bit of the signal within its associated I-PDU.
```

*Note:* For signal(s) of type `UINT8_DYN`, the update-bit, if present, must reside before the signal, within its associated I-PDU.

*Note:* If a signal is received with a reset update-bit signal, the signal shall be discarded.

```
Path: ComConfig/ComSignal/ComDataInvalidAction
Description: Specifies the action to take, upon the reception of the signal, with 'ComSignalDataInvalidValue' as value.
Range:
	NOTIFY - Sends an invalid-notification to the respective upper-layer.
	REPLACE - Acts as if the signal was received with its 'ComSignalInitValue' value.
```
###### `ComFilter`
---
```
Description: Used for filtering (i.e., discarding) RX signal(s), and evaluating TMC for TX signal(s).
```
## References
---
[1] Specification of Communication (COM), AUTOSAR Classic Platform, R20-11