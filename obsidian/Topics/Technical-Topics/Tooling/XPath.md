──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#Introduction|Introduction]]
	- [[#Introduction#Axes|Axes]]
	- [[#Introduction#Operator(s)|Operator(s)]]
	- [[#Introduction#Function(s)|Function(s)]]
## Content
---
*XPath*, which stands for *XML Path Language*, is used for navigating through XML document(s).
### Introduction
---
*XPath* expression(s) are either,
* relative (to the current element), starting with `./`, or,
* absolute (i.e., relative to the root element), starting with `/`.

Afterwards, a number of `/`-separated (sub-)expression(s) are specified, each of which may consist of,
* An *axis*, which specifies the search-space,
* a name, which may be,
	* tag-name, for element(s)
	* attribute-name, for attribute(s)
	* `*`, as wildcard
	* `text()`, as a special-case, to extract text from element(s)
* a predicate (i.e., conditional).

```
AXIS::NAME[PREDICATE]
```
#### Axes
---
The following axes may be used:
* `ancestor`, or `ancestor-or-self`
* `descendant`, or `descendant-or-self`
* `parent`, or `child`
* `following-sibling`, or `preceding-sibling`,
* `attribute`

The following axis abbreviation(s) may be used:
* `descendant::` as `/`
* `attribute::` as `@`

*Note:* When unspecified, the default axis is `child`.
#### Operator(s)
---
The following operator(s) may be used:
* `=`, `!=`, `<`, `<=`, `>`, and `>=`
* `or`, `and`
* `(` and `)`, for grouping
* `"..."`, for string(s)
* `|`, to combine result(s) from two *XPath* expression(s)
#### Function(s)
---
The following function(s) may be used:
* Category: *Statistics*
	* `count(EXPR)`, to count the number of match(es) to an expression.
* Category: *Indexing*
	* `position()`, used in predicate(s), which,
		* when used over `child` element(s), determines the position of the element among its siblings, starting with `1`.
		* when used over a whole expression (i.e., `(EXPR)`), determines the (arbitrary) position of the element among other match(es).
	* `last()`, used in predicate(s), which,
		* when used over `child` element(s), determines the position of the last-element among its siblings.
		* when used over a whole expression (i.e., `(EXPR)`), determines the (arbitrary) position of the last element among other match(es).
* Category: *Casting*
	* `string(EXPR)`
	* `number(EXPR)`
* Category: *String-Manipulation*
	* `contains(EXPR,STR)`
	* `starts-with(EXPR,STR)`
	* `ends-with(EXPR,STR)`
## References
---
[1] XML Path Language (XPath), Version 1.0, W3C