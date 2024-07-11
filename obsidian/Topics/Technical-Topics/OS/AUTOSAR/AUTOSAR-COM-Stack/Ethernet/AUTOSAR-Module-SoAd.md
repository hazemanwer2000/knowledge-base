──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) Socket Adaptor (SoAd)* module, in functionality, API and configuration.
### Specification
---
The module allows the configuration of socket connection group(s), each with one or more socket connection.

Each socket connection may be in one of these state(s):
* `SOAD_SOCON_OFFLINE`
* `SOAD_SOCON_RECONNECT`
* `SOAD_SOCON_ONLINE`

After `SoAd_Init` is called, all socket connection(s) are initialized into the `SOAD_SOCON_OFFLINE` state.
#### UDP
---
Socket connection(s) within a UDP socket connection group share the same UDP socket.

Within `SoAd_MainFunction`, 
### Configuration
---
```
SoAdConfig [C, 1]

	SoAdSocketConnectionGroup [C, 1..*]
		SoAdPduHeaderEnable [P]
		SoAdSocketAutomaticSoConSetup [P]
		SoAdSocketLocalPort [P]
		SoAdSocketLocalAddressRef [R, 1]
		SoAdSocketMsgAcceptanceFilterEnabled [P]

		SoAdSocketConnection [C, 1..*]
			SoAdSocketId [P]

			SoAdSocketRemoteAddress [C, 1]
				SoAdSocketRemoteIpAddress [P]
				SoAdSocketRemotePort [P]

		SoAdSocketProtocol [C, 1]

			SoAdSocketUdp [C, 0..1]
				SoAdSocketUdpAliveSupervisionTimeout [P]
				SoAdSocketUdpListenOnly [P]
				SoAdSocketnPduUdpTxBufferMin [P] {Feature: nPduUdp}
				SoAdSocketUdpTriggerTimeout [P] {Feature: nPduUdp}

			SoAdSocketTcp [C, 0..1]
				SoAdSocketTcpInitiate [P]

	SoAdSocketRoute [C, 0..*]
		SoAdRxSocketConnOrSocketConnBundleRef [R, 1]

		SoAdSocketRouteDest [C, 1..*]
			SoAdRxPduRef [R, 1]
			SoAdRxRoutingGroupRef [R, 1]

	SoAdPduRoute [C, 0..*]
		SoAdTxPduCollectionSemantics [P, 0..1] {Feature: nPduUdp}
		SoAdTxPduRef [R, 1]

		SoAdPduRouteDest [C, 1..*]
			SoAdTxUdpTriggerMode [P, 0..1] {Feature: nPduUdp}
			SoAdTxUdpTriggerTimeout [P, 0..1] {Feature: nPduUdp}
			SoAdTxSocketConnOrSocketBundleRef [R, 1]
			SoAdTxRoutineGroupRef [R, 1]

	SoAdRoutingGroup [C, 0..*]
		SoAdRoutingGroupId [P]
		SoAdRoutingGroupIsEnabledAtInit [P]

SoAdGeneral [C, 1]
	SoAdMainFunctionPeriod [P]
```
###### `SoAdSocketConnectionGroup`
---
```
Path: SoAdConfig/SoAdSocketConnectionGroup/SoAdSocketLocalPort
Description: If not set, an ephemeral port is used.
```
###### `SoAdSocketRemoteAddress`
---
```
Path: SoAdConfig/SoAdSocketConnectionGroup/SoAdSocketConnection/SoAdSocketRemoteAddress/SoAdSocketRemoteIpAddress
Description: To accept any remote IP address, set to 'ANY'.
```

```
Path: SoAdConfig/SoAdSocketConnectionGroup/SoAdSocketConnection/SoAdSocketRemoteAddress/SoAdSocketRemotePort
Description: To accept any remote port, set to 0.
```
## References
---
[1] Specification of Socket Adaptor module, AUTOSAR Classic Platform, R20-11