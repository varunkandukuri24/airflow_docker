from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner':'varun',
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='catchup_backfill_dag_v2',
    description='Testing catchup and backfill',
    default_args=default_args,
    start_date=datetime(2023, 9, 29, 2),
    schedule_interval='@daily',
    catchup=False
) as dag:
    task1 = BashOperator(task_id = 'task1', bash_command='echo this is a test command')