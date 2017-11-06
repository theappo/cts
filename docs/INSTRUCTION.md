# INSTRUCTION

## Basis

- We are going to use [Python 3.6.2][Python 3.6.2] as our development language.

- We are going to use [PEP 8][PEP 8] naming conventions.

- Here are two great python IDE that I recommend: [PyCharm][PyCharm], [PyDev][PyDev].

- Also, Here are a few good text editors that you may want to use: [sublime text 3][sublime text 3], VIM and [Notepad++][Notepad++].

## Workflow

Setup:

1. In the terminal/Shell, go to the directory where you want to place the team project, then use the following command to clone our project:

	`git clone https://github.com/whuang001/cts.git`

2. change directory to `cts` or `coding-turk-system`then use the following command to see local branch:

	`git branch`

3. you should only see a *master* branch. Now, run following command to see all remote branch:

	`git branch -r`

4. then fetch the develop branch and your own branch:

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
	
- You can update your branch to match develop branch anytime

	1. `git checkout develop`
	
	2. `git pull`
	
	3. `git checkout your_branch`
	
	4. `git merge develop`

## Version control

You can use `Reset`, `Revert` to control your code's version, and you should read [this][reset/revert] before you are using them.

Tips:

- you can `reset` your branch only before a `push`.

- you have to use `revert` after a `push`.


## Useful git commands

Reset local repository branch to be just like remote repository HEAD:

	git fetch origin
	git reset --hard origin/branch_name

## Database

I decide to use MariaDB as out relational database management system. I will tech you how to install MariaDB when we need it.

**GateWay.py** require `MariaDB` and `Python` installed in your computer.
Additionally, you need to install a pure-Python MySQL client library, `PyMySQL`.

To avoid setting environment variable manually, I suggest that using `pip3` to install `PyMySQL`:

1. If you installed python via brew, go to step 3.

2. If you installed python via official website, and you don't have `pip3` installed, run below command to install `pip3`:

	`sudo easy_install pip3`(mac)
	`sudo apt-get install pip3`(linux)

pip `MAY` installed in path /Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg, since this is the default python path for MACOX.

3. Install `PyMySQL` via `pip3`:

	`sudo pip3 install PyMySQL`

4. Test `PyMySQL` install correctly:

- int terminal/shell, run:

	`python 3`

- then run:

	`import pymysql`

**YOU SHOULD RECEIVE NO ERROR.**

==========================================================================================

For brewed Python, modules installed with pip or python setup.py install will be installed to the (brew --prefix)/lib/pythonX.Y/site-packages directory (explained above). Executable Python scripts will be in $(brew --prefix)/bin.

The system Python may not know which compiler flags to set in order to build bindings for software installed in Homebrew so you may need to run:

	CFLAGS=-I$(brew --prefix)/include LDFLAGS=-L$(brew --prefix)/lib pip install <package>

===========================================================================================

**You have to manually restore the cts database by doing follow:**

	mysql -u root cts < backup-file.sql

**You can back up cts by command**

	mysqldump -u root cts > backup-file.sql

==========================================================================================

**every one should have a root user with an empty password**

## Setting your git username and email address

For peoper who not yet set a global git username and a email address for their computer, run:

- Set a Git username:

	`git config --global user.name your_name`
	
- Set an email address in Git, please use your github email address:

	`git config --global user.email your_email`
	
To check whether git username and email configuration, you can run:

	git config --list


## Mark down

- Our documents are written in [Markdown][Markdown]. You can learn mark down [here][here].

- I recommend you use [sublime text 3][sublime text 3] as a Markdown editor.

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
