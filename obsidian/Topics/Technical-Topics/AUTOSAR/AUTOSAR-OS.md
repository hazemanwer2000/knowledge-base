──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
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
			OsAlarmCallbackName [P]
		
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

OsApplication [C, 0..*]

OsAppMode [C, 1..*]

OsEvent [C, 0..*]

OsScheduleTable [C, 0..*]

OsResource [C, 0..*]

OsSpinlock [C, 0..*]

OsPeripheralArea [C, 0..UINT16_MAX]

OsIoc [C, 0..1]
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
## *References*
---
[1] ...