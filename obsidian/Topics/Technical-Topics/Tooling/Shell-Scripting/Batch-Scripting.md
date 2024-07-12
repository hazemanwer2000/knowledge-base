──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#Basic Syntax|Basic Syntax]]
- [[#Comment(s)|Comment(s)]]
- [[#Variable(s)|Variable(s)]]
	- [[#Variable(s)#Local Variable(s)|Local Variable(s)]]
	- [[#Variable(s)#Special Variable(s)|Special Variable(s)]]
- [[#Conditional(s) and Branching|Conditional(s) and Branching]]
- [[#Output Re-direction|Output Re-direction]]
## Content
---

A batch script, `*.bat`, is interpreted and executed by a `cmd.exe` executable.

The following are different command(s) to execute a batch script.

| Command        | Description                                                                                                             |
| -------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `cmd /c *.bat` | New interpreter is opened, executes script and terminates.                                                              |
| `cmd /k *.bat` | New interpreter is opened, executes script and remains running.                                                         |
| `*.bat`        | Executes script in currently running interpreter. However, `EXIT` build-in command does not terminate the interpretter. |
### Basic Syntax
---
Usually, a batch script begins with the line,

```
@ECHO OFF
```

By default, echo'ing of commands in a batch script is enabled. This line disables echo'ing for all forth-coming commands.

*Note:* To disable echo'ing for a single command, prepend the character `@` to it.
### Comment(s)
---
To comment in a batch script, begin a line with the built-in command `REM`.
### Variable(s)
---
To set a variable, use the `SET` built-in command.

To use a variable thereafter, surround its name with `%`.

```
REM Assign a value to a variable.
SET VARIABLE-NAME=VALUE

REM Assign a variable to another variable.
SET VARIABLE-NAME=%VARIABLE-NAME%

REM Assign a numerical value to a variable.
SET /A VARIABLE-NAME = NUMERICAL-VALUE

REM Assign the result of a mathematical expression to a variable.
SET /A VARIABLE-NAME = %VARIABLE-NAME% + %VARIABLE-NAME%
```

```
REM Extracts substring, from index 'I' (inclusive) to 'J' (exclusive).
ECHO %VARIABLE-NAME:~1,4%

REM Extracts substring, removing first and last characters.
ECHO %VARIABLE-NAME:~1,-1%

REM Replaces every occurence of substring 'SUB1' with 'SUB2'.
ECHO %VARIABLE-NAME:SUB1=SUB2%
```
#### Local Variable(s)
---
A local variable is a variable more limited in scope, set between the `SETLOCAL` and `ENDLOCAL` commands.

```
SET /A X = 0

SETLOCAL
SET /A X = 1
REM Prints '1'.
ECHO %X%
ENDLOCAL

REM Prints '0'.
ECHO %X%
```
#### Special Variable(s)
---
The variables `%0` through `%9` are special variables within a batch script.

| Variable     | Description                                         |
| ------------ | --------------------------------------------------- |
| `%0`         | File path of the currently executing script.        |
| `%1` to `%9` | Arguments passed to the currently executing script. |
### Conditional(s) and Branching
---
An `IF-ELSE` statement enables the conditional execution of a command, based on the current value of a variable.

```
REM 'IF-ELSE' statement.
IF %VARIABLE-NAME%==VALUE (COMMAND) ELSE (COMMAND)

REM Nested 'IF' statement.
IF %X%==VALUE (IF %Y%==VALUE (COMMAND))
```

The following operator(s) may be used.

| Operator | Description               |
| -------- | ------------------------- |
| `EQU`    | Equal to.                 |
| `NEQ`    | Not equal to.             |
| `LSS`    | Less than.                |
| `LEQ`    | Less than or equal to.    |
| `GTR`    | Greater than.             |
| `GEQ`    | Greater than or equal to. |
*Note:* The `NOT` operator may precede any comparison.

To execute multiple commands within a single `IF-ELSE` statement, combine commands using the following operators, executing them left-to-right.

| Operator | Description                              |
| -------- | ---------------------------------------- |
| `&`      | Run all commands.                        |
| `&&`     | Run all commands, stop at first failure. |
| `\|\|`   | Run all commands, stop at first success. |
*Note:* An `IF-ELSE` statement, combined with the `%ERRORLEVEL%` variable, may be used to emulate the behavior of the `&&` and `||` operator(s).

A `GO-TO` statement jumps to a label, proceeding execution from there onwards.

```
REM Repeat command, until it succeeds.
:SOME-LABEL
SOME-COMMAND
IF %ERRORLEVEL% NEQ 0 (GOTO :SOME-LABEL)
```
### Output Re-direction
---
Redirection of the standard output and error files, `stdout` and `stderr`, to a file, instead of the command-line, is possible.

```
REM Redirecting 'stdout' to file.
COMMAND > output.txt

REM Redirecting 'stderr' to file.
COMMAND 2> output.txt

REM Redirecting both, 'stdout' and 'stderr', to file.
COMMAND > output.txt 2>&1
```

*Note:* Alternatively, a `NUL` file may be used instead of an actual file, discarding the re-directed text.