from datetime import datetime

from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'end_date': None,
    'schedule_interval': None,
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': 0,
}

with DAG(
    dag_id='demo_flow1',
    default_args=default_args,
    catchup=False,
    tags=['demo']
) as dag1:

    task1 = DummyOperator(task_id='task1')
    task2 = DummyOperator(task_id='task2')
    task3 = DummyOperator(task_id='task3')
    task4 = DummyOperator(task_id='task4')

    task1 >> [task2, task3] >> task4


with DAG(
    dag_id='demo_flow2',
    default_args=default_args,
    catchup=False,
    tags=['demo']
) as dag2:

    task1 = DummyOperator(task_id='task1')
    task2 = DummyOperator(task_id='task2')
    task3 = DummyOperator(task_id='task3')
    task4 = DummyOperator(task_id='task4')

    task4 << [task2, task3] << task1
