### Error when `git add`, `git rm` ...
```
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        deleted:    Use Responsive Design with Bootstrap Fluid Containers.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        Bootstrap.md

Hankyu (master *+) HTML5_CSS $ git rm 'Use Responsive Design with Bootstrap Flui                d Containers.md'
fatal: Unable to create 'C:/Users/Hankyu/Dropbox/_OnlineLectures/Web lectures/fr                eeCodeCamp/HTML5_CSS/.git/index.lock': File exists.
```
command prompt from repo directory:
```
cd .git
rm index.lock
```
Go back to the directory and try again.
