from airflow import DAG
# from airflow.datasets import Dataset
from airflow.decorators import task
from datetime import datetime, date

# my_file = Dataset("/temp/my_file.txt")

with DAG(
        dag_id="consumer",
        schedule_interval="@daily",
        start_date=datetime(2023, 1, 1),
        catchup=False
) as dag:
    None
    # @task(outlets=[my_file])
    # def read_dataset():
    #     with open(my_file.uri, "r") as f:
    #         print(f.read())
