from github import Github, Auth

TOKEN = "your_github_token_here"  # Replace with your GitHub Personal Access Token
auth = Auth.Token(TOKEN)
g = Github(auth=auth)
user = g.get_user()

# Collect all forks
forks = [repo for repo in user.get_repos() if repo.fork]

if not forks:
    print("No forked repositories found!")
    exit(0)

print(f"Found {len(forks)} forked repositories:\n")
for i, repo in enumerate(forks, 1):
    print(f"{i:2}. {repo.full_name}")
    print(f"    URL: {repo.html_url}")
    print(f"    Private: {repo.private}")
    print()

print(f"\n⚠️  WARNING: This will DELETE all {len(forks)} forked repositories!")
print("This action CANNOT be undone.\n")

response = input("Type 'DELETE ALL FORKS' to confirm: ")

if response == "DELETE ALL FORKS":
    print(f"\nDeleting {len(forks)} repositories...\n")

    deleted_count = 0
    failed_count = 0
    permission_errors = []

    for i, repo in enumerate(forks, 1):
        try:
            repo.delete()
            print(f"✓ [{i}/{len(forks)}] Deleted: {repo.name}")
            deleted_count += 1
        except Exception as e:
            failed_count += 1
            error_msg = str(e)
            if "403" in error_msg or "admin rights" in error_msg.lower():
                print(f"✗ [{i}/{len(forks)}] Permission denied: {repo.name}")
                permission_errors.append(repo.name)
            else:
                print(f"✗ [{i}/{len(forks)}] Failed to delete {repo.name}: {e}")

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  ✓ Deleted: {deleted_count}")
    print(f"  ✗ Failed: {failed_count}")

    if permission_errors:
        print(f"\n⚠️  Permission Errors ({len(permission_errors)}):")
        print(f"Your token needs the 'delete_repo' scope.")
        print(f"Update your token at: https://github.com/settings/tokens")
        print(f"\nFailed repositories:")
        for repo_name in permission_errors:
            print(f"  - {repo_name}")

    print(f"{'='*60}")
else:
    print("\nCancelled. No repositories were deleted.")
