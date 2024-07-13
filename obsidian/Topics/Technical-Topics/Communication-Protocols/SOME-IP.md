──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*SOME/IP* (Scalable service-Oriented MiddlewarE over IP) protocol allows the definition of service(s). [1]

*SOME/IP-SD* (Service Discovery) manages the discovery and subscription to service(s). [2]
### SOME/IP
---
A service may contain one or more event, method or field.
* An event is a `NOTIFICATION` sent by a provider either cyclically, or on-change.
* A method is invoked via a `REQUEST` (i.e., RPC, or Remote-Procedure-Call), sent by a client. Accordingly, a `RESPONSE` is sent by the provider.
	* If it is a Fire-and-Forget request (i.e., `REQUEST_NO_RETURN`), no response is sent.
* A field consists of any combination of,
	* A getter, a `REQUEST`/`RESPONSE`, used to get the current value of the field.
		* *Note:* The payload of a getter `REQUEST` is empty.
	* A setter, a request/response, used to set the current value of the field.
		* *Note:* The payload of a setter `RESPONSE` is the current value of the field.
	* A `NOTIFICATION`, sent by the provider, on-change.
		* *Note:* Upon subscription to the service (see below), a field `NOTIFICATION` is always sent initially.
#### Header Format
---
The header format, as shown below, consists of,
* Service ID (Size: 2 bytes)
* Method/Event/Field ID (Size: 2 bytes)
* Length (Size: 4 bytes)
* Request ID (Size: 4 bytes)
	* Purpose
		* Identify which `REQUEST`(s) (including `REQUEST_NO_RETURN`(s)) are from which client.
		* Identify which `RESPONSE`(s) correspond to which `REQUEST(s)`, even from the same client.
		* In all other cases, this field may be `0x0`.
	* Format
		* Client ID (Size: 2 bytes), which identifies a client uniquely.
			* *Note:* Multiple client(s) may reside within an ECU.
		* Session ID (Size: 2 bytes), which increments from `0x1` to `0xFFFF`, then wraps.
			* *Note:* For `REQUEST_NO_RETURN`(s), this field may be `0x0`.
* Protocol Version (Size: 1 byte), which identifies the SOME/IP protocol version used.
* Interface Version (Size: 1 byte), which identifies the major version of the service.
* Message Type (Size: 1 byte), which identifies whether the SOME/IP message is,
	* `REQUEST`.
	* `RESPONSE`.
	* `REQUEST_NO_RETURN`.
	* `NOTIFICATION`.
	* `ERROR` (see below).
* Return Code (Size: 1 byte), which identifies the status of the SOME/IP message.
	* If an error occurs while constructing a `RESPONSE`, it is sent with status other than `E_OK`.
	* If a generic error occurs, an `ERROR` is sent with status other than `E_OK`.
	* In all other cases, the status is `E_OK`.

![[SOME-IP-Header-Format.png|650]]
### SOME/IP-SD
---
#### Header Format
---
SOME/IP-SD messages are sent as SOME/IP messages. Hence, a SOME/IP header precedes the SOME/IP-SD header, and consists of, most notably,
* Service ID, fixed to `0xFFFF`.
* Method/Event/Field ID, fixed to `0x8100`.
* Request ID, consists of,
	* Client ID, fixed to `0x0`.
		* *Note:* Only a single SD client may reside within an ECU.
	* Session ID, increments per SD message sent, per client.
		* *Note:* Even though SD message(s) are `NOTIFICATION`(s), the Session ID must be used.
* Interface Version, fixed to `0x1`.
* Message Type, fixed to `NOTIFICATION`.

The SD header format, as shown below, consists of,
* Flags (Size: 1 byte)
	* Reboot flag (Position: 7), which is initially set, and is reset after the Session ID wraps for the first time.
		* *Note:* A reboot of an SD client is detected if either,
			* Reboot flag transitions from `0` to `1`.
			* Reboot flag remains `1`, and the Session ID, let it be ($X$), ($X_{n+1} > X_n$) is not true.
* ...

![[SOME-IP-SD-Header-Format.png|700]]

*Note:* SOME/IP-SD messages are sent over UDP.
## References
---
[1] SOME/IP Protocol Specification, AUTOSAR Classic Platform, R22-11
[2] SOME/IP-SD Protocol Specification, AUTOSAR Classic Platform, R22-11