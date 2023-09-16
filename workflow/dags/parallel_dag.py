from airflow.models.dag import DAG

from airflow.decorators import task
from datetime import datetime, date
from airflow.operators.bash import BashOperator

with DAG(
        dag_id="parallel_dag",
        schedule_interval="@daily",
        start_date=datetime(2023, 1, 1),
        catchup=False
) as dag:
    extract_a = BashOperator(
        task_id="extract_a",
        bash_command='sleep 10'
    )

    extract_b = BashOperator(
        task_id="extract_b",
        bash_command='sleep 10'
    )
    load_a = BashOperator(
        task_id="load_a",
        bash_command='sleep 10'
    )
    load_b = BashOperator(
        task_id="load_b",
        bash_command='sleep 10'
    )
    transform = BashOperator(
        task_id="transform",
        bash_command='sleep 30',
        queue='high_cpu'
    )
    extract_a >> load_a
    extract_b >> load_b
    [load_a, load_b] >> transform
