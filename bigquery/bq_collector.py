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

    platforms = ["Cloud Build", "Cloud Run", "Kubernetes Engine"]

    # Convert time
    start_ts = datetime.fromisoformat(start_time).replace(tzinfo=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    end_ts = datetime.fromisoformat(end_time).replace(tzinfo=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    for platform in platforms:
        platform_key = platform.replace(" ", "_").lower()
        all_data[platform_key] = []

        for table in billing_export_tables:
            query = f"""
                SELECT
                    service.description AS service_name,
                    sku.description AS sku_name,
                    usage_start_time,
                    usage_end_time,
                    project.id AS project_id,
                    location,
                    cost,
                    currency,
                    transaction_type
                FROM `{dataset_reference}.{table}`
                WHERE service.description = "{platform}"
                    AND usage_start_time >= TIMESTAMP('{start_ts}')
                    AND usage_end_time < TIMESTAMP('{end_ts}')
            """

        data = run_query(query)
        all_data[platform_key].extend(data)
  

    return all_data


