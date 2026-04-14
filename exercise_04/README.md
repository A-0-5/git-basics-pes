## Scenario
Its vacation season , another team mate of yours is on vacation and wants you to add some more comments to a file in their branch `john_does_vacation` and raise a PR. Before going on vacation they mentioned to you that their branch was a bit out of date with main and had to update other wise the PR cant be merged due to conflicts. So your task is now to checkout john doe's branch , make the necessary changes (uncomment code) and raise a PR.

### 1. Get the branch
```bash
git fetch origin
git checkout john_does_vacation
```

### 2. Update the branch with Main
Since the branch is out of date, you need to bring in the latest changes from `main`. There are two common ways to do this:

#### Approach A: Git Pull with Merge (Default)
This creates a new "merge commit" that ties the history of `main` and your branch together. It is non-destructive and preserves the chronological history.
```bash
git pull origin main
```
*If there are conflicts, resolve them, then `git add` and `git commit`. OR you can also do `git merge --continue` *

#### Approach B: Git Pull with Rebase (Cleaner History)
This moves your branch's unique commits to the "tip" of the latest `main` branch. It results in a linear history without extra merge commits.
```bash
git pull --rebase origin main
```
*If there are conflicts, resolve them, then run `git rebase --continue`.*

### 3. Make Changes and Push
1. Add the requested comments to the file.
2. Commit your changes:
   ```bash
   git add <file_name>
   git commit -m "add comments requested by John"
   git push origin john_does_vacation
   ```
   *(Note: If you rebased, you might need to use `git push --force-with-lease` if the branch was already on the remote).*
