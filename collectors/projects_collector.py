import requests
import os
from dotenv import load_dotenv
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_API_URL = "https://api.github.com/graphql"

def fetch_project_items(org, project_number):
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

    return response.json()