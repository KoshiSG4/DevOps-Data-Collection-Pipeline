import requests
import os
from datetime import datetime, timezone
from dotenv import load_dotenv
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def fetch_commits(owner, repo, source):
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
            "name": "commit",
            "status": None,
            "created_at": item["commit"]["author"]["date"],
            "updated_at": item["commit"]["author"]["date"],
            "metadata": {
                "message": item["commit"]["message"],
                "author": item["commit"]["author"]["name"]
            }

        })

    return {
        "source": f"{source}",
        "entity": "commits",
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "data": commits
    }


def fetch_prs(owner, repo, source):
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
            "name": item["title"],
            "status": item["state"],           
            "created_at": item["created_at"],
            "updated_at": item["updated_at"],
            "metadata": {
                "author": item["user"]["login"]
            }
        })

    return {
        "source": f"{source}",
        "entity": "pull_requests",
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "data": pull_requests
    }


def fetch_issues(owner, repo, source):
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
            "name": item["title"],
            "status": item["state"],  
            "created_at": item["created_at"],
            "updated_at": item["updated_at"],
            "metadata": {
                "author": item["user"]["login"]
            }
        })

    return {
        "source": f"{source}",
        "entity": "issues",
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "data": issues
    }