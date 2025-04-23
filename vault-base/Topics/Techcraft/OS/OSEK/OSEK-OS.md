──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*

- [[#Specification|Specification]]
	- [[#Specification#Task Management|Task Management]]
		- [[#Task Management#Task Types|Task Types]]
	- [[#Specification#Interrupt Handling|Interrupt Handling]]
	- [[#Specification#Resource Management|Resource Management]]
		- [[#Resource Management#*OSEK Priority Ceiling Protocol*|*OSEK Priority Ceiling Protocol*]]
		- [[#Resource Management#Internal Resources|Internal Resources]]
	- [[#Specification#Alarms|Alarms]]
- [[#Miscellaneous|Miscellaneous]]
	- [[#Miscellaneous#Status Mode|Status Mode]]
- [[#API(s)|API(s)]]
	- [[#API(s)#Task Management|Task Management]]
	- [[#API(s)#Interrupt Handling|Interrupt Handling]]
	- [[#API(s)#Event Handling|Event Handling]]
	- [[#API(s)#Resource Management|Resource Management]]
	- [[#API(s)#Alarm Handling|Alarm Handling]]
	- [[#API(s)#Execution Control|Execution Control]]
	- [[#API(s)#Hook Routines|Hook Routines]]
## Content
---
*OSEK* is a standards body that has produced specifications for an embedded operating system, namely *OSEK-OS*, primarily used in the automotive industry.
### Specification
---
#### Task Management
---
Each task is configured a priority, and more than one task may be assigned the same priority.

*Note:* Ready tasks of the same priority enter a queue, and execute in the order *oldest-to-newest*.

*Note:* When no tasks are ready to execute, the system becomes *idle*.
##### Task Types
---
*OSEK* defines two types of tasks, *basic* and *extended*.
* Extended tasks may wait on events, while basic tasks may not.
* Basic tasks may be activated more than once (i.e., have queued activation requests), while extended tasks may be activated at most once.

*Note:* Events are configured, and mapped `1:1` per extended task.

The figure below shows the state diagram of basic tasks.

![[OSEK-Basic-Task-State-Diagram.png|325]]

The figure below shows the state diagram of extended tasks.

![[OSEK-Extended-Task-State-Diagram.png|450]]
#### Interrupt Handling
---
*OSEK* defines two types of interrupts:
* ISR Category-1, may not make any (except interrupt handling) system calls.
* ISR Category-2, may make more system calls.
#### Resource Management
---
A resource must be acquired and released in a *Last-In-First-Out (LIFO)* order.
##### *OSEK Priority Ceiling Protocol*
---
To avoid possible priority inversion and deadlocks, *OSEK* defines the *OSEK Priority Ceiling Protocol*.
* Each task specifies which resources it uses at configuration-time.
* Each resource is assigned a *ceiling priority*, which is the highest priority of any task that uses that resource.
* When a task acquires a resource, it inherits the ceiling-priority of that resource.
* Before releasing the resource, the task may not call `TerminateTask(..)` or `ChainTask(..)`, and if the task is extended, it may not call `WaitEvent(..)`, which guarantees it will not transition out of either the *running*, or *ready* states.

*Note:* The *OSEK Priority Ceiling Protocol* may be extended to interrupts, but not necessary for an implementation to be *OSEK-compliant*.
##### Internal Resources
---
Each task may be configured an *internal resource*, that,
* It inherits the ceiling-priority of (i.e., acquires it) when entering into the *running* state,
* And returns to its configured priority (i.e., releases its internal resource) when leaving the *running* state.

Hence,
* Tasks with a shared internal resource may not preempt each other, and constitute a *task group*.
* Fully preemptable tasks have no internal resource configured.
* Non-preemptable tasks have *RES_SCHEDULER* as an internal resource configured, which has the highest ceiling-priority in the system.

#### Alarms
---
An expiring alarm may be configured to perform different actions:
* Activate a suspended task.
* Trigger event(s).
* Execute a callback routine.
### Miscellaneous
---
#### Status Mode
---
*OSEK* defines two status modes system-wide, *standard* and *extended*.

In *extended* mode, more fatal errors (i.e., errors that may induce a forced-system shutdown) are checked for and reported as application errors (i.e., passing a `NULL` pointer to an OS API). It is employed in the development phase.

*Standard* mode, on the other hand, is employed in the production phase.
### API(s)
---
*Note:* Refer to [1] for a chart showing which API(s) may be called from which context(s).
#### Task Management
---

| Name               | Description                                                                                                                                                                             |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ActivateTask(ID)` | Activate task.                                                                                                                                                                          |
| `TerminateTask()`  | Terminate task.                                                                                                                                                                         |
| `ChainTask(ID)`    | Terminate, then activate task.                                                                                                                                                          |
| `Schedule()`       | If a higher priority task is *ready*, the internal resource of the task is released, the current task is put in the *ready* state, and the higher priority task in the *running* state. |
#### Interrupt Handling
---

| Name                     | May be nested? | Description                        |
| ------------------------ | -------------- | ---------------------------------- |
| `DisableAllInterrupts()` | No             | Disable all interrupts.            |
| `EnableAllInterrupts()`  | No             | Enable all interrupts.             |
| `SuspendAllInterrupts()` | Yes            | Suspend all interrupts.            |
| `ResumeAllInterrupts()`  | Yes            | Resume all interrupts.             |
| `SuspendOSInterrupts()`  | Yes            | Suspend all Category-2 interrupts. |
| `ResumeOSInterrupts()`   | Yes            | Resume all Category-2 interrupts.  |

*Note:* Within any critical section established by any interrupt handling API(s), any other type of system call within this critical section is not permitted.
#### Event Handling
---

| Name                    | Description                                         |
| ----------------------- | --------------------------------------------------- |
| `SetEvent(ID, Mask)`    | Set event(s).                                       |
| `ClearEvent(Mask)`      | Clear event(s).                                     |
| `GetEvent(ID, MaskPtr)` | Get event(s).                                       |
| `WaitEvent(Mask)`       | Wait on event(s), returns when at least one is set. |
#### Resource Management
---

| Name              | Description         |
| ----------------- | ------------------- |
| `GetResource`     | Acquire a resource. |
| `ReleaseResource` | Release a resource. |

#### Alarm Handling
---

| Name                            | Description                                                                                                                                                        |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `GetAlarm(ID, TickPtr)`         | Get the remaining number of ticks before an alarm expires.                                                                                                         |
| `SetRelAlarm(ID, Start, Cycle)` | Set an alarm to expire, initially after `Start` number of ticks, relative to the current counter value, then, cyclically after `Cycle` number of ticks thereafter. |
| `SetAbsAlarm(ID, Start, Cycle)` | Set an alarm to expire, initially at `Start` number of ticks, compared to the current counter value, then, cyclically after `Cycle` number of ticks thereafter.    |
| `CancelAlarm(ID)`               | Cancel an alarm.                                                                                                                                                   |
#### Execution Control
---

| Name                 | Description                                           |
| -------------------- | ----------------------------------------------------- |
| `StartOS(AppMode)`   | Start the OS, in a specific application mode.         |
| `ShutdownOS(Status)` | Shutdown the OS, passing an error (i.e., not `E_OK`). |
#### Hook Routines
---

| Name             | Description                                                                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `StartupHook()`  | Called after `StartOS` has been called, and the system has been initialized (implementation-specific), but before the scheduler is executing. |
| `ShutdownHook()` | Called after the system has ran into a fatal error, or `ShutdownOS(..)` has been called.                                                      |
| `ErrorHook()`    | Called whenever an OS API returns a status other than `E_OK`, before the call returns.                                                        |
## *References*
---
[1] Operating System Specification, OSEK, 2.2.3