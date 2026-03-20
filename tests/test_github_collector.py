import sys
import yaml
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from collectors.github_collector import fetch_commits
from collectors.github_collector import fetch_prs
from collectors.github_collector import fetch_issues

config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")

with open(config_path, "r") as f:
    config = yaml.safe_load(f)

cicds = config["cicd_collector"]

for cicd in cicds:
    owner = cicd["owner"]
    repo = cicd["repo"]

    commits = fetch_commits("ivedha-tech","platformnex-frontend")
    print(f"Commits ({repo}): {commits}")

    prs = fetch_prs("ivedha-tech","platformnex-frontend")
    print(f"Pull Requests ({repo}): {prs}")

    issues = fetch_issues("ivedha-tech","platformnex-frontend")
    print(f"Issues ({repo}): {issues}")
