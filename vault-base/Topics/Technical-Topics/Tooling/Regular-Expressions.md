──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*

- [[#Special Character(s)|Special Character(s)]]
- [[#Character Class(es)|Character Class(es)]]
- [[#Number of Occurrences|Number of Occurrences]]
- [[#*Starts with, Ends with*|*Starts with, Ends with*]]
- [[#*Look ahead, Look behind*|*Look ahead, Look behind*]]
- [[#Group(s)|Group(s)]]
	- [[#Group(s)#Capture Group(s)|Capture Group(s)]]
## Content
---
A *regular expression (RegEx)* is a sequence of characters that specifies a search pattern. A *RegEx engine* is an application, responsible for parsing and recognizing a *RegEx* in text.

Every engine has its own flavor of *RegEx* syntax. This document will rely on *Python*'s *RegEx* flavor (i.e., its `re` built-in module).
### Special Character(s)
---
A special character is a character that is associated with a special meaning in *RegEx* syntax.

| Special Character | Description                                    |
| ----------------- | ---------------------------------------------- |
| `.`               | Matches any character except newline.          |
| `[]`              | User-defined character class.                  |
| `^`               | Asserts *starts with*.                         |
| `$`               | Asserts *ends with*.                           |
| `*`               | Zero or more occurrences of a character.       |
| `+`               | One or more occurences of a character.         |
| `?`               | Zero or one occurences of a character.         |
| `{}`              | Specified number of occurences of a character. |
| `\|`              | Used to implement `OR` logic.                  |
| `()`              | Capture, and grouping.                         |
### Character Class(es)
---
A character class defines a new character, as a range of acceptable characters that may be matched.

| Character Class | Description                            |
| --------------- | -------------------------------------- |
| `[0-9]`         | Any digit.                             |
| `[a-z]`         | Any lower-case alphabetical character. |
| `[a-zA-Z0-9]`   | Any alphanumeric character.            |
### Number of Occurrences
---
A character may be matched a specified number of times, sequentially, by appending an occurrence specifier to it.

| Range   | Description   |
| ------- | ------------- |
| `{3}`   | $n=1$         |
| `{2,}`  | $n >= 2$      |
| `{,5}`  | $n <= 5$      |
| `{1,4}` | $1 <= n <= 4$ |

*Note:* By default, a *RegEx* engine is *greedy*. This means, it will attempt to match as many occurrences as possible. To force it to be *lazy*, succeed any occurrence specifier with `?`.
### *Starts with, Ends with*
---
To assert that a pattern must exist at,
* the beginning of a text, begin the pattern with `^`.
* the end of a text, end the pattern with `$`.
### *Look ahead, Look behind*
---
A *Look-ahead* asserts the existence (or, lack thereof) of a specific pattern, after the actual pattern to match.

Similarly, a *Look-behind* makes a similar assertion, before the actual pattern to match.

|                | Location                | Description          |
| -------------- | ----------------------- | -------------------- |
| `(?<=` and `)` | Before pattern to match | Positive Look-behind |
| `(?<!` and `)` | Before pattern to match | Negative Look-behind |
| `(?=` and `)`  | After pattern to match  | Positive Look-ahead  |
| `(?!` and `)`  | After pattern to match  | Negative Look-ahead  |

*Note:* The pattern(s) asserted by *Look-ahead* and *Look-behind* are not captured, and consume zero length of the search string.
### Group(s)
---
A number of characters may be grouped using `(?:` and `)`.

Additionally, the `|` operator may be used to implement `OR` logic between a left-side and a right-side, within a grouping.

For example, `abc(?:123|456)` matches `abc123`, or `abc456`.
#### Capture Group(s)
---
A capture group is a special group, that captures a specific part of a pattern, that may later be referenced (e.g., in replacement text).

To form a capture group, surround part of a pattern with `(` and `)`.
## References
---
[1] Python Scripting Language, 3.X