──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
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
* *modified*, if it has been tracked in the last commit, but changed.
* *deleted*, if it has been tracked in the last commit, but has been modified.

By default, new changes are unstaged. To stage changes,

```
git add PATH
```

To clear the current working directory (i.e., revert to unmodified `HEAD`),

```
git reset --hard
```

*Note:* `git reset --hard` does not remove *untracked* files.

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

To checkout to a specific commit,

```
git checkout [-b BRANCH-NAME] HASH
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
git merge BRANCH-NAME
```

To show the log,

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
To fetch the latest changes from a remote branch, without checking it out,

```
git fetch REMOTE-ALIAS REMOTE-BRANCH
```

*Note:* `git fetch` fetches the latest changes from the whole repository.

To checkout a remote branch, and setup a local branch to track it,

```
git checkout -b LOCAL-BRANCH REMOTE-ALIAS/REMOTE-BRANCH
```

For an already existing local branch, it can be setup to track a remote branch,

```
git branch -u REMOTE-ALIAS/REMOTE-BRANCH
```

*Note:* `git status` reveals if the local branch tracks a remote branch, and which.

To fetch and checkout the latest changes to a remote branch, that is being tracked by the current local branch,

```
git pull
```

Instead, to push a local branch, onto a remote branch,

```
git push REMOTE-ALIAS LOCAL-BRANCH:REMOTE-BRANCH [--force]
```

*Note:* To push the current local branch, you may use `HEAD` instead of the branch's name.

To rebase the current branch onto a remote branch,

```
git rebase REMOTE-ALIAS/REMOTE-BRANCH
```
## References
---
[1] ...