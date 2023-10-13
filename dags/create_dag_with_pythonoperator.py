from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

default_args = {
    'owner':'varun',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def greet(ti):
    first_name=ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name=ti.xcom_pull(task_ids='get_name', key='last_name')
    age= ti.xcom_pull(task_ids='get_age', key='age') 
    print("Hello World! My name is {} {} and I am  {} years old".format(first_name, last_name, age))

def get_name(ti):
    ti.xcom_push(key='first_name', value='Karan')
    ti.xcom_push(key='last_name', value='Johar')

def get_age(ti):
    ti.xcom_push(key='age', value='26')


with DAG(
    dag_id='our_first_dag_w_python_v6',
    description='testing python operators',
    default_args=default_args,
    start_date=datetime(2023, 9, 29, 2),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='salutation',
        python_callable=greet
        #op_kwargs={'age': 26}
    )
    task2 = PythonOperator(task_id='get_name', python_callable=get_name)
    task3 = PythonOperator(task_id='get_age', python_callable=get_age)

    [task2, task3] >> task1