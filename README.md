# GitHub Repository Management Scripts

A collection of Python scripts to manage your GitHub repositories: delete forks, make repositories private, and detach from fork networks.

## Requirements

- Python 3.9.7
- PyGithub library
- requests library

## Installation

1. Clone or download this repository

2. Install dependencies:
```bash
pip install PyGithub requests
```

Or if using a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install PyGithub requests
```

## GitHub Token Setup

All scripts require a GitHub Personal Access Token with appropriate permissions.

### Quick Setup:

1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Select required scopes:
   - ✅ `repo` (required for all scripts)
   - ✅ `delete_repo` (required for delete_forks.py only)
4. Copy the generated token
5. Replace `"your_github_token_here"` in each script with your token

**📖 Need detailed instructions?** See [HOW_TO_GENERATE_GITHUB_ACCESS_TOKEN.md](HOW_TO_GENERATE_GITHUB_ACCESS_TOKEN.md) for a complete step-by-step guide with troubleshooting tips and security best practices.

### Configuring the Scripts:

Open each script and replace the placeholder token:

```python
TOKEN = "your_github_token_here"  # Replace with your actual token
```

**⚠️ Security Warning:** Never commit your actual token to version control!

## Scripts Overview

### 1. delete_forks.py

Deletes all forked repositories from your GitHub account.

**Usage:**
```bash
python delete_forks.py
```

**What it does:**
- Lists all forked repositories in your account
- Shows repository names, URLs, and privacy status
- Asks for confirmation before deleting
- Deletes all forks after typing `DELETE ALL FORKS`

**Required Token Permissions:**
- `repo`
- `delete_repo`

---

### 2. make_repos_private.py

Makes all public repositories private.

**Usage:**
```bash
python make_repos_private.py
```

**What it does:**
- Lists all public repositories
- Separates forks from non-forks
- Makes non-fork repositories private
- Skips public forks (GitHub limitation: public forks cannot be made private)

**Note:** Public forks cannot be converted to private repositories due to GitHub's policy. To make a public fork private, you must delete it and recreate it as a new private repository.

**Required Token Permissions:**
- `repo`

---

### 3. remove_to_fork_network.py

Detaches forks from their parent network and attempts to make them private.

**Usage:**
```bash
python remove_to_fork_network.py
```

**What it does:**
- Finds all forked repositories
- Detaches them from the fork network using GitHub's GraphQL API
- Attempts to make them private
- Shows helpful error messages if conversion fails

**Note:** Even after detaching, GitHub still doesn't allow public forks to be made private. This script will inform you which repositories need manual intervention.

**Required Token Permissions:**
- `repo`

---

## Common Issues

### "Bad credentials" Error
Your token is invalid or expired. Generate a new token and update the scripts.

### "Must have admin rights to Repository" Error
Your token doesn't have the `delete_repo` scope. Update your token permissions.

### "Public forks can't be made private" Error
This is a GitHub limitation. To convert a public fork to private:
1. Delete the fork
2. Create a new private repository
3. Push your code to the new repository

## Safety Features

All scripts include:
- ✅ Preview of what will be affected
- ✅ Confirmation prompts before destructive actions
- ✅ Detailed progress reporting
- ✅ Error handling with helpful messages
- ✅ Summary statistics after completion

## Example Workflow

To clean up your GitHub account:

1. **Delete all forks:**
   ```bash
   python delete_forks.py
   ```

2. **Make remaining repos private:**
   ```bash
   python make_repos_private.py
   ```

## Environment Details

These scripts were developed and tested with:
- Python 3.9.7
- PyGithub 2.x
- macOS (but should work on Windows/Linux)

## License

Free to use and modify for your own purposes.

## Disclaimer

**⚠️ Warning:** These scripts perform destructive operations (deleting repositories, changing visibility). Always:
- Review the preview before confirming
- Ensure you have backups of important code
- Test with a few repositories first if unsure
- Double-check which repositories will be affected

The author [JLBardinas](www.jlbardinas.com) is not responsible for any data loss resulting from the use of these scripts.
