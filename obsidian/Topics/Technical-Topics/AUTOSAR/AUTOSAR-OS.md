──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
### Definitions
---
* **Inter-arrival Time:**
	* For basic tasks, this is the time between successively entering the `READY` state from the `SUSPENDED` state.
	* For extended tasks, this is the time between successively entering the `READY` state from the `SUSPENDED` or `WAITING` state. Note that waiting for an event that is already set represents a new arrival.
	* For interrupts, this is the time between successive occurrences of the interrupt.
### Specification
---
The AUTOSAR (Classic-Platform) OS is primarily based on *OSEK* [1], a single-core OS, but extends its specification with more features, even supporting multi-core targets.

*Note:* Reading through [1] is a pre-requisite to reading through this document.
#### OS Application(s)
---
An *OS Application*, in-concept, is a collection of OS objects (e.g., tasks, ISR(s), resources) that all have access to each other (i.e., are allowed as parameters to OS system calls).

*Note:* The right to access an OS object by other OS Application(s) must be granted explicitly (i.e., via the configuration reference `Os<...>AccessingApplication`).

*Note:* An event is accessible if the task for which the event belongs to (i.e., may wait on) is accessible.
#### Scalability Class
---
The *Scalability Class* of the OS is a configuration parameter, that specifies the features (e.g., memory protection, timing protection) that shall be supported by the OS.

*Note:* Refer to [2] for the different Scalability Class(es) available.
### Configuration
---
```
OsAlarm [C, 0..*]
	OsAlarmAccessingApplication [R, 0..*]
	OsAlarmCounterRef [R, 1]
	
	OsAlarmAction [C, 1]

		OsAlarmActivateTask [C, 0..1]
			OsAlarmActivateTaskRef [R, 1]
			
		OsAlarmSetEvent [C, 0..1]
			OsAlarmSetEventRef [R, 1]

		OsAlarmCallback [C, 0..1]
			OsAlarmCallbackName [P, 1]
		
		OsAlarmIncrementCounter [C, 0..1]
			OsAlarmIncrementCounterRef [R, 1]

	OsAlarmAutostart [C, 0..1]
		OsAlarmAlarmTime [P]
		OsAlarmCycleTime [P]
		OsAlarmAutostartType [P]
		OsAlarmAppModeRef [R, 1..*]

OsCounter [C, 0..*] 
	OsCounterMaxAllowedValue [P]
	OsCounterMinCycle [P]
	OsCounterType [P]
	OsCounterAccessingApplication [R, 0..*]

	OsDriver [C, 0..1]
		OsGptChannelRef [R, 0..1]

OsTask [C, 0..*]
	OsTaskActivation [P, 1]
	OsTaskPriority [P, 1]
	OsTaskSchedule [P, 1]
	OsTaskAccessingApplication [R, 0..*]
	OsTaskEventRef [R, 0..*]
	OsTaskResourceRef [R, 0..*]
	
	OsTaskAutostart [C, 0..1]
		OsTaskAppModeRef [R, 1..*]
	
	OsTaskTimingProtection [C, 0..1]
		OsTaskAllInterruptLockBudget [P, 0..1]
		OsTaskOsInterruptLockBudget [P, 0..1]
		OsTaskExecutionBudget [P, 0..1]
		OsTaskTimeFrame [P, 0..1]

		OsTaskResourceLock [C, 0..*]
			OsTaskResourceLockBudget [P, 1]
			OsTaskResourceLockResourceRef [R, 1]

OsIsr [C, 0..*]
	OsIsrCategory [P, 1]
	OsIsrResourceRef [R, 0..*]

	OsIsrTimingProtection [C, 0..1]
		OsIsrAllInterruptLockBudget [P, 0..1]
		OsIsrOsInterruptLockBudget [P, 0..1]
		OsIsrExecutionBudget [P, 0..1]
		OsIsrTimeFrame [P, 0..1]

		OsIsrResourceLock [C, 0..*]
			OsIsrResourceLockBudget [P, 1]
			OsIsrResourceLockResourceRef [R, 1]

OsEvent [C, 0..*]
	OsEventMask [P, 0..1]

OsResource [C, 0..*]
	OsResourceProperty [P, 1]
	OsResourceAccessingApplication [0..*]

OsAppMode [C, 1..*]

OsApplication [C, 0..*]
	OsTrusted [P, 1]
	OsTrustedApplicationWithProtection [P, 1]
	OsApplicationCoreRef [P, 0..1]
	OsAppAlarmRef [R, 0..*]
	OsAppCounterRef [R, 0..*]
	OsAppTaskRef [R, 0..*]
	OsAppIsrRef [R, 0..*]
	OsAppScheduleTableRef [R, 0..*]

	OsApplicationHooks [C, 1]
		OsAppStartupHook [P, 1]
		OsAppShutdownHook [P, 1]
		OsAppErrorHook [P, 1]

	OsApplicationTrustedFunction [C, 0..*]
		OsTrustedFunctionName [P, 1]

OsOS [C, 1]
	OsNumberOfCores [P, 0..1]
	OsScalabilityClass [P, 0..1]
	OsStackMonitoring [P, 1]

	OsHooks [C, 1]
		OsStartupHook [P, 1]
		OsShutdownHook [P, 1]
		OsErrorHook [P, 1]
		OsProtectionHook [P, 1]
		OsPreTaskHook [P, 1]
		OsPostTaskHook [P, 1]
```
###### `OsAlarm`
---
```
Path: OsAlarm/OsAlarmAutostart/OsAlarmAlarmTime
Description: The number of ticks, at which the alarm initially expires.
```

