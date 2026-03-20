import sys
import yaml
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bigquery.bq_collector import fetch_logs

config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")

with open(config_path, "r") as f:
    config = yaml.safe_load(f)

tables = config["bq_collector"]

for table in tables:
    table_name = table["table_name"]
    dataset_reference = table["dataset_reference"]
    platforms = table["platforms"]
    start_time = table["start_time"].isoformat()
    end_time = table["end_time"].isoformat()


    data = fetch_logs(start_time,end_time, dataset_reference, table_name, platforms)
    print(f"BigQuery Data :\n \n {data}")