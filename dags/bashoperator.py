from __future__ import print_function
from builtins import range
from airflow.operators import BashOperator
from airflow.models import DAG
from datetime import datetime, timedelta

import time
from pprint import pprint

seven_days_ago = datetime.combine(
        datetime.today() - timedelta(7), datetime.min.time())

args = {
    'owner': 'airflow',
    'start_date': seven_days_ago,
}

dag = DAG(
    dag_id='test_bash_operator', default_args=args,
    schedule_interval=None)


	
run_this = BashOperator(
    task_id='run_after_loop',
    bash_command='sleep 100',
    dag=dag,
)
