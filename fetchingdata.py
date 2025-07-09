import requests
import pandas as pd
from time import sleep

# Step 1: GitHub token and username
GITHUB_TOKEN = "write ur token here"  
username = "microsoft"  # Change to any username/org

# Step 2: Headers
headers = {
    'Accept': 'application/vnd.github.mercy-preview+json',
    'Authorization': f'token {GITHUB_TOKEN}'
}
print("hello")
# Step 3: Fetch repos
url = f"https://api.github.com/users/{username}/repos?per_page=100"
response = requests.get(url, headers=headers)
print(response)

if response.status_code != 200:
    print("Failed to fetch repositories.")
    exit()

repos = response.json()


# Step 4: Prepare list for all repo data
data = []
print("mir")
# Step 5: Loop through each repo
for repo in repos:
    repo_name = repo["name"]
    
    # Fetch topics
    topics_url = f"https://api.github.com/repos/{username}/{repo_name}"
    topic_response = requests.get(topics_url, headers=headers)
    topics = topic_response.json().get("topics", []) if topic_response.status_code == 200 else []

    # Fetch contributors count
    contributors_url = f"https://api.github.com/repos/{username}/{repo_name}/contributors"
    contrib_response = requests.get(contributors_url, headers=headers)
    
    if contrib_response.status_code == 200:
        contributors = len(contrib_response.json())
    else:
        contributors = 0

    # Final repo data
    repo_info = {
        "Name": repo["name"],
        "Stars": repo["stargazers_count"],
        "Forks": repo["forks_count"],
        "Watchers": repo["watchers_count"],
        "Language": repo["language"],
        "Description": repo["description"],
        "Topics": ", ".join(topics),
        "Contributors": contributors,
        "Last_Push": repo["pushed_at"]
    }

    data.append(repo_info)
    
   
    
print("done")
# Step 6: Save to CSV
df = pd.DataFrame(data)
df.to_csv("github_repos.csv", index=False)
print("Data saved to github_repos.csv")
