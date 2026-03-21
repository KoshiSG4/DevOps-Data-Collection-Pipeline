import sys
import yaml
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from collectors.cicd_collector import fetch_github_workflow_runs, fetch_deployments
from tests.test_load_data_to_devlake import process_entity

config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")

with open(config_path, "r") as f:
    config = yaml.safe_load(f)

cicds = config["cicd_collector"]

for cicd in cicds:
    owner = cicd["owner"]
    repo = cicd["repo"]
    source = cicd["source"]

    deployment_data = fetch_deployments(owner, repo, source)
    print(f"CICD deployment Data ({repo}) : {deployment_data}")

    workflow_data = fetch_github_workflow_runs(owner, repo, source)
    print(f"CICD workflow runs Data ({repo})  : {workflow_data}")

    process_entity(deployment_data)
    process_entity(workflow_data)