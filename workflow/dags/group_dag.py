from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime, date
from groups.group_downloads import download_tasks

with DAG('group_dag',
         start_date=datetime(2023, 1, 1),
         schedule_interval="@daily",
         catchup=False
         ) as dag:
    args = {'start_date': dag.start_date,
            'schedule_interval': dag.schedule_interval,
            'catchup': dag.catchup}

    downloads = download_tasks()
    check_file = BashOperator(
        task_id="check_file",
        bash_command='sleep 10'
    )
    #transform = transform_task()


    downloads >> check_file
