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
			SdClientTimerInitialFindDelayMax [P]
			SdClientTimerInitialFindDelayMin [P]
			SdClientTimerInitialFindRepetitionsBaseDelay [P]
			SdClientTimerInitialFindRepetitionsMax [P]
			SdClientTimerRequestResponseMaxDelay [P]
			SdClientTimerRequestResponseMinDelay [P]
			SdClientTimerTTL [P]
			SdSubscribeEventgroupRetryDelay [P]
			SdSubscribeEventgroupRetryMax [P]

		SdServerService [C, 0..*]
			SdServerServiceHandleId [P]
			SdServerServiceAutoAvailable [P]
			SdServerServiceId [P]
			SdServerServiceInstanceId [P]
			SdServerServiceMajorVersion [P]
			SdServerServiceMinorVersion [P]
			SdServerServiceTcpRef [R, 0..1]
			SdServerServiceUdpRef [R, 0..1]
			SdServerServiceTimerRef [R, 1]
			SdServerGroupRef [R, 0..*]

			SdEventHandler [C, 0..*]
				SdEventHandlerHandleId [P]
				SdEventHandlerMulticastThreshold [P]
				SdEventHandlerTimerRef [R, 1]

				SdEventHandlerMulticast [C, 0..1]
					SdEventActivationRef [R, 1]
					SdMulticastEventSoConRef [R, 1]

				SdEventHandlerTcp [C, 0..1]
					SdEventActivationRef [R, 1]
					SdEventTriggeringRef [R, 1]

				SdEventHandlerUdp [C, 0..1]
					SdEventActivationRef [R, 1]
					SdEventTriggeringRef [R, 1]

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