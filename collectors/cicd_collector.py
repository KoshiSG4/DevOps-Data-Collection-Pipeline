import requests

import os
from dotenv import load_dotenv
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization" : f"token {GITHUB_TOKEN}",
    "Accept" : "application/vnd.github+json"
}

def fetch_github_workflow_runs(owner, repo):
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

def fetch_deployments(owner, repo):
    deployment_url = f"https://api.github.com/repos/{owner}/{repo}/deployments"
    deployment_resp = requests.get(deployment_url, headers=headers)
    deployment_resp.raise_for_status()
    deployment_data = deployment_resp.json()

    deployments = []

    for dep in deployment_data:
        # Fetch deployment status (latest)
        status_resp = requests.get(dep["statuses_url"], headers=headers)
        status_resp.raise_for_status()
        status_data = status_resp.json()
        latest_status = status_data[0] if status_data else {}

        deployments.append({
            "type": "deployment",
            "id": dep["id"],
            "sha": dep["sha"],
            "ref": dep["ref"],
            "environment": dep["environment"],
            "state": latest_status.get("state"),
            "created_at": dep["created_at"],
            "updated_at": latest_status.get("updated_at"),
            "url": dep.get("url")
        })

    return deployments
