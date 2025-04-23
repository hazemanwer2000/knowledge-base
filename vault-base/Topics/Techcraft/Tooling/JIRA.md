──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#JIRA Query Language (JQL)|JIRA Query Language (JQL)]]
	- [[#JIRA Query Language (JQL)#`CONDITION`|`CONDITION`]]
		- [[#`CONDITION`#`OPERATOR`|`OPERATOR`]]
		- [[#`CONDITION`#`FIELD`|`FIELD`]]
	- [[#JIRA Query Language (JQL)#Function(s)|Function(s)]]
	- [[#JIRA Query Language (JQL)#`ORDER BY {..}`|`ORDER BY {..}`]]
## Content
---
*JIRA* is a project management and issue-tracking tool, used across many industries, but most popular in software development.
### JIRA Query Language (JQL)
---
*JIRA Query Language (JQL)* is a language used to query issue(s) in JIRA.

A query shall consist of one or more `CONDITION`(s), and an optional `ORDER BY {..}` at the end.

*Note:* White-spaces act as (syntax) token delimiter(s) by default. Consequently, `"` is used to encapsulate white-space containing token(s) (e.g., `"in progress"`).
#### `CONDITION`
---
A `CONDITION` consists of the following:

```
FIELD OPERATOR VALUE
```
##### `OPERATOR`
---

| Operator                 |
| ------------------------ |
| `=`, `!=`                |
| `>`, `>=`, `<`, `<=` {2} |
| `IN`, `NOT IN`           |
| `IS`, `IS NOT` {3}       |
| `AND`, `OR`, `NOT`       |
| `~`, `!~` {1}            |

* {1}  `~` is used to search for words within a field.
	* `~ "WORD-1 WORD-2"` would search for `WORD-1` and `WORD-2` anywhere in the field.
	* `~ "\"WORD-1 WORD-2\""` would search for `WORD-1 WORD-2` as a phrase in the field.
	* The wildcard character, `*`, may be used within a word (e.g., `log*` would match `login` and `logged`).
* {2}
	* A date may be specified as follows,
		* `-{VALUE}d` represents the current date minus `VALUE` days (e.g., `-7d`).
		* `{YEAR}-{MONTH}-{DAY}` represents an exact date.
* {3} `IS` and `IS NOT` are usually used with `EMPTY`, to select NULL fields.
* {4} `IN` and `NOT IN` are used to test membership within a list, represented as `(VALUE-1, ..)`.
##### `FIELD`
---

| Field         | Usage                                                                                   |
| ------------- | --------------------------------------------------------------------------------------- |
| `status`      | E.g., `status IN ("in progress", "pending")`                                            |
| `priority`    | E.g., `priority > High`                                                                 |
| `type`        | E.g., `type IN (bug, story, epic)`                                                      |
| `assignee`    | E.g., `assignee = "Joe Foe"`                                                            |
| `reporter`    | E.g., `reporter = "Foe Joe"`                                                            |
| `created`     | E.g., `created AFTER {DATE}`                                                            |
| `sprint`      | E.g., `sprint = {SPRINT}`                                                               |
| `team`        | E.g., `team = {TEAM}`                                                                   |
| `summary`     | Used to search within the title of an issue.                                            |
| `description` | Used to search within the description of an issue.                                      |
| `comment`     | Used to search within the comments of an issue.                                         |
| `text`        | Used to search, more generally, within all text inside an issue.                        |
| `labels`      | E.g., `labels IN (LABEL-1, LABEL-2)` (i.e., issue has `LABEL-1` or `LABEL-2` assigned). |
#### Function(s)
---

| Function                     | Usage                                                                                                                                               |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `startOf?(..)`, `endOf?(..)` | Returns the start-of, or end-of, either day, week, or month.<br>If passed a value, e.g., `X`, it offsets the date by `X` days, weeks, or months. `` |
| `currentUser()`              | Returns the name of the current user.                                                                                                               |
| `openSprints()`              | Returns a list of all active sprints.                                                                                                               |
#### `ORDER BY {..}`
---
`ORDER BY {...}` may be used to sort the results of a query.

For example,
* `ORDER BY priority DESC, created ASC` would,
	* First, sort by priority, highest to lowest.
	* Second, for same priority, sort by creation time, oldest first.