# How to Generate a GitHub Personal Access Token

This guide will walk you through creating a GitHub Personal Access Token required for using the repository management scripts.

## Table of Contents
- [What is a Personal Access Token?](#what-is-a-personal-access-token)
- [Step-by-Step Guide](#step-by-step-guide)
- [Required Permissions](#required-permissions)
- [Security Best Practices](#security-best-practices)
- [Troubleshooting](#troubleshooting)

---

## What is a Personal Access Token?

A Personal Access Token (PAT) is like a password that gives applications access to your GitHub account. It's more secure than using your actual password because:
- You can limit what the token can do (scopes)
- You can revoke it anytime without changing your password
- You can create multiple tokens for different purposes
- It can have an expiration date

---

## Step-by-Step Guide

### Step 1: Log into GitHub

1. Go to [github.com](https://github.com)
2. Sign in to your account

### Step 2: Access Token Settings

1. Click your **profile picture** in the top-right corner
2. Click **Settings**
3. Scroll down to the bottom of the left sidebar
4. Click **Developer settings**
5. Click **Personal access tokens**
6. Click **Tokens (classic)**

**Direct link:** https://github.com/settings/tokens

### Step 3: Generate New Token

1. Click the **"Generate new token"** button
2. Select **"Generate new token (classic)"**
3. You may be asked to confirm your password - enter it and click **Confirm**

### Step 4: Configure Your Token

#### Token Name (Note)
Give your token a descriptive name so you remember what it's for:
- Example: `Repository Management Scripts`
- Example: `Cleanup Scripts - MacBook`
- Example: `Fork Deletion Tool`

#### Expiration
Choose how long the token should be valid:
- **30 days** (recommended for temporary use)
- **60 days**
- **90 days**
- **Custom** (set your own date)
- **No expiration** (not recommended for security reasons)

⚠️ **Recommendation:** Use 30-90 days and regenerate when needed. This limits exposure if the token is compromised.

#### Select Scopes (Permissions)

This is the most important part! Check the following boxes:

**For all scripts:**
- ✅ **`repo`** - Full control of private repositories
  - This automatically checks all sub-items under it
  - Required for reading repository information and making them private

**For delete_forks.py only:**
- ✅ **`delete_repo`** - Delete repositories
  - Required only if you want to delete repositories
  - Scroll down to find this option (it's separate from `repo`)

**What each script needs:**
```
delete_forks.py          → repo + delete_repo
make_repos_private.py    → repo
remove_to_fork_network.py → repo
```

#### Screenshot of Required Scopes

```
Select scopes

[ ] repo                           ← CHECK THIS
    [x] repo:status
    [x] repo_deployment
    [x] public_repo
    [x] repo:invite
    [x] security_events

[ ] workflow
[ ] write:packages
[ ] read:packages

[ ] delete_repo                    ← CHECK THIS (for delete_forks.py)

[ ] notifications
...
```

### Step 5: Generate the Token

1. Scroll to the bottom
2. Click the green **"Generate token"** button
3. **IMPORTANT:** Your token will be displayed **only once**!

### Step 6: Copy Your Token

You'll see a green box with your token that looks like:
```
ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

1. Click the **copy icon** (📋) to copy the token
2. **Save it immediately** in a secure location:
   - Password manager (recommended)
   - Secure note on your computer
   - Encrypted file

⚠️ **WARNING:** You cannot see this token again! If you lose it, you'll need to generate a new one.

---

## Required Permissions

### Minimum Permissions by Script

| Script | `repo` | `delete_repo` |
|--------|--------|---------------|
| `delete_forks.py` | ✅ Required | ✅ Required |
| `make_repos_private.py` | ✅ Required | ❌ Not needed |
| `remove_to_fork_network.py` | ✅ Required | ❌ Not needed |

### Permission Descriptions

**`repo` scope includes:**
- Read repository information
- Create and edit repositories
- Change repository settings (including privacy)
- Access both public and private repositories

**`delete_repo` scope:**
- Delete repositories
- This is a separate permission for safety
- Only needed for deletion operations

---

## Security Best Practices

### ✅ DO:

1. **Use descriptive names** for tokens so you know what they're for
2. **Set expiration dates** (30-90 days is good)
3. **Only grant necessary permissions** (don't check every box)
4. **Store tokens securely** (password manager, encrypted file)
5. **Regenerate tokens periodically**
6. **Revoke tokens immediately** if compromised
7. **Use different tokens** for different purposes
8. **Keep tokens private** - never share them

### ❌ DON'T:

1. **Never commit tokens to Git** (add to .gitignore)
2. **Don't share tokens** with others
3. **Don't post tokens** in issues, forums, or chat
4. **Don't use tokens in public repositories**
5. **Don't grant more permissions** than needed
6. **Don't leave tokens** without expiration
7. **Don't reuse tokens** across multiple applications

### Protecting Your Token in Scripts

**Bad:**
```python
# main.py - committed to Git
TOKEN = "ghp_actualTokenHere123456789"  # ❌ NEVER DO THIS
```

**Good - Option 1: Environment Variable**
```python
# main.py
import os
TOKEN = os.environ.get('GITHUB_TOKEN')
```

```bash
# In your terminal
export GITHUB_TOKEN="ghp_actualTokenHere123456789"
python delete_forks.py
```

**Good - Option 2: Config File (.gitignore'd)**
```python
# config.py (added to .gitignore)
GITHUB_TOKEN = "ghp_actualTokenHere123456789"

# main.py
from config import GITHUB_TOKEN
```

```gitignore
# .gitignore
config.py
*.env
```

---

## Using Your Token

### In the Scripts

1. Open the script file (e.g., `delete_forks.py`)
2. Find this line:
```python
TOKEN = "your_github_token_here"
```
3. Replace `your_github_token_here` with your actual token:
```python
TOKEN = "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
4. Save the file
5. Run the script

### Example
```python
# Before
TOKEN = "your_github_token_here"

# After
TOKEN = "ghp_1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t"
```

---

## Managing Your Tokens

### View All Tokens
1. Go to https://github.com/settings/tokens
2. You'll see all your active tokens

### Regenerate a Token
1. Find your token in the list
2. Click **Regenerate token**
3. Copy the new token
4. Update it in your scripts

### Revoke a Token
1. Find your token in the list
2. Click **Delete**
3. Confirm deletion
4. The token will stop working immediately

---

## Troubleshooting

### "Bad credentials" Error
**Problem:** Your token is invalid or expired

**Solutions:**
- Check if you copied the entire token (they're long!)
- Verify the token hasn't expired
- Make sure there are no extra spaces
- Generate a new token if needed

### "Must have admin rights to Repository" Error
**Problem:** Missing `delete_repo` permission

**Solutions:**
1. Go to https://github.com/settings/tokens
2. Click your token name
3. Check the `delete_repo` box
4. Click **Update token**
5. You may need to regenerate the token

### "Validation Failed" or 403 Forbidden
**Problem:** Missing required permissions

**Solutions:**
1. Check which script you're running
2. Verify you have the `repo` scope enabled
3. For `delete_forks.py`, also enable `delete_repo`
4. Regenerate token with correct permissions

### Token Not Working After Setup
**Checklist:**
- [ ] Token is copied completely (no spaces, no truncation)
- [ ] Token is not wrapped in quotes twice: `"ghp_xxx"` not `"'ghp_xxx'"`
- [ ] Token hasn't expired
- [ ] Required scopes are checked
- [ ] You're logged into the correct GitHub account

---

## Token Expiration Reminder

When your token expires, you'll get authentication errors. To fix:

1. Go to https://github.com/settings/tokens
2. Find your expired token (it will show as expired)
3. Click **Regenerate token**
4. Copy the new token
5. Update it in your scripts

**Pro tip:** Set a calendar reminder a few days before expiration!

---

## FAQ

**Q: Can I use the same token for multiple scripts?**
A: Yes, as long as it has all the required permissions.

**Q: What happens if someone gets my token?**
A: They can access your repositories with the permissions you granted. Revoke it immediately at https://github.com/settings/tokens

**Q: Can I create multiple tokens?**
A: Yes! You can create as many as you need for different purposes.

**Q: Do tokens expire automatically?**
A: Only if you set an expiration date. Tokens without expiration last forever (until revoked).

**Q: Can I see my token again after creating it?**
A: No, GitHub only shows it once. If you lose it, generate a new one.

**Q: Will regenerating a token break my scripts?**
A: Yes, you'll need to update the token in your scripts with the new value.

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────┐
│         GitHub Token Quick Reference            │
├─────────────────────────────────────────────────┤
│ URL: https://github.com/settings/tokens         │
│                                                  │
│ For delete_forks.py:                            │
│   ✅ repo                                        │
│   ✅ delete_repo                                 │
│                                                  │
│ For make_repos_private.py:                      │
│   ✅ repo                                        │
│                                                  │
│ For remove_to_fork_network.py:                  │
│   ✅ repo                                        │
│                                                  │
│ Token format: ghp_xxxxx...                      │
│ Length: ~40 characters                           │
│ Recommended expiration: 30-90 days              │
└─────────────────────────────────────────────────┘
```

---

## Additional Resources

- [GitHub: Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [GitHub: Token scopes explained](https://docs.github.com/en/developers/apps/building-oauth-apps/scopes-for-oauth-apps)
- [GitHub: Reviewing your authorized applications](https://github.com/settings/applications)

---

**Need Help?**
If you're still having issues, check the error message carefully - it usually tells you exactly what's wrong (missing permissions, expired token, etc.).
