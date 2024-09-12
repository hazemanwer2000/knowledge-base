──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#Basics|Basics]]
	- [[#Basics#Frame Structure|Frame Structure]]
		- [[#Frame Structure#Frame Header Structure|Frame Header Structure]]
		- [[#Frame Structure#Frame Response Structure|Frame Response Structure]]
	- [[#Basics#Frame Slot Types|Frame Slot Types]]
		- [[#Frame Slot Types#Unconditional Frame Slot|Unconditional Frame Slot]]
		- [[#Frame Slot Types#Event-Triggered Frame Slot|Event-Triggered Frame Slot]]
		- [[#Frame Slot Types#Sporadic Frame Slot|Sporadic Frame Slot]]
	- [[#Basics#Schedule Tables|Schedule Tables]]
	- [[#Basics#Timing Requirements|Timing Requirements]]
- [[#Transport-Layer|Transport-Layer]]
	- [[#Transport-Layer#Timing Requirements|Timing Requirements]]
- [[#LDF File|LDF File]]
- [[#Network Management|Network Management]]
## Content
---
*Local Interconnect Network (LIN)* is a serial, half-duplex, asynchronous and `1:N` (i.e., `Master:Slave`) *L2*-protocol.

Usually employed in the automotive industry, it is specified in [1].
### Basics
---
Each *LIN* node is connected to the *LIN* bus via a single wire. A node may be,
* A `Master` node, with two running tasks (i.e., jobs), a `Master` task and a `Slave` task.
* A `Slave` node, with one running task, a `Slave` task.

![[LIN-Bus-Overview.png|550]]

A frame consists of a header, sent by the `Master` task, and a response, sent by a `Slave` task.

![[LIN-Bus-Header-Response-Diagram.png|650]]

The header specifies the frame to be sent, via the Frame ID (see below), and the `Slave` task acting as its provider transmits the frame response.
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
			* *Note:* Refer to [1] for the equation, to calculate the *Parity* field.
	* ![[LIN-Bus-PID-Field.png|600]]
##### Frame Response Structure
---
Each frame response consists of,
* A *Data* field (Size: 1-to-8-bytes).
* A *Checksum* field (Size: 1-byte).
	* *Note:* Refer to [1] for the equation, to calculate the *Checksum* field.
#### Frame Slot Types
---
##### Unconditional Frame Slot
---
Within an unconditional frame slot, a specific frame (i.e., Frame ID) shall always be sent.
##### Event-Triggered Frame Slot
---
An event-triggered frame slot associates with one or more frames, which must,
* Have equal length.
* Reserve the first byte of their response for the *PID* field.
* Be provided by different `Slave` task(s).
* Shall not be allocated an unconditional frame slot, within the same schedule table.

A unique Frame ID is assigned to the event-triggered frame slot. Upon reception of, every slave provider checks if the data of the associated frame has been altered. If true, it transmits a frame response.

In case a collision is detected by the `Master` task (e.g., invalid *Checksum* field),
* `Master` task switches temporarily to a collision-resolving schedule table.
* Within, at least, associated frames are transmitted in unconditional frame slot(s).
##### Sporadic Frame Slot
---
A sporadic frame slot associates with one or more frames, which must,
* Be provided by the `Slave` task of the `Master` node.

Within a sporadic frame slot, all associated frames are checked, if transmission is warranted (i.e., data altered).
* If no frames shall be transmitted, the frame slot if silent (i.e., no header or response).
* If one frame shall be transmitted, the frame is transmitted within the slot.
* If more than one frame shall be transmitted, highest-priority frame is transmitted within the slot.
	* *Note:* Lower priority frames shall have a chance for transmission, on the next occurrence of this frame slot.
#### Schedule Tables
---
A schedule table consists of a number of consecutive frame slots.

If a schedule table switch is requested (e.g., by the application-layer), it shall occur at the end of the current frame slot.
#### Timing Requirements
---
Timing requirements include,
* `T_Frame_Nominal = T_Header_Nominal + T_Response_Nominal`, where,
	* `T_Header_Nominal = 34 * T_bit`.
	* `T_Response_Nominal = 10 * (N + 1) * T_bit`.
* `T_Frame_Maximum` is `1.4x` `T_Frame_Nominal`.
* `T_Frame_Slot` is,
	* an integer multiple of `T_base`, the time base, and,
	* `T_Frame_Slot > (Jitter + T_Frame_Maximum)`.

![[LIN-Bus-Frame-Slot.png|600]]
### Transport-Layer
---
*LIN-TP* is defined to use Frame ID(s),
* `0x3C`, for transmission from `Master` node to `Slave` node, usually requests.
	* *Note:* It is usually called *Master-Request Frame (MRF)*.
* `0x3D`, for transmission from `Slave` node to `Master` node, usually responses.
	* *Note:* It is usually called *Slave-Response Frame (SRF)*.

*Note:* Both frames have a fixed length of 8 bytes. Unused bytes are set to `0xFF`.

To transmit a request,
* If its length is less than or equal to six bytes,
	* *SF* (Single-Frame) is transmitted.
* Else,
	* *FF* (First-Frame) and *CF* (Consecutive-Frame) are transmitted.

The following is the format of the different *TP*-Frame types.

![[LIN-TP-Frame-Structures.PNG|600]]

Fields include,
* *NAD* (Node Address), a unique identifier of every `Slave` node addressable via *LIN-TP*.
* *PCI* (Protocol Control Information), includes control-flow information, dependent on the *TP*-Frame type.
	* ![[LIN-TP-PCI-Format.png|450]]
	* *Note:* For *FF* frames, the *length* field is 12-bits long.
	* *Note:* For *CF* frames, the *counter* field begins with 1, wraps to 0.
#### Timing Requirements
---
Timing requirements include,
* `ST_min`, the minimum time-delay a `Slave` node requires, between an *FF* and a *CF* frame, or *CF* frame(s).
### LDF File
---
An *LDF (LIN Description File)* completely describes a *LIN* cluster.

```
LIN_description_file;
LIN_protocol_version = <version_number>;
LIN_language_version = <version_number>;
LIN_speed = <floating_value> kbps;
Channel_name = <symbolic_name>;

Nodes {
	Master: <symbolic_name>, <time_base> ms, <jitter> ms;
	Slave: [<symbolic_name>];
}

Node_attributes {
	[<node_ref> {
		configured_NAD = <hex_value>;
		ST_min = <floating_value> ms;
	}]
}

Frames {
	[<symbolic_name>: <frame_id>, <provider_node_ref>, <length_in_bytes> {
		...
	}]
}

Sporadic_frames {
	[<symbolic_name>: [<frame_ref>];]
}

Event_triggered_frames {
	[<symbolic_name>:
		<collision_resolving_schedule_table_ref>,
		<frame_id>,
		[<frame_ref>]
	;]
}

Schedule_tables {
	[<symbolic_name> {
		[<frame_ref> delay <floating_value> ms;]
	}]
}
```

*Note:* Schedule table(s) may reference language-built-in frame(s). Refer to [1] for further information.
### Network Management
---
The following is the state diagram of any `Slave` node.

![[LIN-Bus-NM-State-Diagram.png|550]]

A Go-To-Sleep request is transmitted by the `Master` node as an *MRF*, and is as shown below.

![[LIN-Bus-Go-To-Sleep-Request.png|600]]

*Note:* *NAD* with value zero is reserved for network management purposes.

A bus wake-up signal may be issued, by any node, by forcing the *LIN* bus to the dominant state, for `250-us` to `5-ms`, after which the signal is considered valid.

If the `Master` node does not transmit a *break* field for `150-ms` to `250-ms` from when the bus wake-up signal was validated, the node issuing the wake-up signal shall re-transmit a new wake-up signal.

![[LIN-Bus-Wake-Up-Retransmit.png|700]]

After three transmissions of wake-up signal(s), the issuing node shall wait a minimum of `1.5s`, before retrying.

![[LIN-Bus-Wake-Up-Retransmit-Wait.png|675]]
## References
---
[1] LIN Protocol Specification, Revision 2.2A, LIN Consortium