# Exercise: Git Branching Operations

In this exercise, you will learn how to manage different lines of development using branches.

## 1. Create and Switch Branches (Checkout)
To create a new branch and switch to it immediately:
```bash
git checkout -b feature-login
```
*Note: You can also use the newer command `git switch -c feature-login`.*

To switch back to your main branch:
```bash
git checkout main
```

## 2. Rename a Branch
If you are currently on the branch you want to rename:
```bash
git branch -m new-feature-name
```
If you are on a different branch:
```bash
git branch -m old-name new-name
```

## 3. List Branches
To see all local branches and identify which one you are currently on:
```bash
git branch
```

## 4. Delete a Branch
Once a feature is merged or no longer needed, you can delete the branch.

To delete a branch that has been merged:
```bash
git branch -d new-feature-name
```

To force delete a branch (even if changes aren't merged):
```bash
git branch -D new-feature-name
```