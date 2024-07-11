──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#Specification|Specification]]
	- [[#Specification#Additional Features|Additional Features]]
		- [[#Additional Features#PDU Header Option|PDU Header Option]]
		- [[#Additional Features#Message Acceptance Filter|Message Acceptance Filter]]
		- [[#Additional Features#Routing Group(s)|Routing Group(s)]]
		- [[#Additional Features#`nPDU` Buffering|`nPDU` Buffering]]
- [[#Configuration|Configuration]]
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) Socket Adaptor (SoAd)* module, in functionality, API and configuration.
### Specification
---
The module allows the configuration of socket connection group(s), each with one or more socket connection(s).

*Note:* For UDP, socket connection(s) within a socket connection group share the same UDP socket.

*Note:* For TCP, if `SoAdSocketTcpInitiate` is false for a socket connection group, multiple socket connection(s) will use the same listen TCP socket, but use independent TCP socket(s) upon connection establishment.

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
* For TCP,
	* If `SoAdSocketTcpInitiate` is set to false,
		* TCP connection listened for and established, and configured remote address matches that of the peer.

*Note:* For UDP, if `SoAdSocketUdpListenOnly` is set to true, socket connection transitions from the `RECONNECT` to `CONNECT` state automatically.

*Note:* For TCP, if `SoAdSocketTcpInitiate` is set to true, TCP connection is initiated within the `SoAd_MainFunction`. Upon success, socket connection transitions to `CONNECT` state. 

*Note:* For socket connection group(s) with multiple socket connection(s), selection of the socket connection is based on the best-match algorithm [1].

If `SoAd_CloseSoCon` is called for a socket connection, within the next `SoAd_MainFunction`,
* For UDP,
	* Transition into the `OFFLINE` state.
	* Reset to the configured remote address.
* For TCP,
	* TCP connection is terminated.
	* Transition into the `OFFLINE` state.
	* Reset to the configured remote address.

*Note:* For UDP, if `SoAdSocketUdpAliveSupervisionTimeout` time has passed since the last reception of a datagram, the associated socket connection transitions into the `RECONNECT` state.
#### Additional Features
---
##### PDU Header Option
---
For a socket connection group, if `SoAdPduHeaderEnable` is set to true, each PDU shall have a header, consisting of:
* ID field (size: 4 bytes)
* Size field (size: 4 bytes)
##### Message Acceptance Filter
---
For a socket connection group, if `SoAdSocketMsgAcceptanceFilterEnabled` is set to true,
* For TCP,
	* TCP connection(s) will be accepted if the remote address of the peer matches the configured remote address.
* For UDP,
	* Received UDP datagram(s) will be accepted if the remote address, in each datagram, matches the configured remote address.
##### Routing Group(s)
---
Socket/PDU route destination(s) may belong to a routing group.

If a routing group is de-activated, associated destination(s) become inactive.
##### `nPDU` Buffering
---
If a UDP socket connection is referenced by PDU route destination(s) with at least one having `SoAdTxUdpTriggerMode` configured to `TRIGGER_NEVER`, a TX buffer shall be maintained.

The TX buffer shall be transmitted, if,
* `SoAdTxUdpTriggerTimeout` (or, if not configured, `SoAdSocketUdpTriggerTimeout`) is exceeded for any buffered PDU.
* `SoAdSocketnPduUdpTxBufferMin` is about to be exceeded.
* PDU is transmitted on a PDU route destination, with `SoAdTxUdpTriggerMode` set to `TRIGGER_ALWAYS`.

For a PDU route, 
* If `SoAdTxPduCollectionSemantics` is set to `COLLECT_LAST_IS_BEST`, only the transmission request shall be stored. Upon transmission, the PDU data is requested from the upper-layer.
* If `SoAdTxPduCollectionSemantics` is set to `COLLECT_QUEUED`, the PDU data is queued when transmission is requested. Queuing of multiple instance(s) of same PDU (i.e., with same ID) is allowed.
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