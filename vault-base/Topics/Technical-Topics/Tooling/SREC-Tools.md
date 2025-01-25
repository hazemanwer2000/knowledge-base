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
* HEX file, specified as `FILE`.
* Binary file, specified as `FILE -binary`.
* Arbitrary (empty) address-range, specified as `-generate ADDRESS-RANGE`.

`OUTPUT` may be any of the following:
* HEX file, specified as `FILE`.
* Binary file, specified as `FILE -binary`.

*Note:* Binary input or output file(s) assume an `ADDRESS-RANGE` that starts from zero, and is consecutive. When specified as output file(s), any hole(s), up-to the maximum address, are zero-filled.

Every `INPUT` or `OUTPUT` may be followed by a consecutive number of filter(s), order-sensitive.
#### `ADDRESS-RANGE`
---
`ADDRESS-RANGE` may be any of the following:
* Consecutive number of start- and end- address(es), end-address exclusive.
	* For example, `0x8000 0x8100 0x8200 0x8300`.
* `-within FILE`, specifying the address-range(s) within a file, excluding hole(s).
* `-over FILE`, specifying the address-range(s) within a file, including hole(s).
#### Input Filter(s)
---
For a HEX file such as `.s19`, the following filter may be used to ignore, and re-calculate, checksum(s).

```
-ignore-checksums
```

To offset the address(s) by a specific value, which may be negative,

```
-offset VALUE
```

To extract byte(s) from specific address-range(s),

```
-crop ADDRESS-RANGE
```

To exclude byte(s) from specific address-range(s),

```
-exclude ADDRESS-RANGE
```

To fill hole(s) within specific address-range(s),

```
-fill VALUE ADDRESS-RANGE

VALUE: 0x00 to 0xFF
```

```
-random-fill ADDRESS-RANGE
```
## References
---
[1] ...