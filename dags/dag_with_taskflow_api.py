from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args = {
    'owner': 'varun',
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}


@dag(dag_id='dag_w_taskflow_api_v2',
     default_args=default_args,
     start_date=datetime(2023, 9, 29, 2),
     schedule_interval='@daily')
def hello_world_etl():

    @task(multiple_outputs=True)
    def get_name():
        return {'first_name': 'Karan', 'last_name':'Johar'}
    
    @task()
    def get_age():
        return 26
    
    @task()
    def greet(first_name, last_name, age):
        print("Hello my name is {} {} and I am {} years old".format(first_name, last_name, age))

    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'], last_name=name_dict['last_name'], age=age)

greet_dag = hello_world_etl()