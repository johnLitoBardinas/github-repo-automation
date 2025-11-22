from github import Github, Auth
import requests

TOKEN = "your_github_token_here"  # Replace with your GitHub Personal Access Token
auth = Auth.Token(TOKEN)
g = Github(auth=auth)
user = g.get_user()

DETACH_FORK_MUTATION = """
mutation($repoId: ID!) {
  detachForkFromNetwork(input: {repositoryId: $repoId}) {
    clientMutationId
  }
}
"""

for repo in user.get_repos():
    if repo.fork:
        print(f"Processing fork: {repo.name}")
        
        # Detach from fork network
        response = requests.post(
            'https://api.github.com/graphql',
            json={
                'query': DETACH_FORK_MUTATION,
                'variables': {'repoId': repo.raw_data['node_id']}
            },
            headers={'Authorization': f'Bearer {TOKEN}'}
        )
        
        if response.status_code == 200:
            print(f"  ✓ Detached from fork network")
        else:
            print(f"  ✗ Failed to detach: {response.json()}")
            continue
        
        # Try to make it private
        try:
            repo.edit(private=True)
            print(f"  ✓ Made private: {repo.name}")
        except Exception as e:
            if "Public forks can't be made private" in str(e):
                print(f"  ⚠ Cannot make private: {repo.name}")
                print(f"    GitHub doesn't allow public forks to be made private.")
                print(f"    To make it private, you need to:")
                print(f"    1. Delete the repository: {repo.html_url}")
                print(f"    2. Create a new private repository with the same name")
                print(f"    3. Push your code to the new repository")
            else:
                print(f"  ✗ Error making private: {e}")

print("\nDone!")