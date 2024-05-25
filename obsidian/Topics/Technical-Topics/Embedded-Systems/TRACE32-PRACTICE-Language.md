──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---

### Command Group(s)
---
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
## References
---
[1] ...