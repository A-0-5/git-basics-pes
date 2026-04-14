## Scenario
You just joined a company and you are asked to fix a simple bug you need to first author your change, then commit it and push it to your branch and raise a pull request.

1. First let us create a new branch 
   ```bash
   git checkout -b fix-typo
   ```
2. In the `hello_world.py` there is a typo in the 4th line where `stmdard libary` should be `standard library` lets fix that.
3. Save it and review your change locally in vscode
4. Commit the change, there are many ways to do it lets try all of them
   1. `git commit -am "fix typo in hello world"`
   2. ```bash
      git add hello_world.py
      git commit -m "fix typo in hello world"
      ```
   3. Using the vscode UI
5.  `git push --set-upstream origin remote-branch-name`