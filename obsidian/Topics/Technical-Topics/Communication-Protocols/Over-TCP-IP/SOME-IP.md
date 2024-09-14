──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## Content
---
*SOME/IP* (Scalable service-Oriented MiddlewarE over IP) protocol allows the definition of service(s). [1]
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
## References
---
[1] SOME/IP Protocol Specification, AUTOSAR Classic Platform, R22-11