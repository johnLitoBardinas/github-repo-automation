from github import Github, Auth

TOKEN = "your_github_token_here"  # Replace with your GitHub Personal Access Token
auth = Auth.Token(TOKEN)
g = Github(auth=auth)
user = g.get_user()

# Collect all public repositories (excluding forks)
public_repos = [repo for repo in user.get_repos() if not repo.private]

if not public_repos:
    print("No public repositories found!")
    exit(0)

# Separate forks and non-forks
public_forks = [repo for repo in public_repos if repo.fork]
public_non_forks = [repo for repo in public_repos if not repo.fork]

print(f"Found {len(public_repos)} public repositories:\n")

if public_non_forks:
    print(f"✓ Can be made private ({len(public_non_forks)}):")
    for repo in public_non_forks:
        print(f"  - {repo.full_name}")
    print()

if public_forks:
    print(f"⚠ Public forks (CANNOT be made private) ({len(public_forks)}):")
    for repo in public_forks:
        print(f"  - {repo.full_name}")
    print(f"\nNote: GitHub doesn't allow public forks to be made private.")
    print(f"These will be skipped.\n")

if not public_non_forks:
    print("\nNo repositories can be made private (all are forks).")
    exit(0)

print(f"\nThis will make {len(public_non_forks)} repositories private.\n")
response = input("Type 'MAKE PRIVATE' to confirm: ")

if response == "MAKE PRIVATE":
    print(f"\nMaking repositories private...\n")

    success_count = 0
    failed_count = 0
    skipped_count = len(public_forks)

    for i, repo in enumerate(public_non_forks, 1):
        try:
            repo.edit(private=True)
            print(f"✓ [{i}/{len(public_non_forks)}] Made private: {repo.name}")
            success_count += 1
        except Exception as e:
            failed_count += 1
            print(f"✗ [{i}/{len(public_non_forks)}] Failed: {repo.name} - {e}")

    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  ✓ Made private: {success_count}")
    print(f"  ✗ Failed: {failed_count}")
    if skipped_count > 0:
        print(f"  ⊘ Skipped (public forks): {skipped_count}")
    print(f"{'='*60}")
else:
    print("\nCancelled. No repositories were modified.")
