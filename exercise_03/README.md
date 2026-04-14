## Scenario
Your colleague was working on a change but has gone on vacation. Before going on vacation, they pushed their changes to a branch called `important_changes`. They need you to complete one small fix which they have already added, but that code is commented. You need to fetch their branch, uncomment the code, test it, and raise a PR so that we can get the very important release out on time.

### Learning Git Fetch
When a colleague pushes a new branch to the remote repository (GitHub), your local machine doesn't know about it yet. `git fetch` downloads the latest metadata and branch information from the remote without merging it into your local work.

1. **Update your local tracking information**
   Run the following command to see all branches available on the remote:
   ```bash
   git fetch origin
   ```

2. **Checkout the specific branch**
   Switch to the branch your colleague created:
   ```bash
   git checkout important_changes
   ```

3. **Uncomment the code**
   Open the relevant file, locate the commented-out fix, and uncomment it.

4. **Test your changes**
   Ensure the fix works as expected before proceeding.

5. **Commit the fix**
   Stage the file and commit the change:
   ```bash
   git add <file_name>
   git commit -m "uncomment and enable important fix"
   ```

6. **Push the changes**
   Push your work back to the remote repository:
   ```bash
   git push origin important_changes
   ```
