from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


def print_hello():
    print("Airflow test DAG is working")


with DAG(
    dag_id="test_dag",
    start_date=datetime(2026, 3, 19),
    schedule=None,
    catchup=False,
    tags=["test"],
) as dag:

    hello_task = PythonOperator(
        task_id="print_hello",
        python_callable=print_hello,
    )