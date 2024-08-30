──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
## Content
---
*Local Interconnect Network (LIN)* is a serial, half-duplex, asynchronous and `1:N` (i.e., `Master:Slave`) *L2*-protocol.

Usually employed in the automotive industry, it is specified in [1].
### Concept
---
Each *LIN* node is connected to the *LIN* bus via a single wire. A node may be,
* A `Master` node, with two running tasks (i.e., jobs), a `Master` task and a `Slave` task.
* A `Slave` node, with one running task, a `Slave` task.

![[LIN-Bus-Overview.png|550]]

A frame consists of a header, sent by the `Master` task, and a response, sent by a `Slave` task.

![[LIN-Bus-Header-Response-Diagram.png|650]]
#### Frame Structure
---
Every field within a *LIN* frame, except the *break* field, is transmitted as one or more byte fields.

![[LIN-Bus-Frame-Structure.png|600]]

A byte field consists of,
* *START* (Size: 1-bit, dominant)
* *DATA* (Size: 8-bits)
* *STOP* (Size: 1-bit, recessive)

*Note:* Bits and bytes are sent in Little-Endian form on the *LIN* bus.
##### Frame Header Structure
---
Each frame header consists of,
* A *break* field.
	* It consists of at least 13 dominant bits, followed by a break delimiter, which is at least 1 recessive bit long.
	* ![[LIN-Bus-Break-Field.png|600]]
* A *sync* field.
	* It consists of the value `0x55`.
	* ![[LIN-Bus-Sync-Field.png|600]]
* A *PID* field.
	* It consists of,
		* Frame ID (Size: 6-bits)
			* *Note:* `0x3C-0x3D` Frame ID(s) are reserved for *LIN-TP* (see below).
		* Parity (Size: 2-bits), calculated over the Frame ID.
			* *Note:* Refer to [1] for the equation, to calculate the Parity field.
	* ![[LIN-Bus-PID-Field.png|600]]

Each frame response consists of,
* ...
## References
---
[1] LIN Protocol Specification, Revision 2.2A, LIN Consortium