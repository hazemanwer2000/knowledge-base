──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*Controller Area Network (CAN)* is a serial, half-duplex, asynchronous, message-oriented and `N:N` (i.e., `Master:Slave`) *L2*-protocol.

It is usually employed in the automotive industry.
### Acronyms
---
* `RTR` - Remote Transmission Request
* `IDE` - Identifier Extension Request
* `FDF` - FD-Format
* `DLC` - Data Length Code
* `SRR` - Substitute Remote Request
* `EOF` - End of Frame
* `ITM` - Intermission-Space
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
	* forces `RTR` bit to dominant state.
* A *Remote* Frame, whose purpose is to request data, from its publisher,
	* omits the Data Field, and,
	* forces `RTR` bit to recessive state.

*Note*: Based on arbitration, a Data *CAN* frame with the same ID is always prioritized over a Remote *CAN* frame.

The `DLC` field specifies the number of bytes in the Data field.

| DLC field | No. of bytes |
| --------- | ------------ |
| `N <= 8`  | `N`          |
| `N > 8`   | `8`          |

After each *CAN* frame, the following field(s) exist:
* `ACK` (Size: 1-bit)
	* *Note:* All *CAN* node(s) shall acknowledge all CRC-valid *CAN* frame(s), by asserting a dominant state.
* `ACK` delimiter (Size: 1-bit)
* `EOF` (Size: 8-bits)
* `ITM` (Size: 3-bits)

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
* signals to the transmitter of the current *CAN* frame to delay the transmission of the next frame (with the same ID), and,
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
* `ITM` (Size: 3-bits)

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
	* While bit monitoring, the **transmitter** reads `ACK` as a recessive state (i.e., unacknowledged by all receivers).
## References
---
[1] Road Vehicles - Controller Area Network (CAN), ISO 11898-1, 2015