import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bigquery.bq_collector import fetch_logs

start_time = "2024-03-27T20:00:00"
end_time = "2024-03-28T00:00:00"

data = fetch_logs(start_time,end_time)
print(f"BigQuery Data :\n \n {data}")