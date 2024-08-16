──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*Unified Diagnostic Services (UDS)* is an automotive-oriented, application-layer protocol, that specifies a set of diagnostic services (i.e., requests and responses).

*UDS* is transport-layer protocol-independent, and may run over *CAN-TP* in *CAN*, *DoIP* in *Ethernet*, etc.
### Acronyms
---
* **VM -** Vehicle Manufacturer
* **RC -** Response Code
	* **PRC -** Positive RC
	* **NRC -** Negative RC
### Definitions
---
...
### Overview
---
Each service has a byte-length value unique identifier, called *Service Identifier (SID)*.

Each service may have multiple sub-function(s), each of which has a 6-bit-length value unique identifier.
#### Message Structure
---
The structure of a service request is as follows,
* SID (Length: 1-byte)
* Sub-Function (Length: 1-byte)
	* Sub-Function ID (Length: 6-bit)
	* "SuppressPositiveResponse" Option (Length: 1-bit)
* Data (Length: Variable)

The structure of a positive service response is as follows,
* SID + `0x40` (Length: 1-byte)
* Sub-Function (Length: 1-byte)
	* Sub-Function ID (Length: 6-bit)
	* `0x0` (Length: 1-bit)
* Data (Length: Variable)

The structure of a negative service response is as follows,
* `0x7F` (Length: 1-byte)
* SID (Length: 1-byte)
* NRC (Length: 1-byte)
#### Generic NRC(s)
---
The following is a list of generic NRC(s).

| NRC    | Description                                  | Acronym | Description                                                                                           |
| ------ | -------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------- |
| `0x13` | Incorrect Message Length Or Invalid Format   | IMLOIF  | Message length or format is incorrect.                                                                |
| `0x11` | Service Not Supported                        | SNS     | SID is not supported.                                                                                 |
| `0x7F` | Service Not Supported In Active Session      | SNSIAS  | SID is not supported, in active session.                                                              |
| `0x12` | Sub-Function Not Supported                   | SFNS    | Sub-Function is not supported.                                                                        |
| `0x7E` | Sub-Function Not Supported In Active Session | SFNSIAS | Sub-Function is not supported, in active session                                                      |
| `0x31` | Request Out Of Range                         | ROOR    | Data (in request) is not supported.                                                                   |
| `0x22` | Conditions Not Correct                       | CNC     | Criteria (for request) is unmet.                                                                      |
| `0x24` | Request Sequence Error                       | RSE     | Sequence of request(s) is invalid.                                                                    |
| `0x21` | Busy (Repeat Request)                        | BRR     | Currently busy, and unable to perform request.                                                        |
| `0x33` | Security Access Denied                       | SAD     | Request is secured, and server is in an unlocked state.                                               |
| `0x11` | General Reject                               | GR      | Request rejected, reason unknown.                                                                     |
| `0x78` | Request Correctly Received, Response Pending | RCRRP   | Request correctly received, response pending.<br>*Note:* This is not a negative response (see below). |
### Services
---
#### Management
---
##### Diagnostic Session Control (0x10)
---
This service may be used to transition a server between the *Default* session, and *Non-Default* session(s). 

Depending on the active session, some request(s) (e.g., service(s)) may not be supported.

The following are standardized session(s), which may be extended with VM-specific session(s).
* *Default* (ID: `0x1`)
	* This is the default session, upon reset.
* *Programming* (ID: `0x2`)
	* It allows for programming-specific diagnostics.
* *Extended* (ID: `0x3`)
	* It allows for diagnostics, super-set from the *Default* session.
###### Positive Response
---
* Case: `#1`
	* Sub-Function: Session ID
	* Data (Response)
		* ${P2}_{Server\_Max}$ (Size: 2-bytes)
			* This represents the maximum time, in `ms`, before the server should respond positively, negatively, or with RCRRP.
		* ${P2*}_{Server\_Max}$ (Size: 2-bytes)
			* This represents the maximum time, in `10-ms`, before the server should respond positively, or negatively, after responding once with RCRRP.
##### Tester Present (0x3E)
---
Whenever a server transitions into a *Non-Default* session, it starts a timer, with value ${S3}_{Server}$, specified as `5-s` in [2].
* Upon the reception of any request before the timer expires, the timer resets.
* If the timer expires before any request is received,
	* the timer is stopped, and,
	* the server transitions to the *Default* session.

This service may be used to keep a server in a *Non-Default* session (i.e., by being sent periodically), in the absence of actual request(s).
###### Positive Response
---
* Case: `#1`
	* Sub-Function: `0x0`
##### ECU Reset (0x11)
---
This service may be used to trigger a reset, of different types, in the server (i.e., ECU).
###### Positive Response
---
* Case: `#1`
	* Sub-Function: Reset Type
##### Security Access (0x27)
---
This service may be used to unlock secured request(s) (VM-specific).
* Multiple levels of security access shall exist.
* Only a single level of security access may be granted, at any time.
* Each level of security access unlocks a sub-set of all secured request(s).

*Note:* This service is unsupported in *Default* session, and any session-transition shall revoke security access.
###### Positive Response
---
* Case: `#1`
	* Sub-Function: Request-Seed (i.e., security level).
		* This must be an odd-number.
	* Data (Response)
		* Seed (Size: Variable)
			* *Note:* If zero, then level of security access already granted.

* Case: `#2`
	* Sub-Function: Send-Key (i.e., security level plus one).
	* Data (Request)
		* Key (Size: Variable)
			* This key must correspond (cryptographically) to the seed.
## References
---
[1] Unified Diagnostic Services (UDS), Specification and Requirements, ISO 14229-1
[2] Unified Diagnostic Services (UDS), Session Layer Services, ISO 14229-2