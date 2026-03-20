import sys
import yaml
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from collectors.cicd_collector import fetch_github_workflow_runs, fetch_deployments

config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")

with open(config_path, "r") as f:
    config = yaml.safe_load(f)

cicds = config["cicd_collector"]

for cicd in cicds:
    owner = cicd["owner"]
    repo = cicd["repo"]
    source = cicd["source"]

    data = fetch_deployments(owner, repo, source)
    print(f"CICD deployment Data ({repo}) : {data}")

    data = fetch_github_workflow_runs(owner, repo, source)
    print(f"CICD workflow runs Data ({repo})  : {data}")