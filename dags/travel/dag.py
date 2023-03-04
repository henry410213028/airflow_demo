from datetime import datetime, timedelta

from airflow.models import DAG
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
    dag_id='show_taipei_travel',
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    end_date=datetime(2024, 1, 1),
    schedule_interval='0 0 * * *',
    catchup=False,
    tags=['demo']
) as dag:

    from travel import udf

    PythonOperator(
        task_id='list_events',
        python_callable=udf.main,
        op_kwargs={
            "start_date": "{{ ds }}",
            "end_date": "{{ next_ds }}",
        }
    )
