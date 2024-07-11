──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) Socket Adaptor (SoAd)* module, in functionality, API and configuration.
### Specification
---
The module allows the configuration of socket connection group(s), each with one or more socket connection(s).

*Note:* For UDP, socket connection(s) within a socket connection group share the same UDP socket.

Each socket connection may be in one of these state(s) (i.e., `SOAD_SOCON_<..>`):
* `OFFLINE`
* `RECONNECT`
* `ONLINE` (TX/RX enabled)

After `SoAd_Init` is called, all socket connection(s) are initialized into the `OFFLINE` state.

Within `SoAd_MainFunction`, all `OFFLINE` socket connection(s) that match the following criteria will transition into the `RECONNECT` state.
* `SoAdSocketAutomaticSocketSoConSetup` is set to true, or `SoAd_OpenSoCon` is requested.
* Associated TCP/IP local IP address is in state `ASSIGNED`.

Within `SoAd_RxIndication`, a socket connection transitions from the `RECONNECT` state, to the `ONLINE` state, if,
* For UDP,
	* Configured remote address matches that of the received datagram.

*Note:* For UDP, if `SoAdSocketUdpListenOnly` is set to true, socket connection transitions from the `RECONNECT` to `CONNECT` state automatically.

*Note:* For socket connection group(s) with multiple socket connection(s), selection of the socket connection is based on the best-match algorithm [1].

If `SoAd_CloseSoCon` is called for a socket connection, within the next `SoAd_MainFunction`,
* For UDP,
	* Transition into the `OFFLINE` state.

*Note:* For UDP, if `SoAdSocketUdpAliveSupervisionTimeout` time has passed since the last reception of a datagram, the associated socket connection transitions into the `RECONNECT` state.
#### Additional Features
---
##### PDU Header Option
---
##### Message Acceptance Filter
---
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