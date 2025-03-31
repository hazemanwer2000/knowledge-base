──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#SWC Type(s)|SWC Type(s)]]
	- [[#SWC Type(s)#`SwComponentType`|`SwComponentType`]]
		- [[#SWC Type(s)#`SwComponentPrototype`|`SwComponentPrototype`]]
- [[#Port(s) and Connector(s)|Port(s) and Connector(s)]]
	- [[#Port(s) and Connector(s)#`PortPrototype`|`PortPrototype`]]
		- [[#`PortPrototype`#`PortInterface`|`PortInterface`]]
			- [[#`PortInterface`#`DataPrototype`|`DataPrototype`]]
			- [[#`PortInterface`#`DataType`|`DataType`]]
			- [[#`PortInterface`#`ModeDeclarationGroupPrototype`|`ModeDeclarationGroupPrototype`]]
			- [[#`PortInterface`#`ModeDeclarationGroup`|`ModeDeclarationGroup`]]
		- [[#`PortPrototype`#`PPortComSpec`|`PPortComSpec`]]
		- [[#`PortPrototype`#`RPortComSpec`|`RPortComSpec`]]
- 
## Content
---
In an *AUTOSAR* system (e.g., a vehicle), the application software is organized into components.

Modelling of SW-Component(s) is broken down into steps.
* First, port(s) and connector(s) across the different SWC(s) are specified.
* Second, the internal behavior of every SWC is specified, in terms of event(s) and runnable(s).
* Third, an implementation is specified (e.g., C-code implementation of every runnable).

*Note:* Any implementation of a SWC depends on the Run-Time Environment (RTE) for the handling of event(s), and communication across SWC(s).
### SWC Type(s)
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
##### `SwComponentPrototype`
---
```plantuml
class SwComponentPrototype {
	type : SwComponentType (ref, 1)
}
```
### Step: Port(s) and Connector(s)
---
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
##### `PortInterface`
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
class Trigger
PortInterface <|-- ClientServerInterface
PortInterface <|-- ModeSwitchInterface
PortInterface <|-- TriggerInterface
PortInterface <|-- DataInterface
DataInterface <|-- SenderReceiverInterface
```
###### `DataPrototype`
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
###### `DataType`
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
###### `ModeDeclarationGroupPrototype`
---
```plantuml
class ModeDeclaractionGroupPrototype {
	type : ModeDeclarationGroup (ref, 1)
}
```
###### `ModeDeclarationGroup`
---
```plantuml
class ModeDeclarationGroup {
	initialMode : ModeDeclaration (ref, 1)
	modeDeclaration : ModeDeclaration (aggr, *)
	modeTransition : ModeTransition (aggr, *)
}
class ModeTransition {
	enteredMode : ModeDeclaration (aggr, 1)
	exitedMode : ModeDeclaration (aggr, 1)
}
```
##### `PPortComSpec`
---
```plantuml
abstract PPortComSpec
abstract SenderComSpec {
	dataElement : DataPrototype (ref, 1)
}
class ServerComSpec {
	operation : ClientServerOperation (ref, 1)
	queueLength : Integer (attr, 1)
}
class ModeSwitchSenderComSpec {
	modeGroup : ModeDeclarationGroupPrototype (ref, 1)
}
PPortComSpec <|-- SenderComSpec
SenderComSpec <|-- NonqueuedSenderComSpec
SenderComSpec <|-- QueuedSenderComSpec
PPortComSpec <|-- ServerComSpec
PPortComSpec <|-- ModeSwitchSenderComSpec
```
##### `RPortComSpec`
---
```plantuml
abstract RPortComSpec
abstract ReceiverComSpec {
	dataElement : DataPrototype (ref, 1)
}
class ClientComSpec {
	operation : ClientServerOperation (ref, 1)
}
class ModeSwitchReceiverComSpec {
	modeGroup : ModeDeclarationGroupPrototype (ref, 1)
}
class QueuedReceiverComSpec {
	queueLength : Integer (attr, 1)
}
RPortComSpec <|-- ReceiverComSpec
ReceiverComSpec <|-- NonqueuedReceiverComSpec
ReceiverComSpec <|-- QueuedReceiverComSpec
RPortComSpec <|-- ClientComSpec
RPortComSpec <|-- ModeSwitchReceiverComSpec
```
#### `SwConnector`
---
```plantuml
abstract SwConnector
class AssemblySwConnector {
	provider : AbstractProvidedPortPrototype (ref, 1)
	requester : AbstractRequiredPortPrototype (ref, 1)
}
class DelegationSwConnector {
	innerPort : PortPrototype (ref, 1)
	outerPort : PortPrototype (ref, 1)
}
class PassThroughSwConnector {
	providedOuterPort : AbstractProvidedPortPrototype (ref, 1)
	requiredOuterPort : AbstractRequiredPortPrototype (ref, 1)
}
SwConnector <|-- AssemblySwConnector
SwConnector <|-- DelegationSwConnector
SwConnector <|-- PassThroughSwConnector
```
### Step: Internal Behavior
---
#### `InternalBehavior`
---
```plantuml
abstract InternalBehavior {
	dataTypeMapping : DataTypeMappingSet (ref, *)
	exclusiveArea : ExclusiveArea (aggr, *)
}
class SwcInternalBehavior {
	event : RTEEvent (aggr, *)
	runnable : RunnableEntity (aggr, *)
}
class ExclusiveArea
InternalBehavior <|-- SwcInternalBehavior
```
##### `DataTypeMappingSet`
---
```plantuml
class DataTypeMappingSet {
	dataTypeMap : DataTypeMap (aggr, *)
	modeRequestTypeMap : ModeRequestTypeMap (aggr, *)
}
```
```plantuml
class DataTypeMap {
	applicationDataType : ApplicationDataType (ref, 1)
	implementationDataType : ImplementationDataType (ref, 1)
}
class ModeRequestTypeMap {
	modeDeclarationGroup : ModeDeclarationGroup (ref, 1)
	implementationDataType : ImplementationDataType (ref, 1)
}
```
##### `RTEEvent`
---
```plantuml
abstract AbstractEvent
abstract RTEEvent {
	startOnEvent : RunnableEntity (ref, 1)
}
class TimingEvent {
	period : TimeValue (attr, 1)
}
class InitEvent
class DataReceivedEvent {
	data : VariableDataPrototype (ref, 1)
}
class OperationInvokedEvent {
	operation : ClientServerOperation (ref, 1)
}
class SwcModeSwitchEvent {
	activation : ModeActivationKind (attr, 1)
	mode : ModeDeclaration (ref, 1..2)
}
enum ModeActivationKind {
	onEntry
	onExit
	onTransition
}
AbstractEvent <|-- RTEEvent
RTEEvent <|-- TimingEvent
RTEEvent <|-- InitEvent
RTEEvent <|-- DataReceivedEvent
RTEEvent <|-- OperationInvokedEvent
RTEEvent <|-- SwcModeSwitchEvent
```
## References
---
[1] Software Component Template, AUTOSAR Classic Platform, R20-11