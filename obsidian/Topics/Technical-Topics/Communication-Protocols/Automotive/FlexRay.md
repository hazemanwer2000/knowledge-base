──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*FlexRay* is a serial, half-duplex, asynchronous, message-oriented and *TDMA (Time-Division, Multiple-Access)* *L2*-protocol.

It is usually employed in the automotive industry, specified in [1].
### Constants
---
Per *FlexRay* cluster, the network designer selects the value of a number of constant(s).

* `CycleCount` - Number of recurring cycle(s).
* `SlotCountMaxPerCycle` - Maximum number of slot(s) per cycle.
* For the static segment,
	* `MacroTickCountPerStaticSlot` - Number of macro-tick(s) per static slot.
	* `StaticSlotCountPerCycle` - Number of static slot(s) per cycle.
* For the dynamic segment,
	* `MacroTickCountPerMiniSlot` - Number of macro-tick(s) per mini-slot.
	* `MiniSlotCountPerCycle` - Number of mini-slot(s) per cycle.
* `MacroTickCountPerSymbolWindow` - Number of macro-tick(s) per *Symbol Window (SW)*.
* `MacroTickCountPerNetworkIdleTime` - Number of macro-tick(s) per *Network Idle Time (NID)*.
### Basics
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
Within the static segment, `StaticSlotCountPerCycle` consecutive static slot(s) occur, each lasting `MacroTickCountPerStaticSlot` macro-tick(s).

*Note:* The number of macro-tick(s) per static slot, `MacroTickCountPerStaticSlot`, must be selected based upon the largest frame scheduled for transmission within a static slot.

*Note:* A frame must be transmitted within a static slot, possibly as a null-frame (see below).
#### Dynamic Segment
---
Within the dynamic segment, `MiniSlotCountPerCycle` consecutive mini-slot(s) occur, each lasting `MacroTickCountPerMiniSlot` macro-tick(s).

A dynamic slot is of variable-size, according to the following rule(s):
* If nothing is transmitted within a dynamic slot, the slot has the size of a single mini-slot.
* If a frame is transmitted within a dynamic slot, the slot has the size of the frame, ceiled up-to an integer multiple of mini-slot(s).
#### Symbol Window (SW)
---
Refer to [1] for a 
## References
---
[1] Road Vehicles - FlexRay, ISO 17458-1, 2013
[2] FlexRay and Its Applications, Dominique Paret, 2012