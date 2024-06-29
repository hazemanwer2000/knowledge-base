──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) TCP/IP module, in functionality, API and configuration.
### Specification
---
...
### Function(s)
---

| Name  | Type | Description |
| ----- | ---- | ----------- |
| `...` | API  | ...         |
|       |      |             |
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
Description: Specifies assignment trigger, whether 'AUTOMATIC', or 'MANUAL' via 'TcpIp_RequestIpAddrAssignment'.
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
[1] ...