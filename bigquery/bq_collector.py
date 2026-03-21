from datetime import datetime, timezone
from bigquery.bq_utils import run_query

def fetch_logs(start_time:str, end_time:str, dataset_reference, table_name, platforms, source ):
    all_data = []

    # Convert time
    start_ts = datetime.fromisoformat(start_time).replace(tzinfo=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    end_ts = datetime.fromisoformat(end_time).replace(tzinfo=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    for platform in platforms:

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
            FROM `{dataset_reference}.{table_name}`
            WHERE service.description = "{platform}"
                AND usage_start_time >= TIMESTAMP('{start_ts}')
                AND usage_end_time < TIMESTAMP('{end_ts}')
        """

        data = run_query(query)
        
        for row in data:
            all_data.append({
                "id": f"{row['project_id']}_{row['usage_start_time']}",
                "name": row["service_name"],
                "status": row["transaction_type"],
                "created_at": row["usage_start_time"],
                "updated_at": row["usage_end_time"],
                "metadata": {
                    "platform": platform,
                    "cost": row["cost"],
                    "currency": row["currency"],
                    "sku": row["sku_name"],
                    "location": row["location"]
                }
            })

  

    return {
        "source": f"{source}",
        "entity": "gcp_logs",
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "data": all_data
    }


