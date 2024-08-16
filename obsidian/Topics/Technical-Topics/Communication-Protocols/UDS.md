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

| NRC    | Description                                  | Acronym | Description                                             |
| ------ | -------------------------------------------- | ------- | ------------------------------------------------------- |
| `0x13` | Incorrect Message Length Or Invalid Format   | IMLOIF  | Message length or format is incorrect.                  |
| `0x11` | Service Not Supported                        | SNS     | SID is not supported.                                   |
| `0x7F` | Service Not Supported In Active Session      | SNSIAS  | SID is not supported, in active session.                |
| `0x12` | Sub-Function Not Supported                   | SFNS    | Sub-Function is not supported.                          |
| `0x7E` | Sub-Function Not Supported In Active Session | SFNSIAS | Sub-Function is not supported, in active session        |
| `0x31` | Request Out Of Range                         | ROOR    | Data (in request) is not supported.                     |
| `0x22` | Conditions Not Correct                       | CNC     | Criteria (for request) is unmet.                        |
| `0x24` | Request Sequence Error                       | RSE     | Sequence of request(s) is invalid.                      |
| `0x21` | Busy (Repeat Request)                        | BRR     | Currently busy, and unable to perform request.          |
| `0x33` | Security Access Denied                       | SAD     | Request is secured, and server is in an unlocked state. |
| `0x11` | General Reject                               | GR      | Request rejected, reason unknown.                       |
### Services
---
#### 
## References
---
[1] Unified Diagnostic Services (UDS), Specification and Requirements, ISO 14229-1
[2] Unified Diagnostic Services (UDS), Session Layer Services, ISO 14229-2