```
Path: OsAlarm/OsAlarmAutostart/OsAlarmCycleTime
Description: The number of ticks, at which the alarm cyclically expires. If zero, the alarm is not cyclic.
```

```
Path: OsAlarm/OsAlarmAutostart/OsAlarmAutostartType
Description: Specifies whether upon 'StartOs', 'SetRelAlarm' or 'SetAbsAlarm' is called.
```
###### `OsCounter`
---
```
Path: OsCounter/OsCounterMaxAllowedValue
Description: The maximum number of ticks, before the counter wraps to zero.
```

```
Path: OsCounter/OsCounterMinCycle
Description: The minimum cycle that may be specified for alarms, using `Set<...>Alarm` API(s), referencing this counter.
```

```
Path: OsCounter/OsCounterType
Description: Specifies whether the counter is driven by hardware (i.e., via a timer unit), or software (i.e., incremented using 'IncrementCounter' API).
```
###### `OsTask`
---
```
Path: OsTask/OsTaskActivation
Description: The maximum number of queued task activations to support. If set to one, then queuing of task activation requests is not supported for this task.
```

```
Path: OsTask/OsTaskPriority
Description: The priority of the task, where a higher value corresponds to a higher priority.
```

```
Path: OsTask/OsTaskSchedule
Description: The preemptibility of the task, 'NON' (i.e., not preemptable) or 'FULL' (i.e., preemptable).
```

```
Path: OsTask/OsTaskEventRef
Description: Reference to an event, that this task may wait on.
```

```
Path: OsTask/OsTaskResourceRef
Description: Reference to a resource, that this task may acquire.
```

```
Path: OsTask/OsTaskTimingProtection/OsTaskTimeFrame
Description: Minimum inter-arrival time.
```
###### `OsResource`
---
```
Path: OsResource/OsResourceProperty
Description: Resource type, whether 'INTERNAL' or 'STANDARD'.
```
###### `OsApplication`
---
```
Path: OsApplication/OsTrusted
Description: Implementation-specific, usually toggles between execution in a higher/lower-level processor privilege mode (e.g., supervisor and user).
```

```
Path: OsApplication/OsTrustedApplicationWithProtection
Description: Implementation-specific, usually toggles between access to peripheral address-space.
```
###### `OsOS`
---
```
Path: OsOS/OsStackMonitoring
Description: In the absence of an MPU hardware unit, this specifies whether software stack monitoring is enabled for tasks and CAT2 ISR(s).
```
### API(s)
---

| Name              | Description                                               |
| ----------------- | --------------------------------------------------------- |
| `<...>TaskAsync`  | Similar to `<...>Task`, primarily used for across cores.  |
| `<...>EventAsync` | Similar to `<...>Event`, primarily used for across cores. |

*Note:* For asynchronous call(s), possible error(s) are not reported to the caller directly.
### Additional Features
---
#### Schedule Table(s)
---
##### Specification
---
A *Schedule Table* defines a duration, and a series of expiry points to occur within this duration. With each expiry point, task(s) may be activated and event(s) may be set.

*Note:* Schedule Table(s) have a similar use-case to Alarm(s).

*Note:* For each expiry point, all task activation(s) are processed first, then all event(s) are set.

The state diagram of a schedule table is shown below.

![[AUTOSAR-OS-Schedule-Table-States.png|550]]

*Note:* `NextScheduleTable` may be used to stop, after the current cycle, and start another schedule table, as long as both are driven by the same counter.
###### Synchronization
---
A schedule table may be synchronized *implicitly*, or *explicitly*.

In implicit synchronization, the schedule table must reference a counter that has a modulus (i.e., maximum counter tick value plus 1) equal to its duration, to guarantee that expiry points occur at the same counter tick value every time.

The state diagram of an implicitly synchronized schedule table is shown below.

![[AUTOSAR-OS-Schedule-Table-Implict-States.png|625]]

In explicit synchronization, the schedule table is driven by a counter, as usual, but it must be synchronized on a counter value, called the *synchronization counter*, that is not a OS counter object.

*Note:* The schedule table duration must be equal to the modulus of the synchronization counter.

