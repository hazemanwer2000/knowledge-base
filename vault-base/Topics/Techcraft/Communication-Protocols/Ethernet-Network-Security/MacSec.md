──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#Connectivity Association (CA)|Connectivity Association (CA)]]
	- [[#Connectivity Association (CA)#Key Hierarchy|Key Hierarchy]]
	- [[#Connectivity Association (CA)#Secure Channel(s) (SC)|Secure Channel(s) (SC)]]
	- [[#Connectivity Association (CA)#Secure Association(s) (SA)|Secure Association(s) (SA)]]
- [[#*Mka* Protocol|*Mka* Protocol]]
	- [[#*Mka* Protocol#Authentication|Authentication]]
	- [[#*Mka* Protocol#Replay Protection|Replay Protection]]
	- [[#*Mka* Protocol#Liveness|Liveness]]
	- [[#*Mka* Protocol#Key-Server Election|Key-Server Election]]
	- [[#*Mka* Protocol#Frame Structure|Frame Structure]]
		- [[#Frame Structure#Basic Parameter Set|Basic Parameter Set]]
		- [[#Frame Structure#`Live/Potential Peer List` Set|`Live/Potential Peer List` Set]]
		- [[#Frame Structure#`MacSec SAK Use` Set|`MacSec SAK Use` Set]]
		- [[#Frame Structure#`Distributed SAK` Set|`Distributed SAK` Set]]
		- [[#Frame Structure#`Announcement` Set|`Announcement` Set]]
		- [[#Frame Structure#`ICV Indicator` Set|`ICV Indicator` Set]]
- [[#*MacSec* Protocol|*MacSec* Protocol]]
	- [[#*MacSec* Protocol#Cipher Suite(s)|Cipher Suite(s)]]
	- [[#*MacSec* Protocol#Frame Structure|Frame Structure]]
## Content
---
*Media Access Control (MAC) Security* protocol, termed *MacSec*, is an Ethernet Network Security protocol, operating at the *Data-Link* layer of the *OSI* model. [1]

It is meant to secure Ethernet frames between two or more entities within a *LAN*, collectively forming a *Connectivity Association (CA)*.

*MacSec* relies on *MAC Security Key Agreement (Mka)* protocol to authenticate entities, and exchange session-key(s).
### Connectivity Association (CA)
---
An entity within a *CA* must possess its key, abbreviated as *CAK*.

*Note:* A *CAK* must be an *AES-128*, or an *AES-256* key.

*Note:* This document assumes *CAK* is a pre-shared key, abbreviated as *PSK*.

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
* its identifier (see below), abbreviated as *KI*,
* a 2-bit association number, abbreviated as *AN*,
* and a 4-byte Packet Number, abbreviated as *PN*, starting with 1, and incrementing with each *MacSec* frame sent, secured via *SAK*.
### *Mka* Protocol
---
#### Authentication
---
Every *Mka* frame is authenticated via a 128-bit ICV, calculated as follows,

```
M = CONCAT(DST-ADDR, SRC-ADDR, ETHERTYPE, PAYLOAD)

CMAC(ICK, M)
```
#### Replay Protection
---
Every *Mka* entity, at first, generates a random 96-bit value, as its *Message Identifier (MI)*.

With every *Mka* frame sent, it increments its 32-bit *Message Number (MN)*, starting with 1.

*Note:* An *Mka* frame with the same *MI* and *MN* must never be received twice, during a session.

If an *Mka* entity reaches the maximum value of its *MN*, it shall generate a new *MI* and reset its *MN*, communicating as a new *Mka* entity.
#### Liveness
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
#### Key-Server Election
---
A Key-Server is elected from all entities within the *CA*, as the entity responsible for generation and distribution of session-key(s), *SAK*(s).

Election metrics are based on,
* Key-Server Priority ($\downarrow$), a 1-byte value, sent in every *Mka* frame.
* If equal, *SCI* ($\downarrow$) is used as a tie-breaker.

For each *SAK* generated and distributed by a Key-Server, its *KI* consists of,
* the Key-Server's *MI*, and,
* a 32-bit *Key Number (KN)*, starting with 1, and incrementing.
#### Frame Structure
---
*Mka* frame(s) are sent over *EAPoL (Extensible Authentication Protocol over LAN)*, which is out-of-scope of this document.

*Note:* *EAPoL* specifies the destination MAC address of *Mka* frame(s) as one of multiple group address(es), specified in [2].

*Note:* Ether-Type of *EAPoL* frame(s) is `0x888E`.

An *EAPoL* frame consists of,
* Protocol Version (Size: 1-byte), specified in [2] as `0x03`.
* Packet Type (Size: 1-byte), specified as `0x05` for *Mka* frame(s).
* Packet Length (Size: 2-bytes).
* Packet Body (e.g., *Mka* frame).

An *Mka* frame consists of,
* Basic Parameter Set.
* Zero, or more, (optional) Parameter Set(s).
* `ICV Indicator` Set.

The encoding of a Parameter Set is shown below.

![[MKA-Parameter-Set-Encoding.png|500]]

*Note:* For a Basic Parameter Set, only, the first byte consists of the *Mka* version identifier, specified in [2] as `0x03`.

*Note:* Total size, in bytes, of a Parameter Set must be a multiple of 4.
##### Basic Parameter Set
---
* Specific Parameters:
	* Key-Server Priority (Size: 1-byte)
	* Key-Server Flag (Size: 1-bit)
	* *MacSec* Desired Flag (Size: 1-bit)
	* *MacSec* Capability (Size: 2-bits)
		* `0b00` - Incapable
		* `0b01` - Integrity without Confidentiality
		* `0b10` - Integrity with/without Confidentiality
		* `0b11` - Integrity with/without Confidentiality, with selectable offset
* Body:
	* *SCI* (Size: 8-bytes)
	* *MI* (Size: 12-bytes)
	* *MN* (Size: 4-bytes)
	* Algorithm Agility (Size: 4-bytes), specified in [2] as `0x0080C201`.
	* *CKN* (Size: 32-bytes)
		* *Note:* If the size of *CKN* is less than 32-bytes, it is right-zero-padded.
##### `Live/Potential Peer List` Set
---
* Type: 
	* `Live Peer List` - `0x01`
	* `Potential Peer List` - `0x02`
* Body:
	* Multiple of,
		* *MI* (Size: 12-bytes)
		* *MN* (Size: 4-bytes)
##### `MacSec SAK Use` Set
---
* Type: `0x03`
* Specific Parameters:
	* Double of (i.e., Latest/Old)
		* *AN* (Size: 2-bits)
		* TX Flag (Size: 1-bit)
		* RX Flag (Size: 1-bit)
	* Plain TX (Size: 1-bit)
	* Plain RX (Size: 1-bit)
	* Reserved (Size: 1-bit)
	* Delay Protect Flag (Size: 1-bit)
		* *Note:* This is set if Replay Protection is enabled for *MacSec*-protected frame(s). If reset, Lowest Acceptable *PN* (see below) may be set to zero.
* Body:
	* Double of (i.e., Latest/Old)
		* *KI* (Size: 16-bytes)
		* Lowest Acceptable *PN* (Size: 4-bytes)
			* This specifies the *PN* value associated with this *Mka* entity's *SA* that contains *KI*, `(MKA-HELLO-TIME)/2` prior to this *Mka* frame's transmission.
			* It is monitored by the Key-Server.
				* If it exceeds `0xC0000000`, as specified in [2], for the Latest *KI*, for any *Mka* entity,
				* then, the Key-Server shall generate and distribute a new *SAK*.
##### `Distributed SAK` Set
---
* Type: `0x04`
* Specific Parameters:
	* *AN* (Size: 2-bits)
	* Confidentiality Offset (Size: 2-bits)
		* `0b00` - No Confidentiality
		* `0b01` - `0`
		* `0b10` - `30`
		* `0b11` - `50`
* Body:
	* *KN* (Size: 4-bytes)
	* AES Key-Wrap of *SAK* (Size: Variable)
##### `Announcement` Set
---
* Type: `0x07`
* Body:
	* Multiple of *TLV* (i.e., Type-Length-Value).
		* Type (Size: 7-bits)
		* Length (Size: 9-bits)
		* Value (Size: Variable)

For a `MacSec Cipher Suites` *TLV*, which specifies the Cipher Suite(s) supported by an *Mka* entity,
* Type: `112`
* Value:
	* Multiple of,
		* Reserved (Size: 14-bits)
		* *MacSec* Capability (Size: 2-bits)
		* Cipher Suite Reference Number (Size: 8-bytes), as specified in [1]

* *Note:* Mandatory Cipher Suite(s), as specified in [1], are not included in a `MacSec Cipher Suites` *TLV*.
##### `ICV Indicator` Set
---
* Type: `0xFF`
* Body:
	* ICV (Size: 16-bytes)
### *MacSec* Protocol
---
#### Cipher Suite(s)
---
Mandatory Cipher Suite(s), as specified in [1], include,
* GCM-AES-128
	* MAC Truncation Length as 128-bits.
	* IV as the concatenation of *SCI*, of the *SC* used, and *PN*, of the *SA* used.

Optional Cipher Suite(s), as specified in [1], include,
* GCM-AES-256
#### Frame Structure
---
A frame is encapsulated within a *MacSec* frame as shown below.

![[MACSEC-Frame-Structure.png|700]]

*Note:* Ether-Type of *MacSec* frame(s) is `0x88E5`.

*SecTAG* consists of,
* Tag Control Information (TCI) (Size: 6-bits)
	* *Note:* Refer to [1] for the encoding of TCI.
* *AN* (Size: 2-bits)
* Short Length (SL) (Size: 1-byte)
	* *Note:* Refer to [1] for the encoding of SL.
* *PN* (Size: 4-bytes)
* *SCI* (Size: 8-bytes) (Optional)
## References
---
[1] Media Access Control (MAC) Security, IEEE 802.1AE-2018
[2] Port-Based Network Access Control, IEEE 802.1X-2020