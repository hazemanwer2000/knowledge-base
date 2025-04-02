──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
In an *AUTOSAR* system (e.g., a vehicle), an ECU Extract is an extract of all information relevant to a specific ECU from the System Description.

Information in an ECU extract can be classified into multiple categories:
* **Topology**: The different Communication Cluster(s) the ECU is connected to.
* **Communication**: The Signal(s), PDU(s) and Frame(s) the ECU transmits and receives.
* **Software:** The Root `CompositionSwComponentType` of an ECU, aggregating `AtomicSwComponentType`(s) only (i.e., ECU-specific flattened view).
* **Mapping**: The mapping of data from `PortPrototype`(s) of the Root `CompositionSwComponentType` to Signal(s).
### ECU Extract
---
#### `System`
---
```plantuml
class System <category=ECU_EXTRACT> {
	fibexElement : FibexElement (ref, *)
	rootSoftwareComposition : RootSwCompositionPrototype (aggr, 1)
	mapping : SystemMapping (aggr, *)
}
```
### Category: Topology
---
#### `CommunicationCluster`
---
```plantuml
abstract CommunicationCluster <<FibexElement>>
abstract PhysicalChannel {
	commConnector : CommunicationConnector (ref, *)
}
CommunicationCluster o-- PhysicalChannel
```

*Note:* Semantically, every `CommunicationCluster` (e.g., CAN network) is composed of one or more (redundant) `PhysicalChannel`(s).

*Note:* Semantically, every `PhysicalChannel` is composed of many `CommunicationConnector`(s) (i.e., physical or virtual bus interface(s)).
#### `EcuInstance`
---
```plantuml
class EcuInstance <<FibexElement>>
abstract CommunicationController
abstract CommunicationConnector
EcuInstance o-- CommunicationController
EcuInstance o-- CommunicationConnector
CommunicationController <-right- CommunicationConnector
```

*Note:* Semantically, every `EcuInstance` aggregates one or more `CommunicationController`(s) (e.g., CAN controller), each composed of one or more `CommunicationConnector`(s).
## References
---
[1] System Template, AUTOSAR Classic Platform, R20-11
[2] ASAM MCD-2 NET (FIBEX)