import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from collectors.github_collector import fetch_commits
from collectors.github_collector import fetch_prs
from collectors.github_collector import fetch_issues

commits = fetch_commits("ivedha-tech","platformnex-frontend")
print(f"Commits: {commits}")

prs = fetch_prs("ivedha-tech","platformnex-frontend")
print(f"Pull Requests: {prs}")

issues = fetch_issues("ivedha-tech","platformnex-frontend")
print(f"Issues: {issues}")
