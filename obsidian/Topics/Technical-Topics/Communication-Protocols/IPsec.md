──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
## Content
---
*Internet Protocol Security (IPsec)* is a suite of protocols, namely *IKEv2*, *ESP*, and *AH*, that operates at the *IP* layer of the *OSI* model, securing upper-layer payloads.
### Security Policy Database (SPD)
---
*IPsec* introduces a minimal firewall, that consists of traffic policies, managed inside a *Security Policy Database (SPD)*. An *SPD* stores each traffic policy as an entry, of which there are three types,

* *SPD-I*, which specifies a subset of inbound traffic (e.g., a range of IP-addresses, a range of ports, *UDP* or *TCP*), and whether to bypass (i.e., forward), or discard.
* *SPD-O*, which specifies a subset of outbound traffic, and whether to bypass, or discard.
* *SPD-P*, which specifies a subset of outbound traffic, and which protocol, *ESP* or *AH*, to use to protect.

*Note:* *SPD-I* entries do not apply to inbound *ESP* or *AH* traffic (i.e., traffic with an *ESP* or *AH* header) (see below).
### Security Association Database (SAD)
---
An *SA* encapsulates all required information, to protect traffic between any two peers. This includes,

* keys, used for *MAC* generation/verification, and encryption/decryption.
* security protocol to use (i.e., *ESP*, *AH*),
* *traffic selectors*, which specify which traffic the *SA* will apply to (e.g., a range of IP-addresses, a range of ports, *UDP* or *TCP*),
* and whether the *SA* is used for inbound or outbound traffic.
#### Outbound Traffic
---
Whenever an outbound packet matches an *SPD-P* entry, a *Security Association (SA)* is searched for inside the *Security Association Database (SAD)*, to be used to protect the packet. For an outbound *SA* to match, among possibly other points,

* the security protocol specified in the *SPD-P* entry, whether *ESP* or *AH*, must match the *SA*'s.
* the source and destination IP-addresses must be included in the *traffic selector(s)* of the *SA*,
* the source and destination ports must be included in the *traffic selector(s)* of the *SA* [optional],
* and the transport layer protocol type must match as well (e.g., *UDP*, *TCP*) [optional].

If no matching *SA* was found, a security protocol (e.g., *IKEv2*) is used to negotiate and establish an *SA* with the peer (see below).

*Note:* An *SA* may either be configured manually, or established using a security protocol.
#### Inbound Traffic
---
Whenever an inbound *AH* or *ESP* packet is received, a *Security Association (SA)* is searched for inside the *Security Association Database (SAD)*. For an inbound *SA* to match, among possibly other points,

* the security protocol of the packet, whether *ESP* or *AH*, must match the *SA*'s.
* the source and destination IP-addresses must be included in the *traffic selector(s)* of the *SA*,
* the source and destination ports must be included in the *traffic selector(s)* of the *SA* [optional],
* and the transport layer protocol type must match as well (e.g., *UDP*, *TCP*) [optional].

If no matching *SA* was found, the packet is discarded.
### IKEv2
---
*Internet Key Exchange (IKEv2)* protocol is used to negotiate and establish *SA(s)* with a peer.

Each exchange is a request and a response. There are four types of exchanges, as shown below.

| Name              | Description                                                                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| *IKE_SA_INIT*     | The first exchange between any two peers.                                                                                                        |
| *IKE_AUTH*        | The second exchange between any two peers, after which four *SA(s)* are considered established; an inbound and outbound *IKE_SA* and *CHILD_SA*. |
| *INFORMATIONAL*   | Exchange used to convey a variety of information, between any two peers with an established *IKE_SA*.                                            |
| *CREATE_CHILD_SA* | Exchange used to create additional *CHILD_SA(s)*, between any two peers with an established *IKE_SA*.                                            |

*Note:* An *IKE_SA* is an *SA*, used to secure *IKEv2* traffic.

*Note:* Even though an *IKE_SA* is not considered established before the *IKE_AUTH* exchange completes successfully, it is used to secure the *IKE_AUTH* exchange.
## *References*
---
[1] Security Architecture for the Internet Protocol, RFC 4301
[2] Internet Key Exchange (IKEv2) Protocol, RFC 4306
[3] IP Authentication Header (AH), RFC 4302
[4] IP Encapsulating Security Payload (ESP), RFC 4303