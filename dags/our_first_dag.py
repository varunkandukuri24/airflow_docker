from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner':'varun',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='our_first_dag_v3',
    description='first test airflow dag',
    default_args=default_args,
    start_date=datetime(2023, 9, 29, 2),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world, this is the first task!"
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo hey this is task 2 and I am dependent on taks1'
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo Hey I am the third task'
    )

    task1.set_downstream(task2)
    task1.set_downstream(task3)