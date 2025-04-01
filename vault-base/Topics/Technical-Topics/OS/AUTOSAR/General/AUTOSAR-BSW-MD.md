──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
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
## References
---
[1] Basic Software Module Description Template, AUTOSAR Classic Platform, R20-11