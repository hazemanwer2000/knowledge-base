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
* Sub-function (Length: 1-byte)
	* Sub-function ID (Length: 6-bit)
	* "SuppressPositiveResponse" Option (Length: 1-bit)
* Data (Length: Variable)

The structure of a positive service response is as follows,
* SID + `0x40` (Length: 1-byte)
* Sub-function (Length: 1-byte)
	* Sub-function ID (Length: 6-bit)
	* `0x0` (Length: 1-bit)
* Data (Length: Variable)

The structure of a negative service response is as follows,
* `0x7F` (Length: 1-byte)
* SID (Length: 1-byte)
* NRC (Length: 1-byte)
#### Generic NRC(s)
---

### Services
---
#### 
## References
---
[1] Unified Diagnostic Services (UDS), Specification and Requirements, ISO 14229-1
[2] Unified Diagnostic Services (UDS), Session Layer Services, ISO 14229-2