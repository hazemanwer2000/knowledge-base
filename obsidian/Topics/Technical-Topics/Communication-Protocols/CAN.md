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
#### ...
## References
---
[1] Road Vehicles - Controller Area Network (CAN), ISO 11898-1, 2015