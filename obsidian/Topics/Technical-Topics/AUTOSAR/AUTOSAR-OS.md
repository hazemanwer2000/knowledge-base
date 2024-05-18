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
...
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

OsSpinlock [C, 0..*]
	OsSpinlockLockMethod [P, 1]
	OsSpinlockAccessingApplication [R, 1..*]
	OsSpinlockSuccessor [R, 0..1]

OsAppMode [C, 1..*]

OsApplication [C, 0..*]
	OsTrusted [P, 1]
	OsTrustedApplicationWith(Memory)Protection [P, 1]
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
Description: The minimum cycle that may be specified for alarms, using `Set<XXX>Alarm` API(s), referencing this counter.
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
### Additional Features
---
#### Schedule Table(s)
---
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
## *References*
---
[1] ...


Trusted Function
Timing Protection
Stack Monitoring
Multi-core and spinlock