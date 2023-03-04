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
    dag_id='travel_remider',
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    end_date=datetime(2024, 1, 1),
    schedule_interval='0 0 * * *',
    catchup=False,
    tags=['demo']
) as dag:

    from remider import udf

    fetch_travel_events = PythonOperator(
        task_id='fetch_travel_events',
        python_callable=udf.fetch_travel_events,
        provide_context=True,
        op_kwargs={
            "start_date": "{{ ds }}",
            "end_date": "{{ next_ds }}",
        }
    )

    send_activity_msg = PythonOperator(
        task_id='send_activity_msg',
        python_callable=udf.send_activity_msg,
        provide_context=True,
    )

    clean_up = PythonOperator(
        task_id='clean_up',
        python_callable=udf.clean_up,
        provide_context=True,
    )

    fetch_travel_events > send_activity_msg >> clean_up
