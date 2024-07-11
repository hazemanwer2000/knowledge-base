──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*GNU Make* is a build-process automation tool, mainly employed in C/C++ projects. It prevents the unnecessary re-compilation of many files, especially in a medium-to-large sized project, significantly reducing the compilation time.

The tool is called `make`, and by default, searches for a *Makefile* file in the working directory. Alternatively, the file to be executed may be passed with the `-f` option.
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
## References
---
[1] ...