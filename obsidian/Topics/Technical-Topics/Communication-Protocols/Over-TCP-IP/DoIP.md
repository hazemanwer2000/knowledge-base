──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#Acronyms|Acronyms]]
- [[#Definitions|Definitions]]
- [[#Overview|Overview]]
	- [[#Overview#Message Structure|Message Structure]]
- [[#Communication Flow|Communication Flow]]
	- [[#Communication Flow#Vehicle Identification|Vehicle Identification]]
	- [[#Communication Flow#Routing Activation|Routing Activation]]
	- [[#Communication Flow#Diagnostic Message(s)|Diagnostic Message(s)]]
## Content
---
*Diagnostic communication over IP (DoIP)* is an automotive-oriented protocol, that enables diagnostics within IP networks. 

Application-layer protocols (e.g., UDS) run over *DoIP*, within IP networks.
### Acronyms
---
* **VM -** Vehicle Manufacturer
* **RC -** Response Code
	* **PRC -** Positive RC
	* **NRC -** Negative RC
### Definitions
---
* **Vehicle Identification Number (VIN):** A value that identifies a vehicle uniquely. It is configured/programmed in the *VIN-master* ECU, and communicated to all *VIN-slave* ECU(s).
### Overview
---
Within a vehicle, multiple ECU(s) reside, of which a subset serve as *DoIP* node(s).

A subset of *DoIP* node(s) serve as *DoIP* gateway(s). A *DoIP* gateway connects two or more sub-network(s) of ECU(s), usually connecting one or more (minor, leaf) non-IP-based (e.g., CAN, LIN) sub-network, to one (major, non-leaf) IP-based sub-network.
#### Message Structure
---
Any *DoIP* message consists of a generic header, payload-type-specific content, and payload (i.e., UDS message).

The following are fields of the generic header.

| Name                         | Length   | Description                                     |
| ---------------------------- | -------- | ----------------------------------------------- |
| Protocol Version             | 1        | *DoIP* protocol version.                        |
| Inverse Protocol Version     | 1        | Bitwise-*NOT* of the "Protocol Version" field.  |
| Payload Type                 | 2        | Specifies the type of payload.                  |
| Payload Length               | 4        | Specifies length of payload.                    |
| Payload-Type-Specific Fields | Variable | Contains fields, specific to each payload-type. |
The following are payload types.

| Name                            | Transport Protocol     | Port Number          |
| ------------------------------- | ---------------------- | -------------------- |
| Vehicle Announcement            | UDP, Multicast         | Dst: `UDP_DISCOVERY` |
| Vehicle Identification Request  | UDP, Multicast/Unicast | Dst: `UDP_DISCOVERY` |
| Vehicle Identification Response | UDP, Unicast           | Src: `UDP_DISCOVERY` |
| Routing Activation Request      | TCP                    | Dst: `TCP_DATA`      |
| Routing Activation Response     | TCP                    | Src: `TCP_DATA`      |
| Diagnostic Message              | TCP                    | Dst: `TCP_DATA`      |
| Diagnostic Message *ACK*        | TCP                    | Src: `TCP_DATA`      |
| Diagnostic Message *NACK*       | TCP                    | Src: `TCP_DATA`      |
### Communication Flow
---
#### Vehicle Identification
---
After a *DoIP* node is assigned an IP address (e.g., via *DHCP*, or *AUTOIP*), it shall,
* Wait for `T_Announce_Wait` seconds.
* Send `N_Announce_Num` Vehicle Announcement message(s), with `T_Announce_Interval` delay in-between.

If not received by the tester, a Vehicle Identification Request message shall be sent, and responded to, by applicable *DoIP* node(s), within `T_Announce_Wait` seconds.

The following are fields, specific to the Vehicle Announcement, or Identification Response payload-type.

| Name                    | Length | Description                                                                                                                                                                                                               |
| ----------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| VIN                     | 17     | The VIN of the vehicle the *DoIP* node belongs to.<br>If not available, shall be all `0xFF` or `0x00`.                                                                                                                    |
| Logical Address         | 2      | Physical address of a specific application-layer within the *DoIP* node (i.e., *DoIP entity*), of which there may be multiple.<br>It must be unique across a vehicle.<br>If not available, shall be all `0xFF` or `0x00`. |
| EID                     | 6      | Uniquely identifies the *DoIP* node, even before a VIN/GID is available.<br>If not available, shall be all `0xFF` or `0x00`.                                                                                              |
| GID                     | 6      | If the VIN is not available, a GID may be used instead.<br>For example, the GID may be the *MAC* address of the *GID-master* ECU.<br>If not available, shall be all `0xFF` or `0x00`.                                     |
| Further Action Required | 1      | Specifies additional information.                                                                                                                                                                                         |
| VIN/GID Sync Status     | 1      | Specifies whether a VIN/GID is available, and has been synced across the vehicle.                                                                                                                                         |

VIN/GID Sync Status field conveys that VIN/GID value is not synced across the vehicle by one or more *DoIP* node(s), `X`, the tester may,
* Wait for `T_Vehicle_Discovery` seconds.
* Send Vehicle Identification Request message(s) to all `X` ECU(s).
Until the VIN/GID is synced across the vehicle.
#### Routing Activation
---
Before being able to send a diagnostic message to a *DoIP* entity,
* TCP connection must be established.
* Routing Activation Request message is sent from tester.
* Routing Activation Response message is sent from *DoIP* entity, with a PRC.

The following are fields, specific to the Routing Activation Request payload-type.

| Name            | Length | Description                 |
| --------------- | ------ | --------------------------- |
| Source Address  | 2      | Physical address of tester. |
| Activation Type | 1      | VM-specific.                |
| Reserved        | 8      | None.                       |

The following are fields, specific to the Routing Activation Response payload-type.

| Name                | Length | Description                        |
| ------------------- | ------ | ---------------------------------- |
| Destination Address | 2      | Physical address of tester.        |
| Source Address      | 2      | Physical address of *DoIP* entity. |
| Activation RC       | 1      | RC of activation.                  |
| Reserved            | 8      | None.                              |
#### Diagnostic Message(s)
---
Upon successful routing activation, a *DoIP* entity becomes diagnosable. For example,
* A UDS request is sent by a tester, as a Diagnostic Message message.
* *DoIP* entity responds with a Diagnostic Message (N)ACK message, within `T_Diagnostic_Message`.
* Later, if previously ACK'ed, a UDS response is sent by the *DoIP* entity, as a Diagnostic Message message.
	* *Note:* Diagnostic Message message(s) sent by the *DoIP* entity do not require acknowledgement from the tester.

The following are fields, specific to the Diagnostic Message payload-type.

| Name           | Length | Description                   |
| -------------- | ------ | ----------------------------- |
| Source Address | 2      | Physical address of sender.   |
| Target Address | 2      | Physical address of receiver. |

The following are fields, specific to the Diagnostic Message *ACK* payload-type.

| Name           | Length | Description                   |
| -------------- | ------ | ----------------------------- |
| Source Address | 2      | Physical address of sender.   |
| Target Address | 2      | Physical address of receiver. |
| *ACK* code     | 1      | Positive *ACK* code.          |

The following are fields, specific to the Routing Activation *NACK* payload-type.

| Name           | Length | Description                   |
| -------------- | ------ | ----------------------------- |
| Source Address | 2      | Physical address of sender.   |
| Target Address | 2      | Physical address of receiver. |
| *NACK* code    | 1      | Negative *ACK* code.          |
## References
---
[1] Diagnostic communication over IP (DoIP), General information and Use-case definition, ISO 13400-1
[2] Diagnostic communication over IP (DoIP), Transport protocol and Network layer services, ISO 13400-2