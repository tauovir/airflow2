from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator

from datetime import datetime


def _t1(ti):
    ti.xcom_push(key='sale', value=99)


def _t2(ti):
    x = ti.xcom_pull(key='sale', task_ids='t1')
    print("x======", x)


def _branch(ti):
    val = ti.xcom_pull(key='sale', task_ids='t1')
    if val < 99:
        return 't2'
    else:
        return 't3'


with DAG("xcom_dag", start_date=datetime(2022, 1, 1),
         schedule_interval='@daily', catchup=False) as dag:
    t1 = PythonOperator(
        task_id='t1',
        python_callable=_t1
    )
    branch = BranchPythonOperator(
        task_id='branch',
        python_callable=_branch
    )

    t2 = PythonOperator(
        task_id='t2',
        python_callable=_t2
    )

    t3 = BashOperator(
        task_id='t3',
        bash_command="echo ''"
    )
    t4 = BashOperator(
        task_id='t4',
        bash_command="echo ''",
        trigger_rule = 'one_success'  # one_success,all_success,all_failed,all_done ----
    )

    t1 >> branch >> [t2, t3] >> t4
