from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.email import send_email

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    'check_disk_space',
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=['demo']
) as dag:

    def send_failure_mail(context):
        send_email(
            to='xxx@gmail.com',
            subject='Low disk space warning',
            html_content='The available disk space is less than 90%. Please check the server.',
        )

    BashOperator(
        task_id='check_space',
        bash_command='''
        if (( $(df -h | awk \'$NF=="/"{print int($5)}\') > 90 )); then
            exit 1;
        fi
        ''',
        on_failure_callback=send_failure_mail,
    )
