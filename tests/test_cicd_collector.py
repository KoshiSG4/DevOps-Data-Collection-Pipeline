import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from collectors.cicd_collector import fetch_github_workflows

owner = "ivedha-tech"
repo = "platformnex-frontend"

data = fetch_github_workflows(owner, repo)
print(f"CICD Data : {data}")