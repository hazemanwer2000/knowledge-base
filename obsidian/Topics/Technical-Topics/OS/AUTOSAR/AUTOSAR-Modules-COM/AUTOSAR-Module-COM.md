──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) Communication (COM)* module, which resides in the Service layer, in functionality, API and configuration.
### Specification
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

	ComIPduGroup [C, 0..*]

	ComSignal [C, 0..*]

	ComSignalGroup [C, 0..*]
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