Comprehensive GIT Command Line Tutorial for Managing a Development Environment
Introduction
This tutorial aims to provide a thorough understanding of using Git from the command line. Git is a powerful version control system that helps developers manage and track changes in their code over time. We'll cover various essential commands, focusing on undoing commits, managing stashes, handling remotes, and other vital Git functionalities.

Basic Setup
Before diving into advanced topics, ensure you have Git installed on your system and have configured your username and email:

git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
Managing Commits
Undoing Commits
Undoing the Last Commit: To undo the most recent commit, keeping the changes in the working directory:

git reset --soft HEAD~1
Discarding the Last Commit: To discard the last commit and all changes:

git reset --hard HEAD~1
Amending a Commit: If you need to modify the last commit (e.g., correct a typo), you can do:

git commit --amend
This opens an editor where you can edit the commit message. If you've made any additional changes to the files, you can add them before running this command.

Managing Stashes
Stashing is useful when you need to switch branches without committing the current working state.

Creating a Stash:

git stash
Listing Stashes:

git stash list
Applying a Stash:

To apply the most recent stash and keep it in the stash list:

git stash apply
To apply a specific stash (e.g., stash@{1}):

git stash apply stash@{1}
To apply the most recent stash and remove it from the stash list:

git stash pop
Deleting a Stash:

To delete a specific stash (e.g., stash@{1}):

git stash drop stash@{1}
To clear all stashes:

git stash clear
Managing Remotes
Remotes are versions of your project that are hosted on the internet or network.

Viewing Remotes: List the remote connections you have to other repositories.

git remote -v
Adding a Remote Repository:

git remote add [remote-name] [remote-url]
Fetching from a Remote: Fetch branches and their respective commits from the remote repository.

git fetch [remote-name]
Pushing to a Remote: Push your branch to a remote repository.

git push [remote-name] [branch-name]
Pulling from a Remote: Fetch and integrate changes from the remote server to your working directory.

git pull [remote-name] [branch-name]
Removing a Remote:

git remote remove [remote-name]
Other Essential Commands
Checking Status:

git status
Viewing Commit History:

git log
Creating a Branch:

git branch [branch-name]
Switching Branches:

git checkout [branch-name]
Merging Branches:

git merge [branch-name]
Deleting a Branch:

git branch -d [branch-name]
Handling Merge Conflicts: Use a text editor to manually resolve conflicts, then:

git add [file-name]
git commit -m "Resolved merge conflict"
Conclusion
Git is a cornerstone tool for any developer. Understanding and efficiently using Git commands can significantly improve your development workflow. Remember, practice is key to mastering Git, so don't hesitate to experiment with these commands>
