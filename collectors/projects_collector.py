import requests
import os
from datetime import datetime, timezone
from dotenv import load_dotenv
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_API_URL = "https://api.github.com/graphql"

def fetch_project_items(org, project_number, source):
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}"
    }

    response = requests.post(
        GITHUB_API_URL,
        json={
          "query": f"""
          query {{
            organization(login: "{org}") {{
              projectV2(number: {project_number}) {{
                title
                items(first: 50) {{
                  nodes {{
                    content {{
                      ... on Issue {{
                        id
                        number
                        title
                        createdAt
                        state
                        labels(first: 10) {{
                          nodes {{
                            name
                          }}
                        }}
                      }}
                    }}
                    fieldValues(first: 10) {{
                      nodes {{
                        ... on ProjectV2ItemFieldSingleSelectValue {{
                          name
                          field {{
                            ... on ProjectV2FieldCommon {{
                              name
                            }}
                          }}
                        }}
                      }}
                    }}
                  }}
                }}
              }}
            }}
          }}
          """
        },
        headers=headers
    )

    
    if response.status_code != 200:
        raise Exception(f"Query failed: {response.text}")
    
    raw_data = response.json()
    
    items = raw_data.get("data", {}) \
        .get("organization", {}) \
        .get("projectV2", {}) \
        .get("items", {}) \
        .get("nodes", [])

    records = []

    for item in items:
        content = item.get("content")
        if not content:
            continue  # skip empty items

        # Extract labels
        labels = [
            label["name"]
            for label in content.get("labels", {}).get("nodes", [])
        ]

        # Extract custom fields (like Status)
        fields = {
            field["field"]["name"]: field["name"]
            for field in item.get("fieldValues", {}).get("nodes", [])
            if field.get("field")
        }

        records.append({
            "id": content["id"],
            "name": content["title"],
            "status": content["state"],  
            "created_at": content["createdAt"],
            "updated_at": content["createdAt"],  
            "metadata": {
                "number": content["number"],
                "labels": labels,
                "project_fields": fields
            }
        })

    return {
        "source": f"{source}",
        "entity": "project_items",
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "data": records
    }