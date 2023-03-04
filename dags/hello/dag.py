from datetime import datetime, timedelta

from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='demo_hello',
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    end_date=datetime(2024, 1, 1),
    schedule_interval='0 0 * * *',
    catchup=False,
    tags=['demo']
) as dag:

    start = DummyOperator(
        task_id='start',
    )

    say_hello = PythonOperator(
        task_id='say_hello',
        python_callable=lambda: print("Hello World"),
    )

    start >> say_hello
