import pandas as pd
import requests

# Replace with your GitHub Personal Access Token
GITHUB_TOKEN = ''

# Function to fetch issues for a repository with keyword filter
def get_issues(owner, repo, keyword_filter):
    url = f'https://api.github.com/repos/{owner}/{repo}/issues'
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    params = {'state': 'all', 'q': keyword_filter}  # Adding the keyword filter

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch issues for {owner}/{repo}")
        return []

# Read the CSV file
df = pd.read_csv('filtered_repositories.csv')

# Define the keyword filter
keyword_filter = 'label:"feature request" OR label:"enhancement"'

# Create an empty DataFrame to store the filtered issues
filtered_issues_df = pd.DataFrame(columns=['Repository', 'Issue Title'])

# Iterate through each row in the CSV and fetch filtered issues
for index, row in df.iterrows():
    owner = row['owner']
    repo = row['repo']

    issues = get_issues(owner, repo, keyword_filter)

    # Process filtered issues and add them to the DataFrame
    for issue in issues:
        filtered_issues_df = filtered_issues_df.append({'Repository': f'{owner}/{repo}', 'Issue Title': issue['title']}, ignore_index=True)

# Save the filtered issues to a CSV file
filtered_issues_df.to_csv('filtered_issues.csv', index=False)

