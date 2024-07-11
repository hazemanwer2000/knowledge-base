──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#Rules|Rules]]
	- [[#Rules#The `.PHONY` Target|The `.PHONY` Target]]
	- [[#Rules#Pattern Rules|Pattern Rules]]
		- [[#Pattern Rules#Static Pattern Rules|Static Pattern Rules]]
	- [[#Rules#Built-in Rules|Built-in Rules]]
	- [[#Rules#Wildcards|Wildcards]]
	- [[#Rules#The `include` Directive|The `include` Directive]]
- [[#Variables|Variables]]
	- [[#Variables#Automatic Variables|Automatic Variables]]
	- [[#Variables#Command-Line Variables|Command-Line Variables]]
	- [[#Variables#Target-specific Variables|Target-specific Variables]]
	- [[#Variables#Conditional Directives|Conditional Directives]]
- [[#Functions|Functions]]
## Content
---
*GNU Make* is a build-process automation tool, mainly employed in C/C++ projects. It prevents the unnecessary re-compilation of many files, especially in a medium-to-large sized project, significantly reducing the compilation time.

The tool is called `make`, and by default, searches for a `makefile` file in the working directory. Alternatively, the file to be executed may be passed with the `-f` option.
### Rules
---
A *Makefile* consists, mainly, of a set of *rules*. Each rule specifies:
* A target file to generate.
* Prerequisite files that the target file depends on.
* Commands that use the prerequisite files to generate the target file.

```
target: prerequisites
    command
    ...
```

When you run `make TARGET`,
* A rule is searched for, that matches the target file.
    * If not found and the target file does not exist, `No rule to make TARGET` is issued.
    * If not found and the target file exists, `Nothing to be done` is issued.
    * If found, `make` proceeds.
* Iteratively, a rule is searched for, that matches each prerequisite file.
    * If not found and the prerequisite file does not exist, `No rule to make PREREQUISITE needed by TARGET` is issued.
    * If not found and the prerequisite file exists, `make` proceeds.
    * If found, this procedure repeats recursively, with the prerequisite file as the target file.
* `make` evaluates whether to execute the associated rule commands, and generate the target file.
    * If the target file does not exist, the commands are executed.
    * If the target file exists, and the *Last Modified Timestamp*, in the file system, of the target file dates older than at least one prerequisite file, the commands are executed.
    * Otherwise, `Nothing to be done` is issued.

*Note:* By default, when not specifying a target, *make* assumes the target in the first rule in the *Makefile*.

*Note:* Precede a command with `@` to stop *make* printing it again on the command-line. Alternatively, running `make` with the `-s` option places `@` before each command.

*Note:* Every command runs in a separate execution environment. Hence, for example, changing the working directory in a command, will not affect the working directory of the following command.

A multiple-target rule is permitted, and is equivalent to declaring multiple single-target rules, with the same prerequisites and commands.

```
target-1 target-2 ...: prerequisites
    command
    ...
```

A prerequisite file whose *Last Modified Timestamp* is ignored when `make` is evaluating whether to execute the associated rule commands, is placed after `|` in a rule, and is called an *order-only prerequisite*.

```
target: prereqs | order-only-prereqs
    command
    ...
```
#### The `.PHONY` Target
---
The `.PHONY` target is a built-in target in `make`, the prerequisites of which are targets themselves, and are called *phony targets*.

A phony target is not a target file, rather is treated as a command. Hence, when you run `$ make PHONY-TARGET`, the commands of a matching rule are always executed.

```
.PHONY: phony-target-1 phony-target-2 ...

phony-target-1: prerequisites
    command
    ...

phony-target-2: prerequisites
    command
    ...
```

*Note:* A phony target may be a prerequisite to another rule. In that case, this rule is also treated as a command.
#### Pattern Rules
---
A *pattern rule* is a rule that captures targets with a common naming convention.

Usually, the common partition of the name, called *stem*, is the prefix of the target name, and is represented with `%`. The captured stem may then be used in the prerequisites.

```
%.o: %.c
    command
    ...
```
##### Static Pattern Rules
---
A *static pattern rule* is a pattern rule that applies to a specific list of target files only.

```
A.o B.o C.o: %.o: %.c
    command
    ...
```
#### Built-in Rules
---
An *built-in rule* is a rule that `make` defines implicitly.

*Note:* It is recommended to cancel all built-in rules, by passing the `-r` option to `make`.
#### Wildcards
---
A *wildcard* is a special character(s), that may be placed within a target or prerequisite file names. It is expanded into all matching file names within a directory.

* `*` matches anything. For example, `*.c` expands into all *C* source files (within the working directory).
* `?` matches a single character. For example, `?.c` expands into all *C* source files with a single letter name.
* `[...]` matches a single character, of specific range.
    * `tmp[0-9].txt` expands into `tmp0.txt`, `tmp1.txt`, etc, if existing.
    * `file.[hc]` expands into `file.c` and `file.h`, if existing.
    * `[a-zA-Z].*` expands into all files with a single alphabetical character, and an extension.

*Note:* Wildcards may be used elsewhere using the `wildcard` function, discussed later.
#### The `include` Directive
---
The `include` directive may be used within a *Makefile* to import an `.mk` file, which is another *Makefile*.

```
include DOT_MK_FILE
```

*Note:* If the included *Makefile* matched a rule, it will be treated as a target file, and generated, before it is imported.
### Variables
---
A *variable* may be defined within a *Makefile* to store text, using `:=`.

```
SRCS := A.c                # Assign 'A.c'
SRCS += B.c                # Append 'B.c'
SRCS := $(SRCS) C.c        # Append 'C.c'

.PHONY: all

all: $(SRCS)
    command
    ...
```

*Note:* Leading spaces are ignored in variable definitions, while trailing spaces are kept.

*Note:* Evaluating an undefined variable yields an empty string, and issues no error.
#### Automatic Variables
---
*Automatic variables* are a number of implicitly declared variables within any rule, that may be used within its commands only.
* `$@`, denotes the target file name.
* `$^`, denotes the names of all prerequisites (exclusive of order-only prerequisites).
* `$?`, denotes the names of all prerequisites, that are newer than the target.
* `$|`, denotes the names of all order-only prerequisites.
* `$*`, denotes the stem of a pattern rule.

*Note:* Use, for example, `$(@F)`, to evaluate to file names instead of complete paths.

*Note:* Use, for example, `$(@D)`, to evaluate to containing directory paths instead of complete paths.
#### Command-Line Variables
---
A variable may be passed to `make` in the command-line (e.g., `make CC:=GCC`). 

It may then be evaluated, like any internally-defined variable, within a *Makefile*.

To override the value of a command-line variable, precede its definition with the `override` directive.

```
override CC := TCC
```
#### Target-specific Variables
---
A variable may have different definitions, each for a different target.

```
CFG := A                   # Default 'CFG' definition
%.o: CFG := B              # 'CFG' definition for any object file, as target
x.o: CFG := C              # 'CFG' definition of 'x.o', as target
```

*Note:* A target-specific definition is prioritized over a pattern-specific definition.
#### Conditional Directives
---
A *conditional directive* controls which lines, usually those that define variables, are included within a *Makefile*.

```
conditional-directive-1
    VAR := VALUE-1
else conditional-directive-2
    VAR := VALUE-2
endif
```

There are four types of conditional directives in *Make*.

```
ifeq ($(A), $(B))          # True, if the two arguments are equal
ifneq ($(A), $(B))

ifdef VAR                  # True, if 'VAR' is a non-empty variable
ifndef VAR
```
### Functions
---
A *function* is called using the following syntax.

```
$(func-name arg1,arg2,...)
```

*Make* provides built-in function(s) for string manipulation, file management, applying conditionals, looping, executing shell commands, and more. [1]
## References
---
[1]  [GNU Make Manual](https://www.gnu.org/software/make/manual/html_node/index.html)