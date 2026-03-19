import requests

import os
from dotenv import load_dotenv
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization" : f"token {GITHUB_TOKEN}",
    "Accept" : "application/vnd.github+json"
}

def fetch_github_workflows(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/actions/runs"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()

    #extract relevant info
    workflows = [
        {
            "id" : run["id"],
            "name": run["name"],
            "status": run["status"],
            "conclusion": run["conclusion"],
            "created_at": run["created_at"],
            "updated_at": run["updated_at"],
            "url": run["html_url"]
        }

         for run in data.get("workflow_runs", [])
    ]

    return workflows