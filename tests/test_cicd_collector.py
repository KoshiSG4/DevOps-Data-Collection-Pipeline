import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from collectors.cicd_collector import fetch_github_workflow_runs, fetch_deployments

owner = "ivedha-tech"
repo = "platformnex-frontend"

data = fetch_deployments(owner, repo)
print(f"CICD deployment Data : {data}")

data = fetch_github_workflow_runs(owner, repo)
print(f"CICD workflow runs Data : {data}")