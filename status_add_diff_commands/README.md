# Exercise: Git Status and Diff

In this exercise, you will learn how to track changes in your repository using `git status` and `git diff`.

## 1. Check the Status
Start by checking the current state of your repository:
```bash
git status
```

## 2. Track Additions
Create a new file and see how Git identifies "untracked" files:
```bash
echo "Hello Git" > exercise.txt
git status
```
Now, stage the file and check the status again:
```bash
git add exercise.txt
git status
```

## 3. View Changes (Diff)
Modify the file to see what has changed before staging:
```bash
echo "Learning about diffs" >> exercise.txt
git diff
```
*Note: `git diff` shows changes in your working directory that are not yet staged.*

## 4. Track Deletions
Delete a file and see how Git tracks the removal:
```bash
rm exercise.txt
git status
```
To stage the deletion, run:
```bash
git add exercise.txt
git status
```