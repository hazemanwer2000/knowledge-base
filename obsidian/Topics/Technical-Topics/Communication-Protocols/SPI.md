──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#Physical Interface|Physical Interface]]
- [[#Protocol Parameter(s)|Protocol Parameter(s)]]
- [[#Frame Structure|Frame Structure]]
- [[#Physical Implementation|Physical Implementation]]
## Content
---
*Serial Peripheral Interface (SPI)* is a serial, full-duplex, synchronous and `1:N` (i.e., `Master:Slave`) *L2*-protocol.

Usually supported in embedded target(s), it is a de-facto standard, that is implementation-specific.
### Physical Interface
---
Usually, the following signal(s) (also, shown below) are required between a `Master` and a `Slave`.
* *MOSI* (*Master-Output-Slave-Input*)
* *MISO* (*Master-Input-Slave-Output*)
* *SS* (*Slave-Select*)
* *CLK*
* *GND*

*Note:* Sometimes, *MOSI* and *MISO* signal(s) are replaced by *SDO/SDI* (*Serial Data Output/Input*) signal(s).

![[SPI-Physical-Interface.png]]
### Protocol Parameter(s)
---
Configurable protocol parameter(s), that *SPI* modules need to agree upon before-hand, include,
* *Baud Rate* (i.e., transmission speed).
* *Clock Polarity*, which specifies whether the base-value of *CLK* is low or high.
* *Clock Phase*, which specifies whether sampling occurs on the leading or trailing edge of *CLK*.
### Frame Structure
---
While idle, the `Master` holds *CLK* at its base-value. To communicate with a `Slave`,

* *SS* is driven low for the selected `Slave` only.
* *N* (e.g., 8) *CLK* cycles are generated.
	* *Note:* With each *CLK* cycle, `Master` transmits and receives 1 bit.
* *SS* is driven high again.

![[SPI-Frame-Structure.jpg|600]]

*Note:* When *SS* is driven high for a `Slave`, its *MISO* physical-pin goes into high-impedance state.
### Physical Implementation
---
Usually, *SPI* module circuitry is as shown below.

![[SPI-Module-Circuitry.jpg|600]]