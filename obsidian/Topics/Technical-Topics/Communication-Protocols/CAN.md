──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#Acronyms|Acronyms]]
- [[#Basics|Basics]]
	- [[#Basics#Frame Structure|Frame Structure]]
	- [[#Basics#Extended-Format|Extended-Format]]
	- [[#Basics#Bit Stuffing|Bit Stuffing]]
	- [[#Basics#Overload Frame(s)|Overload Frame(s)]]
	- [[#Basics#Error Frame(s)|Error Frame(s)]]
- [[#CAN-FD|CAN-FD]]
	- [[#CAN-FD#Frame Structure|Frame Structure]]
	- [[#CAN-FD#Extended-Format|Extended-Format]]
	- [[#CAN-FD#Bit Stuffing|Bit Stuffing]]
- [[#Node State(s)|Node State(s)]]
## Content
---
*Controller Area Network (CAN)* is a serial, half-duplex, asynchronous, message-oriented and `N:N` (i.e., `Master:Slave`) *L2*-protocol.

It is usually employed in the automotive industry, specified in [1].
### Acronyms
---
* `RTR` - Remote Transmission Request
* `IDE` - Identifier Extension Request
* `FDF` - FD-Format
* `DLC` - Data Length Code
* `SRR/RRS` - Substitute Remote-Request / Remote-Request Substitution
* `EOF` - End of Frame
* `ITM` - Intermission-Space
* `RRS` - Remote Request Substitution
* `BRS` - Bit-Rate Switch
* `ESI` - Error State Indicator
### Basics
---
Each *CAN* node is connected to the *CAN* network via a single (logical-)line.

Each *CAN* frame is,
* identified uniquely via an identifier,
* may only be transmitted by a single *CAN* node, and,
* is processed by all *CAN* node(s) in the network.

While the bus is idle, it is in recessive state, and a *CAN* node may begin the transmission of a *CAN* frame.

*Note:* If multiple *CAN* node(s) begin the transmission of a *CAN* frame, arbitration takes place.
#### Frame Structure
---
The following is the structure of a *CAN* frame.

![[CAN-Frame-Format-Basic.png|550]]

A *CAN* frame may be categorized based on its purpose.
* A *Data* Frame, whose purpose is to publish data,
	* contains the Data Field, and,
	* forces `RTR` bit to be dominant.
* A *Remote* Frame, whose purpose is to request data, from its publisher,
	* omits the Data Field, and,
	* forces `RTR` bit to be recessive.

*Note*: Based on arbitration, a Data *CAN* frame with the same ID is always prioritized over a Remote *CAN* frame.

The `DLC` field specifies the number of bytes in the Data field.

| DLC field | No. of bytes |
| --------- | ------------ |
| `N <= 8`  | `N`          |
| `N > 8`   | `8`          |

After each *CAN* frame, the following field(s) exist:
* `ACK` field
	* `ACK` bit (Size: 1-bit)
		* *Note:* All *CAN* node(s) shall acknowledge all CRC-valid *CAN* frame(s), by asserting a dominant state.
	* `ACK` delimiter (Size: 1-bit)
* `EOF` field (Size: 8-bits)
* `ITM` field (Size: 3-bits)

![[CAN-Frame-Format-ACK-EOF.png|225]]
#### Extended-Format
---
A *CAN* frame may be in Extended format, with an extension to the ID field, as shown below.

![[CAN-Frame-Format-Extended.png|700]]

*Note:* Based on arbitration, a *CAN* frame in Extended format is always de-prioritized.
#### Bit Stuffing
---
*Bit Stuffing* is the transmission of an inverted, negligible (i.e., not included in the CRC calculation) bit value, with every transmission of five homogeneous, consecutive bit value(s) within a *CAN* frame.
#### Overload Frame(s)
---
An *Overload* *CAN* frame is a special frame, that is,
* first-transmitted by a receiving *CAN* node during an `ITM` field,
* signals to all other *CAN* node(s) that delay in the transmission of the next *CAN* frame on the bus is required, and,
* triggers all other *CAN* node(s) to transmit a (reactive) *Overload* *CAN* frame themselves.

*Note:* It has the same structure as an *Error* *CAN* frame (see below).
#### Error Frame(s)
---
An *Error* *CAN* frame is a special frame, that is,
* first-transmitted by a transmitting, or receiving node during the transmission of a *CAN* frame, `ACK` field, or `EOF` field,
* signals to all other *CAN* node(s) that an error-condition has been detected, and,
* triggers all other *CAN* node(s) to detect an error-condition themselves (via Stuff Error) and transmit an *Error* *CAN* frame.

It consists of,
* Error Flag (Size: 6-12 bits)
	* *Note:* The transmitting *CAN* node waits for the bus to be in recessive state, to mark the end of the Error Flag.
* Error delimiter (Size: 8-bits)
* `ITM` field (Size: 3-bits)

An error-condition may be,
* Bit Error
	* While bit monitoring, the **transmitter** reads a different bit-value than the bit-value transmitted.
* Stuff Error
	* While bit monitoring, the **transmitter**, or **receiver** reads six homogeneous, consecutive bit value(s).
* CRC Error
	* CRC verification by a **receiver** fails.
* Form Error
	* An unexpected bit-value, according to the format, is read by a **receiver**.
* ACK Error
	* While bit monitoring, the **transmitter** reads `ACK` bit as recessive (i.e., unacknowledged by all receivers).
### CAN-FD
---
*CAN Flexible Data-Rate (CAN-FD)* is a specification of the *CAN* protocol, that allows for higher transmission rates, and larger payload per frame.
#### Frame Structure
---
The following is the structure of a *CAN-FD* frame, with Data field consisting of 16 bytes or less, and more than 16 bytes, respectively.

![[CAN-Frame-Format-Basic-FD.png|675]]
![[CAN-Frame-Format-Basic-FD-Plus-16.png|675]]

*Note:* Only *Data* *CAN-FD* frames exist. 

*Note:* *CAN* and *CAN-FD* frames are arbitrated between, based only on the ID field (and ID Extension field), since an ID may only be associated with either *CAN* or *CAN-FD*.

The `DLC` field specifies the number of bytes in a *CAN-FD* Data field.

| DLC field | No. of bytes |
| --------- | ------------ |
| `N <= 8`  | `N`          |
| `9`       | `12`         |
| `10`      | `16`         |
| `11`      | `20`         |
| `12`      | `24`         |
| `13`      | `32`         |
| `14`      | `48`         |
| `15`      | `64`         |

If `BRS` bit is recessive, variable-speed transmission is used for this *CAN-FD* frame, as shown below.

![[CAN-FD-Variable-Rate.png|850]]

If `ESI` bit is recessive, the transmitting node is in an error-passive state (see below).
#### Extended-Format
---
The following is the structure of a *CAN-FD* frame in Extended-Format, with Data field consisting of 16 bytes or less, and more than 16 bytes, respectively.

![[CAN-Frame-Format-Extended-FD.png|850]]
![[CAN-Frame-Format-Extended-FD-Plus-16.png|850]]
#### Bit Stuffing
---
In *CAN-FD*, *Fixed* Bit Stuffing occurs within the CRF field, as shown below.

![[CAN-FD-Fixed-Bit-Stuffing.png|850]]
### Node State(s)
--- 
Upon start-up, each *CAN* node shall,
* enter the **bus-integration** (implicit) state, and,
* wait for an **idle-condition** to occur, before entering the **error-active** state.

*Note:* An idle-condition occurs with the detection of 11 consecutive, recessive bits (e.g., `EOF` field or Error/Overload Delimiter, followed by `ITM` field).

Each *CAN* node maintains two error counters, TX and RX, that are incremented/decremented according to events outlined in [1].

Transitions between error-active, **error-passive**, and **bus-off** state(s) are shown below.

![[CAN-Node-State-Diagram.png|450]]

In error-passive state, a node,
* may only transmit passive Error Flag(s) (i.e., with all recessive-bit(s)), and,
* after frame transmission, and the associated `ITM` field, shall wait for 8 recessive-bits (called, *Suspend Transmission Time*), before it is possible to transmit another frame.
### Transport-Layer
---
*CAN-TP*, as specified in [2], is used to realize *Diagnostics over CAN (DoCAN)*.
#### Addressing Format(s)
---
In *CAN-TP*, several addressing format(s) are possible.
##### Normal Addressing
---
In normal addressing, a *CAN* frame ID uniquely identifies the logical source and destination address(es).

For example, if a tester, `0x01`, should diagnose two ECU(s), `0x02` and `0x03`, then, four *CAN* frame ID(s) shall be reserved for this purpose.
#### Protocol Control Information
---
In *Protocol Control Information (PCI)*, which precedes the message payload, the high nibble of the first byte denotes the frame type, as either,
* `0x0` - Single Frame (SF),
* `0x1` - First Frame (FF),
* `0x2` - Consecutive Frame (CF), and,
* `0x3` - Flow-Control Frame (FC).

Let `L` be the length of the message payload.

For SF(s),
* For *CAN* frame(s) with length `<= 8`,
	* the low nibble of the first byte denotes `L`.
* For *CAN* frame(s) with length `> 8`,
	* the low nibble of the first byte is set to zero, and,
	* the second byte denotes `L`

![[CAN-TP-Unsegmented.png|500]]

For FF(s),
* For *CAN* frame(s) with length `>= 8`,
	* If `L < 4096`,
		* the low nibble of the first byte (as the most significant part), along with the second byte, denote `L`.
	* Else,
		* the low nibble of the first byte (as the most significant part), along with the second byte, are set to zero, and,
		* the next four byte(s) denote `L`.
* *Note:* *CAN* frame(s) with length `< 8` are not allowed.

For CF(s),
* All (but the last) *CAN* frame(s) should have a length equal to that of the associated FF.
* The low nibble of the first byte denotes the frame counter, which begins with 1, and wraps to 0.

For FC(s),
* The low nibble of the first byte denotes the flow status.
	* `0x0` - `ContinueToSend (CTS)`
		* The sender shall continue to send a maximum number of *BS* CF(s).
		* If *BS* is zero, then,
			* the sender shall continue to send all remaining CF(s), and,
			* shall expect the reception of no more FC(s).
	* `0x1` - `Wait (WAIT)`
		* The sender shall wait for the next FF frame.
	* `0x2 - Overflow (OVFLW)`
		* The sender shall abort sending any more CF(s).
		* *Note:* This shall only be sent after the reception of an FF, with `L` larger than the available buffer size.
* The second byte denotes *BS* (i.e., Block Size).
* The third byte denotes `ST_min`.
	* If `0x00` to `0x7F`, it is in `ms`.
	* If `0xF1` to `0xF9`, it maps to the range of `100` to `900` `us`.

![[CAN-TP-Segmented.png|500]]

*Note:* For all case(s) where *CAN* frame length `> L`, padding byte(s) shall be appended.
## References
---
[1] Road Vehicles - Controller Area Network (CAN), ISO 11898-1, 2015