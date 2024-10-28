──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
...
### Specification
---
...
### Configuration
---
```
DcmConfigSet [C, 1]
	
	DcmDsl [C, 1]

		DcmDslBuffer [C, 1..*]
			DcmDslBufferSize [P]

		DcmDslDiagResp [C, 1]
			DcmDslDiagRespMaxNumRespPend [P]

		DcmDslProtocol [C, 1]

			DcmDslProtocolRow [C, 1..*]
	
	DcmDsp [C, 1]
	
	DcmDsd [C, 1]
	
	DcmPageBufferCfg [C, 1]
	
	DcmProcessingConditions [C, 0..1]
```
###### `DcmDslDiagResp`
---
```
Description: Relates to the automatic 'RCRRP' response management.
```

```
Path: DcmConfigSet/DcmDsl/DcmDslDiagResp/DcmDslDiagRespMaxNumRespPend
Description: Maximum number of allowed 'RCRRP' response(s), before 'GR' response is sent, and service-processing cancelled.
```
## References
---
[1] Specification of Diagnostic Communication Manager (DCM), AUTOSAR Classic Platform, R20-11