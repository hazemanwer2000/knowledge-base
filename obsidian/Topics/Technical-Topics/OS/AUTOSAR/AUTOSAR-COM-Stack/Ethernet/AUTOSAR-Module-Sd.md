──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
### Configuration
---
```
SdConfig [C, 1]

	SdInstance [C, 0..*]

		SdClientService [C, 0..*]
			SdClientServiceHandleId [P]
			SdClientServiceAutoRequire [P]
			SdClientServiceId [P]
			SdClientServiceInstanceId [P]
			SdClientServiceMajorVersion [P]
			SdClientServiceMinorVersion [P]
			SdClientServiceUdpRef [R, 0..1]
			SdClientServiceTcpRef [R, 0..1]
			SdClientServiceTimerRef [R, 1]
			SdServiceGroupRef [R, 0..*]

			SdConsumedEventGroup [C, 0..*]
				SdConsumedEventGroupHandleId [P]
				SdConsumedEventGroupAutoRequire [P]
				SdConsumedEventGroupId [P]
				SdConsumedEventGroupUdpActivationRef [R, 0..1]
				SdConsumedEventGroupTcpActivationRef [R, 0..1]
				SdConsumedEventGroupMulticastGroupRef [R, 0..1]
				SdConsumedEventGroupMulticastActivationRef [R, 0..1]
				SdConsumedEventGroupTimerRef [R, 1]

			SdConsumedMethods [C, 0..1]
				SdClientServiceActivationRef [R, 1]

		SdClientTimer [C, 0..*]

		SdServerService [C, 0..*]

		SdServerTimer [C, 0..*]

		SdInstanceTxPdu [C, 1]

		SdInstanceUnicastRxPdu [C, 1]

		SdInstanceMulticastRxPdu [C, 1]

	SdServiceGroup [C, 0..*]
		SdServiceGroupHandleId [P]
```
## References
---
[1] ...