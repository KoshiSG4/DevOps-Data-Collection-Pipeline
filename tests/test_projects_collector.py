import sys
import yaml
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from collectors.projects_collector import fetch_project_items
from tests.test_load_data_to_devlake import process_entity

config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")

with open(config_path, "r") as f:
    config = yaml.safe_load(f)

projects = config["github_projects_collector"]

for project in projects:
    org = project["org"]
    project_number = project["project_number"]
    source = project["source"]

data = fetch_project_items(org, project_number, source)
print(f"Project Data :\n \n {data}")

process_entity(data)