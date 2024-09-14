──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*FlexRay* is a serial, half-duplex, asynchronous, message-oriented and *TDMA (Time-Division, Multiple-Access)* *L2*-protocol.

It is usually employed in the automotive industry, specified in [1].
### Definitions
---
- **Macro-Tick (MT)** - Time-unit within a cluster.
### Constants
---
Per *FlexRay* cluster, the network designer selects the value of a number of constant(s).

* `CycleCount` - Number of recurring cycle(s).
* `SlotCountMaxPerCycle` - Maximum number of slot(s) per cycle.
* For the static segment,
	* `MacroTickCountPerStaticSlot` - Number of MT(s) per static slot.
	* `StaticSlotCountPerCycle` - Number of static slot(s) per cycle.
* For the dynamic segment,
	* `MacroTickCountPerMiniSlot` - Number of MT(s) per mini-slot.
	* `MiniSlotCountPerCycle` - Number of mini-slot(s) per cycle.
* `MacroTickCountPerSymbolWindow` - Number of MT(s) per *Symbol Window (SW)*.
* `MacroTickCountPerNetworkIdleTime` - Number of MT(s) per *Network Idle Time (NID)*.
* `NetworkManagementVectorLength` - Number of bit(s) in a Network Management Vector.
### The Cycle
---
Communication in *FlexRay* occurs in recurring cycles.
* Every cycle has an ID, ranging from `0` to `(CycleCount - 1)`.
* Cycle `0` occurs, then, cycle `1`, etc, up until cycle `(CycleCount - 1)`, before wrapping to cycle `0` again.

The structure of a cycle is as shown below.

![[FlexRay-Cycle-Structure.png|800]]

Within every cycle, within the static or dynamic segment(s),
* every (static or dynamic) slot has an ID, starting with `1`, incrementing, up to possibly `SlotCountMaxPerCycle`.

Every unique `(Cycle ID, Slot ID)` tuple identifies a specific frame for (possible) transmission, by a single-node.
#### Static Segment
---
Within the static segment, `StaticSlotCountPerCycle` consecutive static slot(s) occur, each lasting `MacroTickCountPerStaticSlot` MT(s).

*Note:* The number of MT(s) per static slot, `MacroTickCountPerStaticSlot`, must be selected based upon the largest frame scheduled for transmission within a static slot.

*Note:* A frame must be transmitted within a static slot, possibly as a null-frame (see below).
#### Dynamic Segment
---
Within the dynamic segment, `MiniSlotCountPerCycle` consecutive mini-slot(s) occur, each lasting `MacroTickCountPerMiniSlot` MT(s).

A dynamic slot is of variable-size, according to the following rule(s):
* If nothing is transmitted within a dynamic slot, the slot has the size of a single mini-slot.
* If a frame is transmitted within a dynamic slot, the slot has the size of the frame, ceiled up-to an integer multiple of mini-slot(s).
#### Symbol Window (SW)
---
The Symbol Window (SW) is out-of-scope of this document.
#### Network Idle Time (NIT)
---
The Network Idle Time (NIT) is out-of-scope of this document.
### Frame Format
---
The following is the format of a *FlexRay* frame.

![[FlexRay-Frame-Format.png|900]]

If the Payload Preamble Indicator bit is set,
* For the static segment,
	* It asserts the presence of a Network Management Vector, of size `NetworkManagementVectorLength` bits, at the beginning of the payload.
* For the dynamic segment,
	* It asserts the present of a 2-byte Message ID, at the beginning of the payload.

If the Null Frame Indicator bit is reset,
* It asserts that this is a null-frame (i.e., a frame with un-useful payload).

The Start-up and Sync Frame Indicator bit(s) are out-of-scope of this document.

*Note:* In *FlexRay*, bits within a Data byte are transmitted MSB-to-LSB.
### Time Synchronization
---
Time within a cluster is represented by the `(Cycle ID, MT Number)` tuple.

Time synchronization within a cluster is out-of-scope of this document.
## References
---
[1] Road Vehicles - FlexRay, ISO 17458-1, 2013
[2] FlexRay and Its Applications, Dominique Paret, 2012