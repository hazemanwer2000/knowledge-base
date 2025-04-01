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

*Note:* Any implementation of a BSW module depends on the BSW Scheduler (SchM) for the handling of event(s), and communication across BSW module(s).
### BSW Module(s)
---
#### `BswModuleDescription`
---
```plantuml

```
## References
---
[1] Basic Software Module Description Template, AUTOSAR Classic Platform, R20-11