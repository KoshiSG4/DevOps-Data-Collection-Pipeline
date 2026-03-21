# import your normalization functions
from devlake.normalize import normalize_commits_to_devlake
from devlake.normalize  import normalize_prs_to_devlake
from devlake.normalize  import normalize_issues_to_devlake
from devlake.normalize  import normalize_projects_data_to_devlake
from devlake.normalize  import normalize_workflow_runs_to_devlake
from devlake.normalize  import normalize_deployments_to_devlake
from devlake.normalize  import normalize_bq_data_to_devlake
from devlake.loader import load_to_devlake

# Map entity -> Python function
NORMALIZE_FUNCTIONS = {
    "commits": normalize_commits_to_devlake,
    "pull_requests": normalize_prs_to_devlake,
    "issues": normalize_issues_to_devlake,
    "project_items": normalize_projects_data_to_devlake,
    "workflow_runs": normalize_workflow_runs_to_devlake,
    "deployments": normalize_deployments_to_devlake,
    "gcp_logs": normalize_bq_data_to_devlake
}

# Load YAML config
import yaml
import os
config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")

with open(config_path, "r") as f:
    config = yaml.safe_load(f)

ENTITY_CONFIG = config["ENTITY_CONFIG"]

def process_entity(data):
    entity = data["entity"]
    print("Entity:",entity)

    # Get table from YAML
    table_name = ENTITY_CONFIG[entity]["table"]
    print("Table name:",table_name)

    # Get normalization function from Python dict
    normalize_fn = NORMALIZE_FUNCTIONS[entity]
    print("\nnormalize_fn from test load data to devlake \n:", normalize_fn)

    normalized = normalize_fn(data)
    load_to_devlake(table_name, normalized)