 # Load normalized data into DevLake DB

import pymysql
import json

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="admin",
    database="lake"
)

def create_table_if_not_exists(table_name, sample_record):
    cursor = connection.cursor()
    columns = []

    long_text_fields = ["message", "description", "body"]

    for k, v in sample_record.items():
        if k in long_text_fields:
            col_type = "TEXT"
        # elif isinstance(v, int):
        #     col_type = "INT"
        elif isinstance(v, str):
            if len(v) > 255:
                col_type = "TEXT"
            else:
                col_type = "VARCHAR(255)"
        elif isinstance(v, (dict, list)):
            col_type = "JSON"
        else:
            col_type = "VARCHAR(255)"
        
        if k == "id":
            columns.append(f"{k} {col_type} PRIMARY KEY")
        else:
            columns.append(f"{k} {col_type}")
            
    columns_sql = ", ".join(columns)
    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_sql})"
    cursor.execute(query)
    connection.commit()

def load_to_devlake(table_name, records):
    if not records:
        print(f"No data to load into {table_name}")
        return
    
    cursor = connection.cursor()

    for record in records:
        create_table_if_not_exists(table_name, record)

        # Serialize lists or dicts to JSON strings
        safe_record = {
            k: json.dumps(v) if isinstance(v, (dict, list)) else v
            for k, v in record.items()
        }

        columns = ", ".join(safe_record.keys())
        placeholders = ", ".join([f"%({k})s" for k in safe_record.keys()])

        query = f"""
            INSERT INTO {table_name} ({columns})
            VALUES ({placeholders})ON DUPLICATE KEY UPDATE
            """ + ", ".join([f"{k} = VALUES({k})" for k in safe_record.keys()])
        cursor.execute(query, safe_record)

    connection.commit()
    print(f"Inserted {len(records)} rows into {table_name}")