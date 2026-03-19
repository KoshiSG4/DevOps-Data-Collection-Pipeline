import os
from dotenv import load_dotenv
load_dotenv()

from google.cloud import bigquery

def get_bq_client():
    return bigquery.Client()

def run_query(query:str):
    client = get_bq_client()
    query_job = client.query(query)
    results = query_job.result()

    rows = []

    for row in results:
        rows.append(dict(row))

    return rows