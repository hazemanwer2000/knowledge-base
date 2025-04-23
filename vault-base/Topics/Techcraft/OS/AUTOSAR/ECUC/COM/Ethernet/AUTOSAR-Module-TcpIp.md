──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#Specification|Specification]]
- [[#Function(s)|Function(s)]]
- [[#Configuration|Configuration]]
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) TCP/IP* module, in functionality, API and configuration.
### Specification
---
For each configured TCP/IP controller, a state is maintained (i.e., `TCPIP_STATE_<..>`), which may be:
* `OFFLINE`
* `ONLINE`
* `ONHOLD`
* `STARTUP` (Note: Transitional).
* `SHUTDOWN` (Note: Transitional).

For each configured local IP address, a state is maintained (i.e., `TCPIP_IPADDR_STATE_<..>`), which may be:
* `UNASSIGNED`
* `ASSIGNED`
* `ONHOLD`

| State (N) | State (N+1) | Description                                                                                                                    |
| --------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `OFFLINE` | `STARTUP`   | `ONLINE` state requested, waiting for at least one associated local IP address to be `ASSIGNED`, after which state is `ONLINE` |
| `ONLINE`  | `SHUTDOWN`  | `OFFLINE` state requested, waiting for allocated resources to be freed, after which state is `OFFLINE`.                        |
| `ONLINE`  | `ONHOLD`    | `ONHOLD` state requested, all associated local IP address(es) are put in state `ONHOLD`, and communication is not active.      |
### Function(s)
---

| Name                            | Type      | Description                                                                                                                                           |
| ------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `TcpIp_Init`                    | API       | Initialize module.                                                                                                                                    |
| `TcpIp_RequestIpAddrAssignment` | API       | Requests a manually-triggered, configured address assignment method for a given local address (See `TcpIpLocalAddr` and `TcpIpAddrAssignment` below). |
| `TcpIp_RequestComMode`          | API       | Requests a state for a specific TCP/IP controller.                                                                                                    |
| `TcpIp_UdpTransmit`             | API       | Transmit a UDP datagram.                                                                                                                              |
| `TcpIp_TcpTransmit`             | API       | Transmit a TCP segment. A TCP/IP buffer is requested and filled, to be transmitted in the next `TcpIp_MainFunction`.                                  |
| `TcpIp_RxIndication`            | Callback  | Called by `EthIf_RxIndication` to indicate the reception of a new frame, calls upper-layer's RX indication API.                                       |
| `TcpIp_MainFunction`            | Scheduled | Cyclic function.                                                                                                                                      |
| `<UP>_RxIndication`             | Interface | Called upon reception of packet. For TCP, `TcpIp_TcpReceived` to be called later by `<UP>_MainFunction` (increasing receive window).                  |
| `<UP>_TxConfirmation`           | Interface | TCP-only, called upon reception of `ACK`.                                                                                                             |

*Note:* TCP/IP module does not receive confirmation from the *EthIf* module upon successful transmission.

*Note:* Refer to [1] for sequence diagrams, illustrating TCP socket connection establishment (as client/server), and TCP/UDP reception/transmission.
### Configuration
---
```
TcpIpConfig [C, 1]

	TcpIpCtrl [C, 1..*]
		TcpIpEthIfCtrlRef [R, 1]

	TcpIpLocalAddr [C, 1..*]
		TcpIpAddressType [P]
		TcpIpDomainType [P]
		TcpIpCtrlRef [R, 1]

		TcpIpAddrAssignment [C, 1..*]
			TcpIpAssignmentPriority [P]
			TcpIpAssignmentTrigger [P]
			TcpIpAssignmentMethod [P]

		TcpIpStaticIpAddressConfig [C, 0..1]
			TcpIpNetmask [P]
			TcpIpStaticIpAddress [P]

TcpIpGeneral [C, 1]
	TcpIpMainFunctionPeriod [P]
	TcpIpBufferMemory [P]
	TcpIpTcpSocketMax [P]
	TcpIpUdpSocketMax [P]
```
###### `TcpIpLocalAddr`
---
```
Path: TcpIpConfig/TcpIpLocalAddr/TcpIpAddressType
Description: Specifies address type (e.g., 'MULTICAST', 'UNICAST').
```

```
Path: TcpIpConfig/TcpIpLocalAddr/TcpIpDomainType
Description: Specifies address family (e.g., 'INET' for IPv4).
```
###### `TcpIpAddrAssignment`
---
```
Path: TcpIpConfig/TcpIpLocalAddr/TcpIpAddrAssignment/TcpIpAssignmentPriority
Description: If a new address is available from a higher priority assignment method, it is used.
```

```
Path: TcpIpConfig/TcpIpLocalAddr/TcpIpAddrAssignment/TcpIpAssignmentTrigger
Description: Specifies assignment trigger, whether 'AUTOMATIC', or 'MANUAL' via 'TcpIp_RequestIpAddrAssignment' API.
```

```
Path: TcpIpConfig/TcpIpLocalAddr/TcpIpAddrAssignment/TcpIpAssignmentMethod
Description: Specifies assignment method (e.g., 'STATIC').
```
###### `TcpIpStaticIpAddressConfig`
---
```
Path: TcpIpConfig/TcpIpLocalAddr/TcpIpStaticIpAddressConfig/TcpIpNetmask
Description: Specifies number of bits in subnet-mask.
```
## References
---
[1] Specification of TCP/IP module, AUTOSAR Classic Platform, R20-11