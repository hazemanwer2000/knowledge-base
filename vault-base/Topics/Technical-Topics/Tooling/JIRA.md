──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## Content
---
*JIRA* is a project management and issue-tracking tool, used across many industries, but most popular in software development.
### JIRA Query Language (JQL)
---
*JIRA Query Language (JQL)* is a language used to query issue(s) in JIRA.

A query shall consist of one or more `CONDITION`(s), and an optional `ORDER BY ...` at the end.

*Note:* White-spaces act as (syntax) token delimiter(s) by default. Consequently, `"` is used to encapsulate white-space containing token(s) (e.g., `"in progress"`).
#### `CONDITION`
---
A `CONDITION` consists of the following:

```
FIELD OPERATOR VALUE
```
##### `OPERATOR`
---

| Operator                              |
| ------------------------------------- |
| `=`, `!=`                             |
| `>`, `>=`, `<`, `<=`                  |
| `IN`, `NOT IN`                        |
| `IS`, `IS NOT` {3}                    |
| `DURING`, `AFTER`, `BEFORE`, `ON` {2} |
| `AND`, `OR`, `NOT`                    |
| `~` {1}                               |

* {1}  `~` is used to search for words within a field.
	* `~ "WORD-1 WORD-2"` would search for `WORD-1` and `WORD-2` anywhere in the field.
	* `~ "\"WORD-1 WORD-2\""` would search for `WORD-1 WORD-2` as a phrase in the field.
* {2}
	* With `AFTER`, `BEFORE` and `ON`, a date may be specified as follows,
		* `-{VALUE}d` represents the current date minus `VALUE` days (e.g., `-7d`).
		* `{YEAR}-{MONTH}-{DAY}` represents an exact date.
	* With `DURING`, a date-range may be specified as `({START-DATE}, {END-DATE})`
* {3} `IS` and `IS NOT` are usually used with `EMPTY`, to select NULL fields.
##### `FIELD`
---

| Field      | Example Usage                          |
| ---------- | -------------------------------------- |
| `status`   | `status IN ("in progress", "pending")` |
| `priority` | `priority > High`                      |
| `type`     | `type IN (bug, story, epic)`           |
| `assignee` | `assignee = "Joe Foe"`                 |
| `reporter` | `reporter = "Foe Joe"`                 |
| `created`  | `created AFTER {DATE}`                 |
