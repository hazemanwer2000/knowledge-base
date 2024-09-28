──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*Media Access Control (MAC) Security* protocol, termed *MacSec*, is an Ethernet Network Security protocol, operating at the *Data-Link* layer of the *OSI* model. [1]

It is meant to secure Ethernet frames between two or more entities within a *LAN*, collectively forming a *Connectivity Association (CA)*.

*MacSec* relies on *MAC Security Key Agreement (Mka)* protocol to authenticate entities, and exchange session-key(s).
### Connectivity Association (CA)
---
An entity within a *CA* must possess its key, abbreviated as *CAK*.

*Note:* A *CAK* must be an *AES-128*, or an *AES-256* key.

Every *CAK* (i.e., *CA*) is identified via its number, abbreviated as *CKN*.

*Note:* A *CKN* must be of size `N` bytes, where `1 <= N <= 32`.
#### Key Hierarchy
---
A *CAK* is used to derive two more keys,
* Integrity Check Value (ICV) Key, abbreviated as *ICK*, used to secure *Mka* frames, and,
* Key-Encrypting Key, abbreviated as *KEK*, used to wrap *MacSec* session-key(s).

*Note:* *ICK*, or *KEK*, must be an *AES-128*, or an *AES-256* key.

The following Key-Derivation Function (KDF), specified in [2], is used.

```
Input:
	Key - AES-128 or AES-256 key
	Label - Arbitrary bit-string (e.g., output-key's purpose)
	KeyID - Arbitrary bit-string (e.g., 'Key' ID)
	Length - Length of output-key in bit(s) (Size: 2-bytes)
```

```
Constants:
	PRF - Represents CMAC-128, if 'Key' is an AES-128 key (...)
	B - Represents the AES block size, in bit(s)
```

```
I = (Length + (B - 1)) / B

FOR i FROM 1 TO I
	RESULT = CONCAT(RESULT, 
		PRF(Key, CONCAT(i, Label, 0x00, KeyID, Length))
	)

RESULT = MSB(Length, RESULT)
```

To derive *ICK* and *KEK*,

```
ICK = KDF(
	CAK,
	"IEEE8021 ICK",
	MSB(128, RPAD(128, CKN)),
	Length
)

KEK = KDF(
	CAK,
	"IEEE8021 KEK",
	MSB(128, RPAD(128, CKN)),
	Length
)
```
#### Secure Channel(s) (SC)
---
Every entity within a *CA* possesses a *Secure Channel (SC)*, through which it may communicate frames to other entities within the *CA*.

Every *SC* is identified via an 8-byte identifier, abbreviated as *SCI*.

Every *SCI* consists of,
* the *MAC* address of the entity, and,
* an arbitrary, 2-byte (physical-)port identifier.
#### Secure Association(s) (SA)
---
Every entity within a *CA* possesses one, or more *Secure Association(s) (SA)*.

Each *SA* consists of,
* a session-key, abbreviated as *SAK*,
* and a 2-bit association number, abbreviated as *AN*.
### *Mka* Protocol
---
#### Introduction
---
##### Authentication
---
Every *Mka* frame is authenticated via a 128-bit ICV, calculated as follows,

```
M = CONCAT(DST-ADDR, SRC-ADDR, ETHERTYPE, PAYLOAD)

CMAC(ICK, M)
```
##### Replay Protection
---
Every *Mka* entity, at first, generates a random 96-bit value, as its *Message Identifier (MI)*.

With every *Mka* frame sent, it increments its 32-bit *Message Number (MN)*, starting with 1.

*Note:* An *Mka* frame with the same *MI* and *MN* must never be received twice, during a session.

If an *Mka* entity reaches the maximum value of its *MN*, it shall generate a new *MI* and reset its *MN*, communicating as a new *Mka* entity.
##### Liveness
---
*Mka* frame(s) are sent periodically, frame per entity per `MKA-HELLO-TIME`, specified in [2] as `2-s`. 

Each entity maintains a *Live-Peer-List* and a *Potential-Peer-List*, sent in every *Mka* frame.

An entity is added to the *Live-Peer-List*, if,
* an *Mka* frame has been received with the receiving entity's *MI* and a (recent) *MN* present in either list(s).

An entity is added to the *Potential-Peer-List*, if,
* an *Mka* frame has been received from the corresponding entity, or,
* an *Mka* frame has been received from a "Live" entity, that includes the corresponding entity in its *Live-Peer-List*.

An entity is removed from both list(s), if,
* an *Mka* frame has not been received from the corresponding entity for at-least `MKA-LIFE-TIME`, specified in [2] as `6-s`.
#### Frame Structure
## References
---
[1] Media Access Control (MAC) Security, IEEE 802.1A-2018
[2] Port-Based Network Access Control, IEEE 802.1X-2020