*Note:* Unlike in implicit synchronization, explicit synchronization requires that the schedule table's zero tick occurs when the synchronization counter tick value is zero as well.

The state diagram of an explicitly synchronized schedule table is shown below.

![[AUTOSAR-OS-Schedule-Table-Explicit-States.png]]
To notify the OS of the synchronization counter value, `SyncScheduleTable` is called. When given, and a drift was identified (i.e., schedule table tick value `!=` synchronization counter tick value), then *adjustable* expiry points are either, lengthened or shortened, until the schedule table is synchronized.

*Note:* If `SetScheduleTableAsync` is called, drift is ignored, until the next `SyncScheduleTable` call.
##### Configuration
---
```
OsScheduleTable [C, 0..*]
	OsScheduleTableDuration [P, 1]
	OsScheduleTableRepeating [P, 1]
	OsScheduleTableAccessingApplication [R, 1]
	OsScheduleTableCounterRef [R, 1]

	OsScheduleTableAutostart [C, 0..1]
		OsScheduleTableAutostartType [P, 1]
		OsScheduleTableStartValue [P, 1]
		OsScheduleTableAppModeRef [R, 1..*]

	OsScheduleTableExpiryPoint [C, 1..*]
		OsScheduleTblExpPointOffset [P, 1]

		OsScheduleTblAdjustableExpPoint [C, 0..1]
			OsScheduleTableMaxLengthen [P, 1]
			OsScheduleTableMaxShorten [P, 1]

		OsScheduleTableEventSetting [C, 0..*]
			OsScheduleTableSetEventRef [R, 1]
			OsScheduleTableSetEventTaskRef [R, 1]

		OsScheduleTableActivateTaskRef [C, 0..*]
			OsScheduleTableSetEventRef [R, 1]
			OsScheduleTableSetEventTaskRef [R, 1]

	OsScheduleTableSync [C, 0..1]
		OsScheduleTableSyncStrategy [P, 1]
		OsScheduleTblExplicitPrecision [P, 1]
```
###### `OsScheduleTable`
---
```
Path: OsScheduleTable/OsScheduleTableAutostart/OsScheduleTableAutostartType
Description: Specifies the API to use to start the schedule table.
Range:
	ABSOLUTE (i.e., StartScheduleTableAbs)
	RELATIVE (i.e., StartScheduleTableRel)
	SYNCHRON (i.e., StartScheduleTableSynchron)
```

```
Path: OsScheduleTable/OsScheduleTableSync/OsScheduleTableSyncStrategy
Description: Specifies the sync strategy, whether IMPLICIT or EXPLICIT.
```

```
Path: OsScheduleTable/OsScheduleTableSync/OsScheduleTblExplicitPrecision
Description: When the sync strategy is EXPLICIT, it specifies the precision (i.e., tick difference) below which the schedule table is considered synchronized.
```
#### Spinlock(s)
---
##### Specification
---
A *spin-lock* is a busy-wait mechanism, that uses a *test-and-set* hardware instruction to synchronize access to a variable across multiple cores.

To avoid a situation where a lower-priority task acquires a spin-lock, and is pre-empted by a higher-priority task, it is possible to specify different actions to wrap around the spin-lock acquiring/releasing API(s) (see `OsSpinlockLockMethod`).

To avoid a dead-lock situation, nested spin-lock acquisition must be ordered, according to the configuration reference value `OsSpinlockSuccess`, with which a linked list of spin-lock(s) may be formed.

*Note:* When acquiring spin-lock(s), in a nested fashion, it is permitted to skip spin-lock(s) in-between.
##### Configuration
---
```
OsSpinlock [C, 0..*]
	OsSpinlockLockMethod [P, 1]
	OsSpinlockAccessingApplication [R, 1..*]
	OsSpinlockSuccessor [R, 0..1]
```
###### `OsSpinlock`
---
```
Path: OsSpinlock/OsSpinlockLockMethod
Description: Specifies the action to take, before/after acquiring/releasing a spin-lock.
Range:
	LOCK_ALL_INTERRUPTS
	LOCK_ALL_CAT2_INTERRUPTS
	LOCK_WITH_RES_SCHEDULER
	LOCK_NOTHING
```

```
Path: OsSpinlock/OsSpinlockSuccessor
Description: References the spin-lock next in the linked list, that may be acquired.
```
##### API(s)
---

| Name               | Description                                         |
| ------------------ | --------------------------------------------------- |
| `GetSpinlock`      | Acquire a spin-lock, busy-wait if already occupied. |
| `TryToGetSpinlock` | Acquire a spin-lock, return if already occupied.    |
| `ReleaseSpinlock`  | Release a spin-lock.                                |

## *References*
---
[1] Operating System Specification, OSEK, 2.2.3
[2] Specification of Operating System, AUTOSAR Classic Platform, R20-11