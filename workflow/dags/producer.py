from airflow.models.dag import DAG
# from airflow.datasets import Dataset
from airflow.decorators import task
from datetime import datetime, date

#my_file = Dataset("/temp/my_file.txt")

with DAG(
    dag_id = "producer",
    schedule_interval = "@daily",
    start_date = datetime(2023,1,1),
    catchup = False
):
    None
    # @task(outlets = [my_file])
    # def update_dataset():
    #     with open(my_file.uri,"a+") as f:
    #         f.write("producer update")
    #
    #
    # update_dataset()
