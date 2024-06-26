──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*

- [[#KOIL|KOIL]]
	- [[#KOIL#File Structure|File Structure]]
	- [[#KOIL#*Version* Section|*Version* Section]]
	- [[#KOIL#*Declaration* Section|*Declaration* Section]]
		- [[#*Declaration* Section#`CTYPE`|`CTYPE`]]
		- [[#*Declaration* Section#`STRING`|`STRING`]]
		- [[#*Declaration* Section#`ENUM`|`ENUM`]]
			- [[#`ENUM`#Links|Links]]
	- [[#KOIL#*Information* Section|*Information* Section]]
-  [[#OSEK Objects and Attributes|OSEK Objects and Attributes]]
## Content
---
*OSEK Run-Time Interface (ORTI)* defines a unified interface for all debuggers, to be able to extract run-time information about an OSEK-compliant OS implementation.

For this, an `*.orti` file is generated by the respective OS generator, and is imported into the debugger's interface, to be parsed.
### KOIL
---
*Kernel Object Interface Language (KOIL)* defines the syntax used in an `*.orti` file, and is described in [1].

*Note:* *KOIL* is meant to be OS-independent (i.e., may be employed by other OS specifications),
#### File Structure
---
The file shall consist of three sections.
* *Version*, which notes the version of *KOIL* and OS specification.
* *Declaration*, which includes declarations of all relevant types.
* *Information*, which includes definitions of all relevant objects.

In the following,
* `$..$` denotes a replaceable part.
* `(...)` denotes an optional part.
#### *Version* Section
---
```
VERSION
{
	KOIL = "$koil_version_number$";
	OSSEMANTICS = "$os_version_name$", $os_version_number$;
};
```
#### *Declaration* Section
---
```
IMPLEMENTATION $implementation_name$
{
	$type_name$
	{
		(TOTRACE) $attribute_declaration$ $attribute_name$(, $attribute_description$);
		...
	}(, $type_description$);

	...
};
```

*Note:* The `TOTRACE` attribute modifier informs the debugger of the intent to trace this attribute, if feasible.

`$attribute_declaration$` may expand into a `CTYPE`, `STRING`, or `ENUM`.
##### `CTYPE`
---
The type of a `CTYPE` attribute is the *High-Level Language (HLL)* type of the value assigned to it in object definitions.

A tentative type may be declared, usually an ANSI-C primitive type, to be used in the case of lacking debug information.

```
CTYPE( $tentative_type$)
```
##### `STRING`
---
A `STRING` attribute shall be displayed by a debugger as is.

```
STRING
```
##### `ENUM`
---
An `ENUM` attribute defines possible values, and the strings to display for each corresponding value.

```
ENUM( $tentative_type$)
[
	"$value_description$" = $value$,
	...
]
```

*Note:* `$value$` may be an *HLL* expression.

###### Links
---
An `ENUM` attribute may, instead of a mere description, reference another object. In this case, the name of the attribute must match the object's type name.

For example,

```
IMPLEMENTATION ...
{
	TASK
	{
		ENUM
		[
			"First Stack" : Stack1 = "&taskStack1[0]",
			...
		] STACK;
	};

	STACK
	{
		...
	};

	...
};

TASK TaskA
{
	STACK = "taskA.stack";
	...
};

STACK Stack1
{
	...
}

...
```
#### *Information* Section
---
```
$object_type$ $object_name$
{
	$attribute_name$ = $expression$;
	...
}

...
```

*Note:* `$expression$` is any *HLL* expression.
### OSEK Objects and Attributes
---
Refer to [2] for OSEK-specific objects and attributes.
## References
---
[1] OSEK Run-Time Interface (ORTI), Part A: Language Specification, Version 2.1
[2] OSEK Run-Time Interface (ORTI), Part B: OSEK Objects and Attributes, Version 2.1