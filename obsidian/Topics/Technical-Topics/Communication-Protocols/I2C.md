──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#Physical Interface|Physical Interface]]
- [[#Communication|Communication]]
	- [[#Communication#Transaction(s)|Transaction(s)]]
		- [[#Transaction(s)#Data Format|Data Format]]
	- [[#Communication#Additional Feature(s)|Additional Feature(s)]]
		- [[#Additional Feature(s)#Arbitration|Arbitration]]
## Content
---
*Inter-Integrated Circuit (I2C)* is a serial, half-duplex, synchronous and `N:N` (i.e., `Master:Slave`) *L2*-protocol.

Usually supported in micro-controller(s), it is specified in [1].
### Physical Interface
---
Usually, the following wire-connection(s) (also, shown below) are required to connect a node to the *I2C* bus.
* *SDA* (*Serial-Data*)
* *SCL* (*Serial-Clock*)

![[I2C-Physical-Interface.png|600]]

*Note:* Pull-up resistor(s) is usually connected to the *SDA* and *SCL* line(s).
### Communication
---
While idle, the *SCL* and *SDA* line(s) are held high.
#### Transaction(s)
---
For a `Master` to initiate a transaction on the *I2C* bus, it generates a *START* condition, which is a *High-Low* transition on the *SDA* line while the *SCL* line is high. 

To terminate a transaction, it generates a *STOP* condition, which is a *Low-High* transition on the *SDA* line while the *SCL* line is high.

![[I2C-START-STOP-Conditions.png|600]]

In-between both condition(s), bits are streamed on the *SDA* line, with every *SCK* cycle, as follows,
* While the *SCL* line is low, the *SDA* line may be altered.
* Otherwise, the *SDA* must remain unchanged.

![[I2C-Data-Validity.png|500]]
##### Data Format
---
Data is transmitted on the *I2C* bus in bytes (MSB-to-LSB).
* `Master` may be the transmitter, or receiver of a byte.
* Each byte must be followed by an acknowledgement-bit, sent by the receiver of the byte.

The first byte is always transmitted by the `Master`. It consists of,
* `Slave` Address (Size: 7-bits)
	* *Note:* `0b1111XXX` and `0b0000XXX` address(es) are reserved. ``
* $R$/$\overline{W}$ (Size: 1-bit)

If acknowledged by a `Slave` (i.e., with a matching address), depending on the $R$/$\overline{W}$ bit, the `Master` is the transmitter, or receiver, of all subsequent byte(s) inside this transaction.

![[I2C-Complete-Transaction.png|650]]
#### Additional Feature(s)
---
##### Arbitration
---
If more than one `Master` initiates a transaction, at the same time, arbitration takes place.
* With every bit streamed, while the *SCL* is high, each `Master` checks if the *SDA* line matches what it has asserted previously (i.e., while the *SCL* line is low).
* If not matching, this `Master` has lost the arbitration.

To not give up control of the bus, before terminating a transaction via a *STOP* condition, a `Master` may generate a *REPEAT-START* condition (as shown below).

![[I2C-REPEAT-START-Condition.png|400]]

Refer to [1] for undefined scenario(s) that may occur during arbitration.
## References
---
[1] UM10204, I2C Bus Specification, NXP Semiconductors