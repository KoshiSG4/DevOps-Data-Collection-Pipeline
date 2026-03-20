import requests
from datetime import datetime, timezone

import os
from dotenv import load_dotenv
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization" : f"token {GITHUB_TOKEN}",
    "Accept" : "application/vnd.github+json"
}

def fetch_github_workflow_runs(owner, repo,source):
    url = f"https://api.github.com/repos/{owner}/{repo}/actions/runs"

    try: 
        response = requests.get(url, headers=headers)

        if response.status_code == 404:
            print(f"No workflow runs found for {owner}/{repo}")
            return[]
        
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching workflow runs for {owner}/{repo}: {e}")
        return []
    
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
            "metadata": {
                "conclusion": run["conclusion"],
                "url": run["html_url"]
            }
        }

         for run in data.get("workflow_runs", [])
    ]

    return {
        "source": f"{source}",
        "entity": "workflow_runs",
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "data": workflows
    }

def fetch_deployments(owner, repo, source):
    deployment_url = f"https://api.github.com/repos/{owner}/{repo}/deployments"
    
    try: 
        deployment_resp = requests.get(deployment_url, headers=headers)

        if deployment_resp.status_code == 404:
            print(f"No deployements found for {owner}/{repo}")
            return[]
        
        deployment_resp.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching deployments for {owner}/{repo}: {e}")
        return []
    
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
            "environment": dep["environment"],
            "status": latest_status.get("state"),
            "created_at": dep["created_at"],
            "updated_at": latest_status.get("updated_at"),
            "url": dep.get("url"),
             "metadata": {
                "sha": dep["sha"],
                "ref": dep["ref"]
            }
        })

    return {
        "source": f"{source}",
        "entity": "deployments",
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "data": deployments
    }
