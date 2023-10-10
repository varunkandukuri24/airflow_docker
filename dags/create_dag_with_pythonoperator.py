from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

default_args = {
    'owner':'varun',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def greet():
    print("Hello World!")

with DAG(
    dag_id='our_first_dag_w_python_v1',
    description='testing python operators',
    default_args=default_args,
    start_date=datetime(2023, 9, 29, 2),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='salutation',
        python_callable=greet
    )

    task1