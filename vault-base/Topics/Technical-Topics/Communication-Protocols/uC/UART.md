──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#Physical Interface|Physical Interface]]
- [[#Protocol Parameter(s)|Protocol Parameter(s)]]
- [[#Frame Structure|Frame Structure]]
## Content
---
*Universal Asynchronous Receiver/Transmitter (UART)* is a serial, full-duplex, and asynchronous *L2*-protocol.

Usually supported in micro-controller(s), it is a de-facto standard, that is implementation-specific.
### Physical Interface
---
Usually, the following wire-connection(s) (as shown below) are required between two *UART* modules.
![[UART-Physical-Interface.jpg|300]]
### Protocol Parameter(s)
---
Configurable protocol parameter(s), that both *UART* modules need to agree upon before-hand, include,
* *Baud Rate* (i.e., transmission speed), usually in *bps*.
* No. of *STOP* bits, either *1* or *2*.
* No. of *DATA* bits, usually *8*.
* *Parity* bit, whether even, odd, or none at all.
### Frame Structure
---
While idle, the transmitter holds the line (i.e, wire) high.

A *UART* frame consists of,
* *START* (Size: 1-bit), which denotes the start of a *UART* frame.
* *DATA*, which contains the payload of a *UART* frame.
* *PARITY* (Optional).
* *STOP*, which denotes the end of a *UART* frame.

![[UART-Frame-Structure.png|500]]