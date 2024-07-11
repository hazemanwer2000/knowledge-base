──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
A *regular expression (RegEx)* is a sequence of characters that specifies a search pattern. A *RegEx engine* is an application, responsible for parsing and recognizing a *RegEx* in text.

Every engine has its own flavor of *RegEx* syntax. This document will rely on *Python*'s *RegEx* flavor (i.e., its `re` built-in module).
### Special Characters
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
| `\|`              | Either, or.                                    |
| `()`              | Capture, and grouping.                         |
### Character Classes
---
A character class defines a new character, as a range of acceptable characters that may be matched.

| Character Class | Description                            |
| --------------- | -------------------------------------- |
| `[0-9]`         | Any digit.                             |
| `[a-z]`         | Any lower-case alphabetical character. |
| `[a-zA-Z0-9]`   | Any alphanumeric character.            |
### Number of Occurrences
---
A character may be matched a specified number of times, sequentially.

| Range   | Description   |
| ------- | ------------- |
| `{3}`   | $n=1$         |
| `{2,}`  | $n >= 2$      |
| `{,5}`  | $n <= 5$      |
| `{1,4}` | $1 <= n <= 4$ |
## References
---
[1] ...