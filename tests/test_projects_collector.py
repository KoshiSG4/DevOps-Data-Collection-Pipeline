import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from collectors.projects_collector import fetch_project_items

org = "ivedha-tech"
project_number = "12"

data = fetch_project_items(org, project_number)
print(f"Project Data :\n \n {data}")