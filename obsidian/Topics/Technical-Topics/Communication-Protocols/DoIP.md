──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*Diagnostic communication Over IP (DoIP)* is an automotive-oriented protocol, that enables diagnostics within IP networks. 

Application-layer protocols (e.g., UDS) run over *DoIP*, within IP networks.
### Overview
---
Within a vehicle, multiple ECU(s) reside, of which a subset serve as *DoIP* node(s).

A subset of *DoIP* node(s) serve as *DoIP* gateway(s). A *DoIP* gateway connects two or more sub-network(s) of ECU(s), usually connecting one or more (minor, leaf) non-IP-based (e.g., CAN, LIN) sub-network, to one (major, non-leaf) IP-based sub-network.
#### Message Structure
---
Any *DoIP* message consists of a generic header, payload-type-specific content, and payload (i.e., UDS message).

The following are fields of the generic header.

| Name                         | Size     | Description                                     |
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
| Vehicle Identification Response | UDP, Unicast           | ...                  |
| Routing Activation Request      | TCP                    | Dst: `TCP_DATA`      |
| Routing Activation Response     | TCP                    | ...                  |
| Diagnostic Message              | TCP                    | ...                  |
| Diagnostic Message *ACK*        | TCP                    | ...                  |
| Diagnostic Message *NACK*       | TCP                    | ...                  |
| Alive Check Request             | TCP                    | ...                  |
| Alive Check Response            | TCP                    | ...                  |

#### Communication Flow
---
After a *DoIP* node is assigned an IP address (e.g., via *DHCP*, or *AUTOIP*), it shall,
* Wait for `T_Announce_Wait` seconds.
* Send `N_Announce_Num` Vehicle Announcement message(s), with `T_Announce_Interval` delay in-between.

The following are fields, specific to the Vehicle Announcement payload-type.

| Name |     |
| ---- | --- |
|      |     |

## References
---
[1] Diagnostic communication Over IP (DoIP), General information and Use-case definition, ISO 13400-1
[2] Diagnostic communication Over IP (DoIP), Transport protocol and Network layer services, ISO 13400-2