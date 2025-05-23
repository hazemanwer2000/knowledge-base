──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#Specification|Specification]]
	- [[#Specification#Asynchronous/Synchronous Interface(s)|Asynchronous/Synchronous Interface(s)]]
- [[#Configuration|Configuration]]
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) Diagnostic Communication Manager (DCM)* module, which resides in the Service layer, in functionality, API and configuration.
### Specification
---
The module shall be composed of three sub-module(s):
* *Diagnostic Session Layer (DSL)*, which shall,
	* Receive request(s) from, and transmit response(s) to, lower-layer *BSW* module(s),
	* Handle session(s), including timeout(s) (i.e., ${S3}_{Server}$), and,
	* Guarantee application-layer timing(s) (i.e., ${P2}_{Server\_Max}$, ${P2*}_{Server\_Max}$).
* *Diagnostic Service Dispatch (DSD)*, which shall,
	* Validate incoming request(s), based on the active session, security-level, etc.
* *Diagnostic Service Processing (DSP)*, which shall,
	* Validate request(s), based on format, and,
	* Assemble response from *BSW* module(s) and *SW-C*(s).
#### Asynchronous/Synchronous Interface(s)
---
For synchronous interface(s):
* Return-value(s):
	* `E_OK`
	* `E_NOT_OK`

For asynchronous interface(s):
* Parameter (In): `OpStatus`
	* It denotes the status of the operation.
	* Upon initial invocation, it shall be set to `DCM_INITIAL`.
	* Upon cancellation of the operation (e.g., timeout occurs), it shall be set to `DCM_CANCEL`.
* Return-value(s):
	* `E_OK`
	* `E_NOT_OK`
	* `DCM_E_PENDING`
		* Request processing still in-progress.
		* It must be invoked again by the next `Dcm_MainFunction`, with `OpStatus = DCM_PENDING`.
	* `DCM_E_FORCE_RCRRP`
		* It force(s) the transmission of an `RCRRP` response (i.e., not automatically triggered by the *DSL* sub-module).
		* It shall not be invoked again until transmission-confirmation.
		* Upon transmission-confirmation, it must be called again by the next `Dcm_MainFunction`, with `OpStatus = DCM_FORCE_RCRRP_OK`.

For all interface(s):
* Parameter (Out): `ErrorCode` (Optional)
	* If `E_NOT_OK` is returned, a negative response is sent with NRC set to `ErrorCode`.

*Note:* Refer to [1] for service-specific interface definition(s)
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
				DcmDslProtocolType [P]
				DcmTimStrP2ServerAdjust [P]
				DcmTimStrP2StarServerAdjust [P]
				DcmDemClientRef [R, 1] (DEM)
				DcmDslProtocolTxBufferRef [R, 1]
				DcmDslProtocolRxBufferRef [R, 1]
				DcmDslProtocolSIDTable [R, 1]

				DcmDslConnection [C, 1..*]
					
					DcmDslMainConnection [C, 1]

						DcmDslProtocolRx [C, 1..*]
							DcmDslProtocolRxAddrType [P]
							DcmDslProtocolRxPduRef [R, 1]

						DcmDslProtocolTx [C, 1]
							DcmDslProtocolTxPduRef [R, 1]
	
	DcmDsp [C, 1]

		DcmDsdServiceTable [C, 1..*]

			DcmDsdService [C, 1..*]
				DcmDsdSidTabServiceId [P]
				DcmDsdSidTabSubfuncAvail [P]
				DcmDsdSidTabSecurityLevelRef [R, 0..*]
				DcmDsdSidTabSessionLevelRef [R, 0..*]

					DcmDsdSubService [C, 0..*]
						DcmDsdSubServiceId [P]
						DcmDsdSubServiceSecurityLevelRef [R, 0..*]
						DcmDsdSubServiceSessionLevelRef [R, 0..*]

	DcmDsd [C, 1]

		DcmDspSecurity [C, 1]

			DcmDspSecurityRow [C, 1..*]
				DcmDspSecurityLevel [P]

		DcmDspSession [C, 1]

			DcmDspSessionRow [C, 1..*]
				DcmDspSessionLevel [P]

		...
```

*Note:* Refer to [1] for service-specific configuration (e.g., DID(s), Routine(s), etc).
###### `DcmDslDiagResp`
---
```
Description: Relates to the automatic 'RCRRP' response management.
```

```
Path: DcmConfigSet/DcmDsl/DcmDslDiagResp/DcmDslDiagRespMaxNumRespPend
Description: Maximum number of allowed 'RCRRP' response(s), before 'GR' response is sent, and service-processing cancelled.
```
###### `DcmDslProtocolRow`
---
```
Path: DcmConfigSet/DcmDsl/DcmDslProtocol/DcmDslProtocolRow/DcmDslProtocolType
Range:
	UDS_ON_CAN
	UDS_ON_LIN
	UDS_ON_IP
	...
```

```
Path: DcmConfigSet/DcmDsl/DcmDslProtocol/DcmDslProtocolRow/DcmTimStrP2ServerAdjust
Description: Adjustment to the current 'DcmDspSessionP2ServerMax', to account for any delay(s) during transmission (i.e., bus-delay, stack-overhead).
```
## References
---
[1] Specification of Diagnostic Communication Manager (DCM), AUTOSAR Classic Platform, R20-11