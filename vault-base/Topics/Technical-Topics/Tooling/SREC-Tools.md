──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
SREC-Tools are a set of tool(s) for analyzing, manipulating and comparing HEX file(s), of different format(s) (e.g., `.s19`).
### Command File
---
All SREC-Tools support receiving CLI argument(s) within a so-called *Command File*.

For example,

```
srec_cat @command.txt
```

```
# COMMENT
-OPTION VALUE
```
### `srec_cat`
---
`srec_cat` is used to manipulate HEX file(s).

It has the following format:

```
srec_cat INPUT-1 ... INPUT-N -o OUTPUT
```

`INPUT` may be any of the following:
* HEX file (e.g., `.s19`).
* Binary file, specified as `FILE -binary`.
* Arbitrary (empty) address-range, specified as `-generate ADDRESS-RANGE`.

Every `INPUT` or `OUTPUT` may be followed by a consecutive number of filter(s), order-sensitive.
#### `ADDRESS-RANGE`
---
`ADDRESS-RANGE` may be any of the following:
* Consecutive number of space-separated start- and end- address(es).
#### Working with HEX file(s)
#### Command File
---
`srec_cat` supports 
## References
---
[1] ...