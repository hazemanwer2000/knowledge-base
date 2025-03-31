──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
In an *AUTOSAR* system (e.g., a vehicle), the application software is organized into components.

Modelling of SW-Component(s) is broken down into steps.
* First, port(s) and connection(s) across the different SWC(s) are specified.
* Second, the internal behavior of every SWC is specified, in terms of event(s) and runnable(s).
* Third, an implementation is specified (e.g., C-code implementation of every runnable).

*Note:* Any implementation depends on the Run-Time Environment (RTE) for the handling of event(s), and communication across SWC(s).
### UML
---
#### `SwComponentType`
---
```plantuml
abstract SwComponentType {
	port : PortPrototype (aggr, 0..*)
}
abstract AtomicSwComponentType {
	internalBehavior : SwcInternalBehavior (aggr, 1)
}
class CompositionSwComponentType {
	component : SwComponentPrototype (aggr, 0..*)
	connector : SwConnector (aggr, 0..*)
}
SwComponentType <|-- AtomicSwComponentType
SwComponentType <|-- CompositionSwComponentType
AtomicSwComponentType <|-- ApplicationSwComponentType
AtomicSwComponentType <|-- ComplexDeviceDriverSwComponentType
AtomicSwComponentType <|-- ServiceSwComponentType
```
#### `PortPrototype`
---
```plantuml
abstract PortPrototype {
	interface : PortInterface (ref, 1)
}
abstract AbstractProvidedPortPrototype {
	providedComSpec : PPortComSpec (aggr, 0..*)
}
abstract AbstractRequiredPortPrototype {
	requiredComSpec : RPortComSpec (aggr, 0..*)
}
class PPortPrototype
class RPortPrototype
class PRPortPrototype

PortPrototype <|-- AbstractProvidedPortPrototype
PortPrototype <|-- AbstractRequiredPortPrototype
AbstractProvidedPortPrototype <|-- PPortPrototype
AbstractProvidedPortPrototype <|-- PRPortPrototype
AbstractRequiredPortPrototype <|-- RPortPrototype
AbstractRequiredPortPrototype <|-- PRPortPrototype
```
## References
---
[1] Software Component Template, AUTOSAR Classic Platform, R20-11