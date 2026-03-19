from datetime import datetime, timezone
from bigquery.bq_utils import run_query

def fetch_logs(start_time: str, end_time: str):
    billing_export_tables = [
        "gcp_billing_export_resource_v1_011C19_C13966_9DC5E1",
        "gcp_billing_export_resource_v1_01E9B5_60A8A4_E1FE52",
        "gcp_billing_export_v1_011C19_C13966_9DC5E1",
        "gcp_billing_export_v1_01E9B5_60A8A4_E1FE52"
    ]

    all_data = {}

    dataset_reference = "prj-datasource-billing.ds_billing"

    queries = {
        "billing_summary_daily":f"""
            SELECT *
            FROM `{dataset_reference}.billing_summary_daily`
            WHERE usage_date = DATE '{datetime.fromisoformat(start_time).date()}'
        """,

        "cloud_pricing_export":f"""
            SELECT *
            FROM `{dataset_reference}.cloud_pricing_export`
            WHERE export_time >= TIMESTAMP('{datetime.fromisoformat(start_time).replace(tzinfo=timezone.utc)}')
            AND export_time < TIMESTAMP('{datetime.fromisoformat(end_time).replace(tzinfo=timezone.utc)}')
        """,
    }

    for table in billing_export_tables:
        queries[table] = f"""
            SELECT *
            FROM `{dataset_reference}.{table}`
            WHERE  usage_start_time>= TIMESTAMP('{datetime.fromisoformat(start_time).replace(tzinfo=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")}')
            AND usage_end_time < TIMESTAMP('{datetime.fromisoformat(end_time).replace(tzinfo=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")}')
        """

    for name, query in queries.items():
        data = run_query(query)
        all_data[name] = data

    return all_data
