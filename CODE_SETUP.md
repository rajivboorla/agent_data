
---- This removes it only from Git, not from your system.
git rm --cached .gitignore

| Task                                 | Command                                                     |
| ------------------------------------ | ----------------------------------------------------------- |
| Remove project `.gitignore` from Git | `git rm --cached .gitignore`                                |
| Use global ignore instead            | `git config --global core.excludesfile ~/.gitignore_global` |

removes file from tracking --> git rm --cached .gitignore
commit the removal --> git commit -m "Remove .gitignore from repository"
push the changes to repo -- > git push


