──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*SOME/IP* (Scalable service-Oriented MiddlewarE over IP) protocol allows the definition of service(s).

*SOME/IP-SD* (Service Discovery) manages the discovery and subscription to service(s).
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
## References
---
[1] SOME/IP Protocol Specification, AUTOSAR Classic Platform, R22-11
[2] SOME/IP-SD Protocol Specification, AUTOSAR Classic Platform, R22-11