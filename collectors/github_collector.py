import requests
import os
from dotenv import load_dotenv
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def fetch_commits(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    headers = {
        "Authorization" : f"Bearer {GITHUB_TOKEN}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"GitHub API error: {response.status_code}")
    
    data = response.json()

    commits = []

    for item in data:
        commits.append({
            "id": item["sha"],
            "message" : item["commit"]["message"],
            "author" : item["commit"]["author"]["name"],
            "date" : item["commit"]["author"]["date"]

        })

    return commits


def fetch_prs(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls?state=all"

    headers = {
        "Authorization" : f"Bearer {GITHUB_TOKEN}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"GitHub API error: {response.status_code}")
    
    data = response.json()

    pull_requests = []

    for item in data:
        pull_requests.append({
            "id": item["id"],
            "title": item["title"],
            "author": item["user"]["login"],  
            "state": item["state"],           
            "created_at": item["created_at"],
            "updated_at": item["updated_at"]
        })

    return pull_requests


def fetch_issues(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=all"

    headers = {
        "Authorization" : f"Bearer {GITHUB_TOKEN}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"GitHub API error: {response.status_code}")
    
    data = response.json()

    issues = []

    for item in data:
        issues.append({
            "id": item["id"],
            "title": item["title"],
            "author": item["user"]["login"],
            "state": item["state"],  
            "created_at": item["created_at"],
            "updated_at": item["updated_at"]
        })

    return issues