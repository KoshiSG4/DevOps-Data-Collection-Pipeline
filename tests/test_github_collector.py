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

fields = config["github_repo_collector"]

for field in fields:
    owner = field["owner"]
    repo = field["repo"]
    source = field["source"]

    commits = fetch_commits(owner, repo, source)
    print(f"Commits ({repo}): {commits}\n")

    prs = fetch_prs(owner, repo, source)
    print(f"\nPull Requests ({repo}): {prs}\n")

    issues = fetch_issues(owner, repo, source)
    print(f"\nIssues ({repo}): {issues}\n")
