# Merge Conflicts

## What is a merge conflict?

A merge conflict happens when two branches have made changes to the same line in a file or when one branch deletes a file that another branch is modifying.

## How to Resolve Merge Conflicts?

1. Git will mark the conflict in the file. Look for the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
2. Edit the file to resolve the conflict.
3. Stage the resolved file using `git add <filename>`.
4. Commit the merge with `git commit`.
