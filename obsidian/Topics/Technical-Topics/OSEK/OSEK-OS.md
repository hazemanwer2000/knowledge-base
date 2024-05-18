──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*OSEK* is a standards body that has produced specifications for an embedded operating system, namely *OSEK-OS*, primarily used in the automotive industry.

### API(s)
---
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