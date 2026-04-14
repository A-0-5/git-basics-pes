## Git Basics
Welcome to this hands-on repo. Here you will learn more about Git, how to get started, and use Git in certain basic scenarios.

## Repository Setup

There are two primary ways to set up a Git repository depending on your starting point.

### 1. Creating a Repository from Scratch in Github and Cloning it
1. Go to Github and create you repo

```bash
# Clone the repository to your local machine
git clone <repository-url>

# Navigate into the newly created directory
cd <repository-name>
```

### 2. Initializing a Repository (Existing Code)
Use this method if you have a local project folder that is not yet tracked by Git and you want to start version controlling it and push it to a remote server.

```bash
# Navigate to your project folder
cd /path/to/your/existing-code

# Initialize the local directory as a Git repository
git init

# Add files, commit them, and push to a remote
git add .
git commit -m "Initial commit"
git remote add origin <repository-url>
git branch -M main
git push -u origin main
```