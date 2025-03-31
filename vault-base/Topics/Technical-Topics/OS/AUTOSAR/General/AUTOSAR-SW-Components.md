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
### Meta-model
---
#### `SwComponentType`
---
```plantuml
abstract SwComponentType {
	port : PortPrototype (aggr, *)
}
abstract AtomicSwComponentType {
	internalBehavior : SwcInternalBehavior (aggr, 1)
}
class CompositionSwComponentType {
	component : SwComponentPrototype (aggr, *)
	connector : SwConnector (aggr, *)
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
	providedComSpec : PPortComSpec (aggr, *)
}
abstract AbstractRequiredPortPrototype {
	requiredComSpec : RPortComSpec (aggr, *)
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
#### `PortInterface`
---
```plantuml
abstract PortInterface
abstract DataInterface
class SenderReceiverInterface {
	dataElement : VariableDataPrototype (aggr, *)
}
class ClientServerInterface {
	operation : ClientServerOperation (aggr, *)
}
class ClientServerOperation {
	argument : ArgumentDataPrototype (aggr, *)
}
class ModeSwitchInterface {
	modeGroup : ModeDeclarationGroupPrototype (aggr, 1)
}
class TriggerInterface {
	trigger : Trigger (aggr, *)
}
PortInterface <|-- ClientServerInterface
PortInterface <|-- ModeSwitchInterface
PortInterface <|-- TriggerInterface
PortInterface <|-- DataInterface
DataInterface <|-- SenderReceiverInterface
```
##### `DataPrototype`
---
```plantuml
abstract DataPrototype {
	type : DataType (ref, 1)
}
class VariableDataPrototype {
	initValue : ValueSpecification (aggr, 1)
}
class ArgumentDataPrototype {
	direction : ArgumentDirectionEnum (aggr, 1)
}
enum ArgumentDirectionEnum {
	in
	out
	inout
}
abstract ValueSpecification
DataPrototype <|-- VariableDataPrototype
DataPrototype <|-- ArgumentDataPrototype
```
##### `DataType`
---
```plantuml
abstract DataType
abstract ApplicationDataType
abstract ApplicationCompositeDataType
DataType <|-- ImplementationDataType
DataType <|-- ApplicationDataType
ApplicationDataType <|-- ApplicationPrimitiveDataType
ApplicationDataType <|-- ApplicationCompositeDataType
ApplicationCompositeDataType <|-- ApplicationRecordDataType
ApplicationCompositeDataType <|-- ApplicationArrayDataType
```
##### `ModeDeclarationGroupPrototype`
---
```plantuml
class ModeDeclaractionGroupPrototype {
	type : ModeDeclarationGroup (ref, 1)
}
```
##### `ModeDeclarationGroup`
---

## References
---
[1] Software Component Template, AUTOSAR Classic Platform, R20-11