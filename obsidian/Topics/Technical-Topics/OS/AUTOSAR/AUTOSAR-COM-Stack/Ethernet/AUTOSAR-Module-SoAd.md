──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) Socket Adaptor (SoAd)* module, in functionality, API and configuration.
### Specification
---
...
### Function(s)
---

| Name        | Type | Description        |
| ----------- | ---- | ------------------ |
| `SoAd_Init` | API  | Initialize module. |
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

SoAdGeneral [C, 1]
	SoAdMainFunctionPeriod [P]
```
###### `SoAdSocketConnectionGroup`
---
```
Path: SoAdConfig/SoAdSocketConnectionGroup/SoAdSocketAutomaticSoConSetup
Description: If disabled, associated socket connection(s) are managed via 'SoAd_<...>SoCon' API(s).
```

```
Path: SoAdConfig/SoAdSocketConnectionGroup/SoAdSocketLocalPort
Description: If not set, an ephemeral port is used.
```

```
Path: SoAdConfig/SoAdSocketConnectionGroup/SoAdSocketMsgAcceptanceFilterEnabled
Description: For UDP, allows the acceptance of datagrams, regardless of the remote address.
Constraints:
	- Must be set to true if,
		- 'SocketConnectionGroup' must contain a single 'SocketConnection'.
		- For UDP, remote address is wildcard and 'SoAdSocketUdpListenOnly' is set to false.
```
## References
---
[1] Specification of Socket Adaptor module, AUTOSAR Classic Platform, R20-11