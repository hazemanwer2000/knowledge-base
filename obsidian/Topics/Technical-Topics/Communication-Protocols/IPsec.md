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
#### Format
---
Any *IKEv2* message consists of a header, and a number of consecutive payloads, each of a specific type, identified by the *Next Payload* field in the header, or preceding payload.

*Note:* If a payload of type *Encrypted* is found, it is decrypted and parsed into additional payloads. No more payloads may follow an *Encrypted* payload.

The header format, as shown below, consists of,

* the initiator's *SPI (Security Parameter Index)*, a unique (i.e., randomly generated) value, used as an index into the initiator's *SAD*,
* the responder's *SPI*,
* the *Next Payload* field,
* the version of *IKE* used,
* the *Exchange Type* field (e.g., *IKE_SA_INIT*),
* different flags (e.g., initiator/responder (see below), request/response),
* the *Message ID* field (see below),
* and the length of the complete IKE message (including the header), in bytes.

![[IKE-Header.png|600]]

*Note:* The *initiator* is the peer that sends the first request (i.e., an *IKE_SA_INIT* request). For the lifetime of the established *IKE* *SA*, this peer is referred to as the initiator in all *IKE* messages.

*Note:* The *Message ID* field is a sequence number that starts with zero, and is incremented with each request sent. A separate value is maintained by each peer. For example, after a successful *IKE_AUTH* exchange, the initiator's next *MID* is 2, and the responder's next *MID* is 0.
#### *IKE_SA_INIT* Exchange
---
The following payloads are typically contained within an *IKE_SA_INIT* request:

* *Security Association*
	* It contains nested *Proposal* payloads. Each *Proposal* payload contains nested *Transform* payloads.
	* Each *Transform* payload specifies a cryptographic algorithm, to be used for a specific operation (e.g., shared secret establishment, key derivation function, MAC generation, encryption).
* *Key Exchange*
	* It contains, for example, in the case of *ECDH*, the *initiator*'s public key used to establish the shared secret, from which a key derivation function derives additional keys, to be used for MAC generation and encryption.
* *Nonce
	* It contains a randomly generated value, that is used as input when deriving keys, called the *initiator*'s nonce value.
* *Notify: Signature Hash Algorithms*
	* It specifies the supported signature hash algorithms, used for signature generation/verification in the *AUTH* payload, part of the *IKE_AUTH* exchange.

*Note:* The *responder*'s SPI is set to all zeros, inside the *IKE_SA_INIT* request.

The following payloads are typically contained within an *IKE_SA_INIT* response:

* *Security Association*
	* It contains a single, nested *Proposal* payload, with nested *Transform* payloads selected from one of the initiator's *Proposal* payload(s).
	* There must be no two *Transform* payloads that specify cryptographic algorithms, to be used for the same operation (e.g., Encryption; *AES-CBC-256* and *AES-CBC-128*).
* *Key Exchange*
	* (...)
* *Nonce
	* (...)
* *Notify: Signature Hash Algorithms*
	* It specifies the signature hash algorithm to be used, selected from the *initiator*'s list of supported algorithms.
* *Certificate Request*
	* It contains the hash value, usually using *SHA-1* *CHF*, of the public key of one of the *CA(s)* of the responder, that it shall use to establish a chain of trust (see below).

*Note:* Any *Proposal* payload specifies the relevant security protocol in a field, called *Protocol ID*. *Security Association* payloads inside *IKE_SA_INIT* requests and responses contain *Proposal* payloads with a *Protocol ID* that specifies *IKE* as the security protocol. Hence, *Security Association* agreement, as a result of the *IKE_SA_INIT* exchange, is used to establish two *IKE_SA(s)*, inbound and outbound, for each peer.
#### *IKE_AUTH* Exchange
---
*IKE_AUTH* request and response contain a single *Encrypted* payload, that is encrypted, and authenticated (via an attached *MAC*).

The following payloads are typically contained within an *IKE_AUTH* request (after decryption of the *Encrypted* payload):

* *Security Association*
	* Use-case is similar to an *IKE_SA_INIT* request, but with *Proposal* payloads with a *Protocol ID* that specifies either *AH* or *ESP* as the security protocol.
* *Certificate*
	* It contains a certificate, usually of type *x509* and is encoded in *DER* format. The certificate may be the initiator's certificate, or an intermediate certificate.
* *Certificate Request*
	* (...)
* *Authentication*
	* It contains the signature, calculated over the *Identification* payload, but not only.
* *Identification*
	* Usually, it contains the *subject* field of the initiator's end-certificate.
* *Notify: Use Transport Mode* or *Notify: Use Tunnel Mode* 
	* It specifies which mode of operation of the security protocols (i.e., *AH* and *ESP*) shall be used (see below).
* *Traffic Selector: Initiator* and *Traffic Selector: Responder*
	* It specifies the traffic selectors, to be associated with the *CHILD_SA* to be established.

The following payloads are typically contained within an *IKE_AUTH* response (after decryption of the *Encrypted* payload):

* *Security Association*
	* (...)
* *Certificate*
	* (...)
* *Authentication*
	* (...)
* *Identification*
	* (...)
* *Notify: Use Transport Mode* or *Notify: Use Tunnel Mode* 
	* (...)
* *Traffic Selector: Initiator* and *Traffic Selector: Responder*
	* It specifies the traffic selectors, to be associated with the *CHILD_SA* to be established, and must be a subset of the traffic selectors in the *IKE_AUTH* request.
## *References*
---
[1] Security Architecture for the Internet Protocol, RFC 4301
[2] Internet Key Exchange (IKEv2) Protocol, RFC 4306
[3] IP Authentication Header (AH), RFC 4302
[4] IP Encapsulating Security Payload (ESP), RFC 4303