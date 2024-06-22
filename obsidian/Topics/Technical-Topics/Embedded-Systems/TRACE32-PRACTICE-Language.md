──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#General Command(s)|General Command(s)]]
- [[#PRACTICE Language|PRACTICE Language]]
	- [[#PRACTICE Language#Macro(s)|Macro(s)]]
	- [[#PRACTICE Language#Operator(s)|Operator(s)]]
	- [[#PRACTICE Language#Flow Control|Flow Control]]
	- [[#PRACTICE Language#Sub-Routine(s)|Sub-Routine(s)]]
	- [[#PRACTICE Language#PRACTICE Command(s)|PRACTICE Command(s)]]
		- [[#PRACTICE Command(s)#User I/O|User I/O]]
		- [[#PRACTICE Command(s)#Delay|Delay]]
	- [[#PRACTICE Language#PRACTICE Function(s)|PRACTICE Function(s)]]
## Content
---
### General Command(s)
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

To clear an `Area` view,

```
Area.Clear AREA_NAME
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
	BEGIN_ADDRESS++OFFSET_TO_BEGIN_ADDRESS
	ADDRESS
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
	BEGIN_ADDRESS++OFFSET_TO_BEGIN_ADDRESS
	ADDRESS
```

*Note:* Address ranges are all-inclusive.
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
#### `Per`
---
To view peripherals,

```
Per.View
```

To set a peripheral register,

```
Per.Set.Simple ADDRESS %FORMAT VALUE

FORMAT:
	Byte
	Word (i.e., 2 byte(s))
	Long (i.e., 4 byte(s))
	Quad (i.e., 8 byte(s))
```

To print a peripheral register's value,

```
Per.In ADDRESS /FORMAT
```
#### `Register`
---
To view the registers of a specific core,

```
Register.View /CORE CORE_NUMBER
```

To set a register of a specific core,

```
Register.Set REGISTER VALUE /CORE CORE_NUMBER
```
#### `Flash`
---
To erase and flash memory,

```
; After this command, updating address(es) of flash area(s) is allowed
; Note: Flash is not actually updated (i.e., erased and programmed) until 'Flash.Auto off'
Flash.Auto all

Data.Load.* ...
Var.Set ...

Flash.Auto off
```

#### `Trace`
---
To select the trace method,

```
Trace.Method METHOD

METHOD:
	Snooper
	...
```

To list the samples captured,

```
Trace.List
```

To chart the active function/task against time (when applicable),

```
Trace.Chart [/Core CORE_NUMBER]

Trace.Chart.Task [/Core CORE_NUMBER]
```

To get statistics about all function/task activity (when applicable),

```
Trace.Statistics [/Core CORE_NUMBER]

Trace.Chart.Task [/Core CORE_NUMBER]
```

To draw the value of a traced variable against time (when applicable),

```
Trace.Draw
```
##### `Snooper`
---
The *Snooper* method can be used to sample a number of addresses, or address ranges.

To select the mode,

```
Snooper.Mode MODE

MODE:
	Memory - Samples specified address(es)
	PC - Samples the PC register
```

In `PC` mode, to specify which core(s) to snoop the PC register of,

```
Snooper.Core CORE_NUMBER [CORE_NUMBER ...]
```

To specify address(es) to sample (in `Memory` mode only),

```
Snooper.Select %FORMAT ADDRESS [%FORMAT ADDRESS ...]

ADDRESS:
	SINGLE_ADDRESS (e.g., 0x90000000)
	BEGIN_ADDRESS--END_ADDRESS (e.g., 0x90000000--0x9000000F)
	BEGIN_ADDRESS++OFFSET_TO_BEGIN_ADDRESS (e.g., 0x90000000++0x0F)
```

*Note:* Address ranges are all-inclusive.

To set the target sampling rate,

```
Snooper.Rate FREQ_HZ              ; e.g., '1000000.' (1 MHz)
```

*Note:* The target sampling rate may not be reached, depending on many factors.

To set the size of the sampling buffer, which is stored in host (i.e., PC),

```
Snooper.Size NUMBER_OF_SAMPLES
```
#### `Core`
---
To select the default core, to be used when command(s) and function(s) do not specify a core,

```
Core.Select CORE_NUMBER
```
### PRACTICE Language
---
A PRACTICE script, a `*.cmm` file, must always be terminated with a `ENDDO` command.
#### Macro(s)
---
A PRACTICE macro resembles a C-preprocessor macro, that is only substituted during line interpretation.

A PRACTICE macro can be defined with different scope.

```
; Accessible only within nested block(s)
PRIVATE &myMacro

; Accessible within nested block(s), sub-routines and sub-scripts
LOCAL &myMacro

; Accessible everywhere, with an unlimited life-time
GLOBAL &myMacro         
```

More than one macro can be declared on the same line.

```
<SCOPE> &x &y &z
```

To assign a value to a macro,

```
&myStringMacro="..."
&myIntegerMacro=123
&myFloatMacro=1.23
```

To reference a macro elsewhere, prepend `&` to its name (e.g., `&myMacro`).

*Note:* When string (i.e., quoted) macro values are replaced, the quotes are removed, so it is interpreted unquoted (i.e., not a string). To preserve its interpretation as a string, surround it double quotes (e.g., `"&myMacro"`). This does not apply to when strings are passed across a (function-/script-)call, and then referenced.
#### Operator(s)
---
PRACTICE language supports arithmetic, bitwise and logical C-operators, in addition to parentheses.

It also supports the range operator, `--`, which may be used to express address r

*Note:* Strings may be concatenated using the addition operator, `+`.
#### Flow Control
---
The following is a list of all flow control commands in PRACTICE language.

```
IF <PRACTICE-EXPR>                       ; Alternatively, 'Var.IF <HLL-EXPR>'
(
	...
)
ELSE
(
	...
)
```

```
WHILE <PRACTICE-EXPR>                    ; Alternatively, 'Var.WHILE <HLL-EXPR>'
(
	...
)
```

```
REPEAT <COUNT>
(
	...
)
```
#### Sub-Routine(s)
---
PRACTICE language supports sub-routines, which must reside at the end of a script.

```
...
SUBDO <SUB-NAME> [<ARG> ..]                              ; Calls <SUB-NAME>, passing while arguments
ENTRY [&<MACRO-NAME> ..]                                 ; Reads return-value(s), in macro(s)
...
ENDDO

<SUB-NAME>:
(
	ENTRY [&<MACRO-NAME> ...]                            ; Receives arguments, in macro(s)
	...
	RETURN [<RET-VAL> ..]                                ; Returns value(s)
)
```

*Note:* In a similar manner, a script may be called from another script, using the `DO` command, and the called script may return value(s) using the `ENDDO` command.
#### PRACTICE Command(s)
---
##### User I/O
---
The following command(s) may be used to get input from user.

```
INKEY &key                                      ; Waits for key-stroke, places ASCII code in 'key'
INKEY                                           ; Waits for key-stroke, does not store its value

ENTER &MACRO-NAME [&MACRO-NAME ...]             ; Waits for user-input in 'Area', space-separated
                                                ; Must match expected number of macro(s)
```

The following command(s) may be used to notify user.

```
BEEP                                            ; Produces a buzz sound
```
##### Delay
---
The `WAIT` command may be used to wait until a condition is met, or a period of time elapses.

```
WAIT [PRACTICE-EXPR] [DELAY-TIME]

DELAY-TIME:
	(INTEGER-VALUE)(UNIT) - Unit may be 'ms', or 's'
```

*Note:* `TIMEOUT()` function may be used in conditions, to check if the last `WAIT` command terminated due to a timeout.
#### PRACTICE Function(s)
---
PRACTICE provides useful functions that may be used in PRACTICE expressions.

```
TRUE()                                         ; Returns boolean value, 'TRUE'
FALSE()                                        ; Returns boolean value, 'FALSE'

RANDOM.<...>(...)                              ; Different random-generating function(s)

CONVERT.<...>(...)                             ; Different type-conversion function(s)

FORMAT.<...>(...)                              ; Different type-to-string formatting function(s)

VAR.<...>(...)                                 ; Different HLL-expression evaluation function(s)

DATA.<...>(...)                                ; Different memory read-write function(s)
```
## *References*
---
[1] TRACE32 Lauterbach User Guide Document(s), Release 02.2024