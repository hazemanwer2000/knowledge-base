──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#Step: Interface(s)|Step: Interface(s)]]
	- [[#Step: Interface(s)#`BswModuleDescription`|`BswModuleDescription`]]
- [[#Step: Internal Behavior|Step: Internal Behavior]]
	- [[#Step: Internal Behavior#`BswInternalBehavior`|`BswInternalBehavior`]]
		- [[#`BswInternalBehavior`#`BswModuleEntity`|`BswModuleEntity`]]
		- [[#`BswInternalBehavior`#`BswEvent`|`BswEvent`]]
- [[#Step: Implementation|Step: Implementation]]
	- [[#Step: Implementation#`BswImplementation`|`BswImplementation`]]
## Content
---
In an *AUTOSAR* system (e.g., a vehicle), the basic software is organized into modules.

Modelling of BSW module(s) is broken down into steps.
1. Interface(s) across the different BSW module(s) are specified.
2. Internal Behavior of every BSW module is specified, in terms of Event(s) and Executable Entity(s).
3. An Implementation is specified (e.g., C-code implementation of every executable entity).

*Note:* Any implementation of a BSW module depends on the BSW Scheduler (SchM) for the handling of event(s), and communication across BSW module(s) (e.g., mode-notification(s)).
### Step: Interface(s)
---
#### `BswModuleDescription`
---
```plantuml
class BswModuleDescription {
	bswModuleDependency : BswModuleDependency (aggr, *)
	expectedEntry : BswModuleEntry (ref, *)
	implementedEntry : BswModuleEntry (ref, *)
	internalBehavior : BswInternalBehavior (aggr, 1)
	providedModeGroup : ModeDeclarationGroupPrototype (aggr, *)
	requiredModeGroup : ModeDeclarationGroupPrototype (aggr, *)
}
```

```plantuml
class BswModuleDependency {
	targetModuleRef : BswModuleDescription (ref, 1)
}
```

```plantuml
class BswModuleEntry {
	callType : BswCallType (attr, 1)
	executionContext : BswExecutionContext (attr, 1)
	isReentrant : Boolean (attr, 1)
	isSynchronous : Boolean (attr, 1)
}
```

```plantuml
enum BswExecutionContext {
	hook
	interruptCat1
	interruptCat2
	task
	unspecified
}
enum BswCallType {
	callback
	callout
	interrupt
	regular
	scheduled
}
```

*Note:* Configuration of the BSW Scheduler specifies which `providedModeGroup` connects to which `requiredModeGroup`.
### Step: Internal Behavior
---
#### `BswInternalBehavior`
---
```plantuml
abstract InternalBehavior {
	dataTypeMapping : DataTypeMappingSet (ref, *)
	exclusiveArea : ExclusiveArea (aggr, *)
}
class BswInternalBehavior {
	entity : BswModuleEntity (aggr, *)
	event : BswEvent (aggr, *)
}
InternalBehavior <|-- BswInternalBehavior
```

*Note:* In BSW Scheduler configuration, the method of implementation of an `ExclusiveArea` is specified (e.g., all-interrupt blocking, `OsResource`-based, `OsSpinLock`-based). 

*Note:* In BSW Scheduler configuration, each `BswEvent` is mapped to an `OsTask`.
##### `BswModuleEntity`
---
```plantuml
abstract BswModuleEntity {
	implementedEntry : BswModuleEntry (ref, *)
	accessedModeGroup : ModeDeclarationGroupPrototype (ref, *)
	managedModeGroup : ModeDeclarationGroupPrototype (ref, *)
}
BswModuleEntity <|-- BswCalledEntity
BswModuleEntity <|-- BswSchedulableEntity
BswModuleEntity <|-- BswInterruptEntity
```
##### `BswEvent`
---
```plantuml
abstract AbstractEvent
abstract BswEvent {
	startsOnEvent : BswModuleEntity (ref, 1)
}
abstract BswScheduleEvent
class BswTimingEvent {
	(..)
}
class BswModeSwitchEvent {
	(..)
}
class BswModeSwitchedAckEvent {
	(..)
}
AbstractEvent <|-- BswEvent
BswEvent <|-- BswScheduleEvent
BswScheduleEvent <|-- BswTimingEvent
BswScheduleEvent <|-- BswModeSwitchEvent
BswScheduleEvent <|-- BswModeSwitchedAckEvent
note right of BswScheduleEvent : May only invoke a <b>BswSchedulableEntity</b>.
```
### Step: Implementation
---
#### `BswImplementation`
---
```plantuml
abstract Implementation
class BswImplementation {
	behavior : BswInternalBehavior (ref, 1)
}
Implementation <|-- BswImplementation
```
## References
---
[1] Basic Software Module Description Template, AUTOSAR Classic Platform, R20-11