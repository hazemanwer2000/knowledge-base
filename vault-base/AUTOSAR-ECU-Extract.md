──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
In an *AUTOSAR* system (e.g., a vehicle), an ECU Extract is an extract of all information relevant to a specific ECU from the System Description.

Information in an ECU extract can be classified into multiple categories:
* **Topology**: The different Communication Cluster(s) the ECU is connected to. 
* **Communication**: The Signal(s), PDU(s) and Frame(s) the ECU transmits and receives.
* **Mapping**: The mapping of data from SWC(s) to Signal(s).
### ECU Extract
---
##### `System`
---
```plantuml
class System <category=ECU_EXTRACT> {
	fibexElement : FibexElement (ref, *)
	mapping : SystemMapping (aggr, *)
}
```
## References
---
[1] ...