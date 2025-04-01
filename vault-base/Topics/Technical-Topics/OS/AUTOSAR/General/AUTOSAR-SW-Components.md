──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#SWC Type(s)|SWC Type(s)]]
	- [[#SWC Type(s)#`SwComponentType`|`SwComponentType`]]
- [[#Step: Port(s) and Connector(s)|Step: Port(s) and Connector(s)]]
	- [[#Step: Port(s) and Connector(s)#`PortPrototype`|`PortPrototype`]]
		- [[#`PortPrototype`#`PortInterface`|`PortInterface`]]
			- [[#`PortInterface`#`DataPrototype`|`DataPrototype`]]
			- [[#`PortInterface`#`DataType`|`DataType`]]
			- [[#`PortInterface`#`ModeDeclarationGroup`|`ModeDeclarationGroup`]]
		- [[#`PortPrototype`#`PPortComSpec`|`PPortComSpec`]]
		- [[#`PortPrototype`#`RPortComSpec`|`RPortComSpec`]]
	- [[#Step: Port(s) and Connector(s)#`SwConnector`|`SwConnector`]]
- [[#Step: Internal Behavior|Step: Internal Behavior]]
	- [[#Step: Internal Behavior#`SwcInternalBehavior`|`SwcInternalBehavior`]]
		- [[#`SwcInternalBehavior`#`DataTypeMappingSet`|`DataTypeMappingSet`]]
		- [[#`SwcInternalBehavior`#`RTEEvent`|`RTEEvent`]]
		- [[#`SwcInternalBehavior`#`RunnableEntity`|`RunnableEntity`]]
- [[#Step: Implementation|Step: Implementation]]
	- [[#Step: Implementation#`SwcImplementation`|`SwcImplementation`]]
## Content
---
In an *AUTOSAR* system (e.g., a vehicle), the application software is organized into components.

Modelling of SW-Component(s) is broken down into steps.
1. Port(s) and Connector(s) across the different SWC(s) are specified.
2. Internal Behavior of every SWC is specified, in terms of Event(s) and Runnable(s).
3. An Implementation is specified (e.g., C-code implementation of every runnable).

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

```plantuml
class ClientServerOperation {
	argument : ArgumentDataPrototype (aggr, *)
}
class Trigger {
	swImplPolicy : SwImplPolicyEnum (attr, 1)
}
enum SwImplPolicyEnum {
	standard
	queued
}
```
###### `DataPrototype`
---
```plantuml
abstract DataPrototype {
	type : DataType (ref, 1)
}
class VariableDataPrototype {
	initValue : ValueSpecification (aggr, ?)
}
class ArgumentDataPrototype {
	direction : ArgumentDirectionEnum (aggr, 1)
}
class SwDataDefProps {
	swImplPolicy : SwImplPolicyEnum (attr, 1)
	
}
enum SwImplPolicyEnum {
	standard
	queued
}
enum ArgumentDirectionEnum {
	in
	out
	inout
}
DataPrototype <|-- VariableDataPrototype
DataPrototype <|-- ArgumentDataPrototype
VariableDataPrototype o-- SwDataDefProps
```

```plantuml
abstract ValueSpecification
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

*Note:* It is not allowed to connect two `PortProtoype`(s) by more than one `SwConnector`. This implies that any connection between two `PRPortPrototype`(s) is bi-directional.
### Step: Internal Behavior
---
#### `SwcInternalBehavior`
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
	startOnEvent : RunnableEntity (ref, ?)
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
class AsynchronousServerCallReturnsEvent {
	eventSource : AsynchronousServerCallResultPoint (ref, 1)
}
class SwcModeSwitchEvent {
	activation : ModeActivationKind (attr, 1)
	mode : ModeDeclaration (ref, 1..2)
}
class ExternalTriggerOccurredEvent {
	trigger : Trigger (ref, 1)
}
class InternalTriggerOccurredEvent {
	eventSource : InternalTriggeringPoint (ref, 1)
}
enum ModeActivationKind {
	onEntry
	onExit
	onTransition
}
AbstractEvent <|-- RTEEvent
RTEEvent <|-right- TimingEvent
RTEEvent <|-right- InitEvent
RTEEvent <|-left- DataReceivedEvent
RTEEvent <|-- OperationInvokedEvent
RTEEvent <|-- AsynchronousServerCallReturnsEvent
RTEEvent <|-- SwcModeSwitchEvent
RTEEvent <|-- ExternalTriggerOccurredEvent
RTEEvent <|-- InternalTriggerOccurredEvent
```
##### `RunnableEntity`
---
```plantuml
abstract ExecutableEntity {
	canEnterExclusiveArea : ExclusiveArea (ref, *)
	runsInsideExclusiveArea : ExclusiveArea (ref, *)
}
class RunnableEntity {
	canBeInvokedConcurrently : Boolean (attr, 1)
	symbol : CIdentifier (attr, 1)
	dataReadAccess : VariableAccess (aggr, *)
	dataReceivePointByArgument : VariableAccess (aggr, *)
	dataReceivePointByValue : VariableAccess (aggr, *)
	dataWriteAccess : VariableAccess (aggr, *)
	dataSendPoint : VariableAccess (aggr, *)
	serverCallPoint : ServerCallPoint (aggr, *)
	asynchronousServerCallResultPoint : AsynchronousServerCallResultPoint (aggr, *)
	externalTriggeringPoint : ExternalTriggeringPoint (aggr, *)
	internalTriggeringPoint : InternalTriggeringPoint (aggr, *)
	modeAccessPoint : ModeAccessPoint (aggr, *)
	modeSwitchPoint : ModeSwitchPoint (aggr, *)
}
ExecutableEntity <|-- RunnableEntity
```

```plantuml
abstract ServerCallPoint {
	operation : ClientServerOperation (ref, 1)
	timeout : TimeoutValue (attr, 1)
}
ServerCallPoint <|-- SynchronousServerCallPoint
ServerCallPoint <|-- AsynchronousServerCallPoint
```

```plantuml
class AsynchronousServerCallResultPoint {
	asynchronousServerCallPoint : AsynchronousServerCallPoint (ref, 1)
}
```

*Note:* A `<..>Access` implies "implicit" access to a `VariableDataPrototype`. This means reading yields the last value set before runnable execution, and writing takes effect after a runnable terminates. This is only applicable for non-queued communication.

*Note:* An `AsynchronousServerCallResultPoint` enables a `RunnableEntity` to query the result of a previous invocation of a `ClientServerOperation` via an `AsynchronousServerCallPoint`. If unspecified, the result is inaccessible. If an `AsynchronousServerCallReturnsEvent` is defined, referencing the `AsynchronousServerCallResultPoint`, the event is set upon completion of the `ClientServerOperation`.

*Note:* An `InternalTriggeringPoint` enables the triggering of a `RunnableEntity` by another, within the same `AtomicSwComponentType`. Hence, it does not reference a `Trigger` from a `PortPrototype`, but is rather stand-alone. This is consistent with the fact that an `InternalTriggerOccurredEvent` references an `InternalTriggeringPoint`.

*Note:* A `RunnableEntity` with only `<..>Access` is classified as category 1A, and category 1B otherwise.
### Step: Implementation
---
#### `SwcImplementation`
---
```plantuml
abstract Implementation
class SwcImplementation {
	behavior : SwcInternalBehavior (ref, 1)
}
Implementation <|-- SwcImplementation
```
## References
---
[1] Software Component Template, AUTOSAR Classic Platform, R20-11