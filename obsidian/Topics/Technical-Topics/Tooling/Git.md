──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*

- [[#`Git` Local|`Git` Local]]
- [[#`Git` Remote|`Git` Remote]]
## Content
---
#### `Git` Local
---
To initialize a directory as a git repository,

```
git init PATH
```

To view changes in the working directory,

```
git status
```

*Note:* `git status` also mentions the current branch.

If a file appears in the output of the `status` command, it may have been:
* *untracked*, if it is newly created.
* *added*, if it is newly created, but tracked.
* *modified*, if it has been tracked in the last commit, but has been modified.
* *deleted*, if it has been tracked in the last commit, but has been deleted.

By default, new changes are unstaged. To stage changes,

```
git add PATH
```

To clear the current working directory (i.e., revert to unmodified `HEAD`),

```
git reset --hard
```

*Note:* `git reset --hard` does not remove *untracked* files.

To remove untracked files

```
git clean -d -f [-x]

Options:
	x - Remove ignored files as well.
```

To stash the current working directory (i.e., push onto a stack),

```
git stash
```

*Note:* To pop stashed changes, use `git stash pop`.

To commit the current working directory,

```
git commit -m "MESSAGE"
```

To create a new branch,

```
git branch BRANCH
```

To switch to a branch,

```
git switch BRANCH
```

To checkout to a specific commit (or, branch),

```
git checkout [-b BRANCH] HASH

Options:
	b - Create and switch to new BRANCH.
```

*Note:* If this commit is the `HEAD` commit of a branch, you may specify the branch's name instead of the hash of the commit.

To cherry-pick a specific commit, onto the current branch,

```
git cherry-pick HASH
```

To rebase the current branch onto a local branch,

```
git rebase BRANCH
```

To merge a branch, into the current branch,

```
git merge BRANCH
```

To show the log (i.e., in CLI),

```
git log [--all] [--oneline] [--decorate] [--graph]

Options:
	all - Display all commits, usually ordered by date-time, not just ones relevant to the graph of the current branch.
	oneline - Display commits on a single-line
	decorate - Display references (e.g., branch names), alongside commit hash(es).
	graph - Display commits in a graph format.
```
#### `Git` Remote
---
In all commands, unless otherwise specified, a remote branch is referenced as `REMOTE-ALIAS/REMOTE-BRANCH`.

To fetch the latest changes from a remote branch, without checking it out,

```
git fetch REMOTE-ALIAS REMOTE-BRANCH
```

To checkout a remote branch, and setup a (new) local branch to track it,

```
git checkout -b LOCAL-BRANCH REMOTE-ALIAS/REMOTE-BRANCH
```

For an already existing local branch, it can be setup to track a remote branch,

```
git branch -u REMOTE-ALIAS/REMOTE-BRANCH
```

*Note:* `git status` reveals if the local branch tracks a remote branch, and which.

If the current local branch tracks a remote branch, then, to fetch and checkout the latest changes from the remote branch into the current local branch,

```
git pull
```

If the current local branch tracks a remote branch, then, to push the latest changes from the current local branch onto the remote branch,

```
git push [--force]
```

In general, to push a local branch, onto a remote branch,

```
git push REMOTE-ALIAS LOCAL-BRANCH:REMOTE-BRANCH [--force]
```

*Note:* To push the current local branch, you may use `HEAD` instead of the branch's name.