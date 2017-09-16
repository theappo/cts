# INSTRUCTION

## Basis

- We are going to use [Python 3.6.2][Python 3.6.2] as our development language.

- We are going to use [PEP 8][PEP 8] naming conventions.

- Here are two great python IDE that I recommend: [PyCharm][PyCharm], [PyDev][PyDev].

- Also, Here are a few good text editors that you may want to use: [sublime text 3][sublime text 3], VIM and [Notepad++][Notepad++].

## Workflow

Setup:

1. In the terminal/Shell, go to the directory where you want to place the team project, then use the following command to clone our project:

	`git clone https://github.com/whuang001/coding-turk-system.git`

2. then use the following command to see local branch:

	`git branch`

3. you should only see a *master* branch. Now, run following command to see all remote branch:

	`git branch -r`

4. then fetch the `develop` branch and your own branch:

	`git fetch origin develop:develop`

	`git fetch origin your_branch:your_branch`

5. use `git branch` to see all local branch, you should see your branch, develop branch and the master branch.

6. go to the develop branch by doing `git checkout develop`, set upstream branch:

	`git branch --set-upstream-to origin/develop`

	and got to your branch do the same thing again:

	`git branch --set-upstream-to origin/your_branch`

---

How to work?

- Your branch belongs to your self, here is where you work. **However, do not work on either develop branch or master branch.**

	1. Use `git checkout your_branch` to switch to your branch. Use `git branch` to see where you are.

- When you finish a model (design and implementation, including testing), you have to merge your code to the develop branch, by doing the following things:

	1. `git checkout develop`

	2. `git pull`

	3. `git merge your_branch`

	4. `git push`. If conflict happen, solve conflict and commit, then do `git push`

## Version control

You can use `Reset`, `Revert` to control your code's version, and you should read [this][reset/revert] before you are using them.

Tips:

- you can `reset` your branch only before a `push`.

- you have to use `revert` after a `push`.


## Useful git commands

Reset local repository branch to be just like remote repository HEAD:

	git fetch origin
	git reset --hard origin/master

## Database

To be determined.

## Mark down

- Our document is written in [Markdown][Markdown]. You can learn mark down [here][here].

## Bug

- Use [issue][issue] to post a bug.

## Slack

- [We're on Slack! Join us!][Join us]




[Python 3.6.2]:https://www.python.org
[PEP 8]:https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles
[PyCharm]:https://www.jetbrains.com/pycharm/
[PyDev]:http://www.pydev.org
[sublime text 3]:https://www.sublimetext.com/3
[Notepad++]:https://notepad-plus-plus.org
[reset/revert]:https://www.atlassian.com/git/tutorials/resetting-checking-out-and-reverting
[Markdown]:http://kirkstrobeck.github.io/whatismarkdown.com/
[here]:https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
[issue]:https://github.com/whuang001/coding-turk-system/issues
[Join us]:https://join.slack.com/t/csc322-2017/shared_invite/enQtMjQxNTYwMzQ1Njk2LTE4NjYwOTY2ZjYxNTYwNzA5NDljYTlhZDM5NTcwNTY2NTllOTVmOWFhYmRlZmU5NTgxZmIyMzQ5OTk3YzM3NDE