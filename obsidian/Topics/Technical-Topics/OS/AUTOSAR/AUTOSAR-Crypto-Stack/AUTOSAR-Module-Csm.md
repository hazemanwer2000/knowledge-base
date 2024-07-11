──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*

- [[#Specification|Specification]]
- [[#Function(s)|Function(s)]]
- [[#Configuration|Configuration]]
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) Crypto Service Manager (Csm)* module, which resides in the Service layer, in functionality, API and configuration.
### Specification
---
The module allows the configuration of cryptographic job(s). Each job references,

* a `CsmKey`, which references a `CryIfKey`, which references a `CryptoKey` from the underlying Crypto Driver module(s),
* a `CsmPrimitive`, specifying the cryptographic operation,
* a `CsmQueue`, which references a `CryIfChannel`, which references a `CryptoDriverObject` from the underlying Crypto Driver module(s).

*Note:* Queuing may occur at different layers; MCAL layer, by the Crypto Driver module(s), and service layer, by the *Csm* module.
### Function(s)
---

| Name               | Type      | Description                                                                               |
| ------------------ | --------- | ----------------------------------------------------------------------------------------- |
| `Csm_Init`         | API       | ...                                                                                       |
| `Csm_MainFunction` | Scheduled | ...                                                                                       |
| `Csm_<SERVICE>`    | API       | Different service API(s), used to trigger job execution.                                  |
| `Csm_CancelJob`    | API       | Used to cancel the execution of an on-going job.                                          |
| `Csm_Key<ACTION>`  | API       | Different key-management API(s), as a direct interface to the underlying *Crypto Driver*. |
### Configuration
---
```
CsmJobs [C, 1]

	CsmJob [C, 1..*]
		CsmJobId [P]
		CsmJobPriority [P]
		CsmProcessingMode [P]
		CsmJobKeyRef [R, 1]
		CsmJobPrimitiveRef [R, 1]
		CsmJobQueueRef [R, 1]
		CsmJobPrimitiveCallbackRef [R, 0..1]

CsmKeys [C, 1]

	CsmKey [C, 1..*]
		CsmKeyId [P]
		CsmKeyRef [R, 1]

CsmQueues [C, 1]

	CsmQueue [C, 1..*]
		CsmQueueSize [P]
		CsmChannelRef [R, 1]

CsmPrimitives [C, 1]
	...

CsmCallbacks [C, 1]
	...
```
## References
---
[1] Specification of Crypto Driver, AUTOSAR Classic Platform, R20-11
[2] Specification of Crypto Interface, AUTOSAR Classic Platform, R20-11
[3] Specification of Crypto Service Manager, AUTOSAR Classic Platform, R20-11