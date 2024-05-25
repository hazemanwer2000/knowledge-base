──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
...
### Command Group(s)
---
#### `Break`
---
To set a breakpoint on a function (using on-chip facilities),

```
Break.Set FUNCTION_NAME /OnChip [/Task "TASK_NAME"] [/Core CORE_NUMBER] [/VarCondition CONDITION] [/CMD COMMAND] [/Resume]
```

To set a read/write breakpoint on a variable,

```
Var.Break.Set VARIABLE_NAME /ReadWrite|/Read|/Write /OnChip [/Data.Auto VALUE] ...
```

The following are other useful `Break` commands:

```
Break.List                 ; Open a view, listing all breakpoint(s)
Break.Reset                ; Delete all breakpoint(s)
Break.Disable              ; Disable all breakpoint(s)
```
#### `Area`
---
To create a new `Area` view,

```
Area.Create AREA_NAME
```

To show the new `Area` view window,

```
Area.View AREA_NAME
```

To select an `Area` view (i.e., for `Print` commands),

```
Area.Select AREA_NAME
```

To save the contents of an `Area` view to a file,

```
Area.Save AREA_NAME FILE_PATH
```
#### `Var`
---
##### `Var.Watch`
---
To open up the watch window (i.e., where values of expressions can be watched),

```
Var.Watch
```

To add an expression to the watch window,

```
Var.AddWatch [%Format] EXPRESSION
```

*Note:* To print an expression to the currently selected `Area` view, instead, use `Var.Print`.

*Note:* To clear the watch window, use `Var.DelWatch`.

The following format specifiers may be used.

| Specifier | Description                                               |
| --------- | --------------------------------------------------------- |
| `String`  | For null-terminated character arrays.                     |
| `Hex`     | Displays integer types in HEX (i.e., base-16) format      |
| `Decimal` | Displays integer types in decimal (i.e., base-10) format. |
| `Binary`  | Displays integer types in binary (i.e., base-2) format    |
##### `Var.Set`
---
To set a variable (or an *lvalue* expression),

```
Var.Set EXPRESSION = VALUE
```

To assign value(s) to an array (or, a range of), all inclusive,

```
Var.Set ARRAY[I..J] = VALUE

Var.Set ARRAY[I..J] = (VALUE, ...)
```

To assign value(s) to a structure,

```
Var.Set STRUCT = (VALUE, ...)
```

##### `Var.Profile`
---
To profile an expression,

```
Var.Profile EXPR-1 (EXPR-2 ...) REFRESH_RATE
```

*Note:* The refresh rate is specified in seconds.

*Note:* This command does not use any tracing capabilities.
#### `Data`
---
To dump a variable, or an address range, for viewing,

```
Data.Dump $RANGE$ [/Byte|/Word|/Long]

$RANGE$:
	Var.Range(VARIABLE_NAME)
	BEGIN_ADDRESS--END_ADDRESS
```

Similarly, to dump a variable, or an address range, to a file,

```
Data.Save.$FORMAT$ FILE_PATH $RANGE$

$FORMAT$:
	Binary         ; '.bin' file format
	S3Record       ; '.S19' file format, using 'S3' record(s)

$RANGE$:
	Var.Range(VARIABLE_NAME)
	BEGIN_ADDRESS--END_ADDRESS
```
#### `Frame`
---
To display the stackframe,

```
Frame.View /Core CORE_NUMBER /Task "TASK_NAME"
```
#### `Task`
---
##### `OSEK`
---
To import an *ORTI* file (for OSEK-compliant OS implementations),

```
Task.ORTI ORTI_FILE_PATH
```

To display task-stack usage (based on a fill-pattern, specified in the *ORTI* file),

```
Task.Stack
```

To display the list of tasks, their corresponding *T32*-assigned magic numbers, and which task is currently active in each core (when halted),

```
Task.List
```

To display all attributes for all objects of a specific type,

```
Task.D$OBJECT_TYPE$
```
## References
---
[1] ...