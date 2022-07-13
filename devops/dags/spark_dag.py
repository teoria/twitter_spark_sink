import datetime
from airflow import models
from airflow.operators.dummy import DummyOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

with models.DAG(dag_id="twitter_batch",
                start_date=datetime.datetime(2022, 2, 2),
                schedule_interval="0 */1 * * *",
                default_args={
                        "owner": "BI",
                        "email_on_failure": False,
                },
                catchup=False, ) as dag:

     
    submit_job = SparkSubmitOperator(
        task_id='submit_job', 
        conn_id='spark',
        application="./dags/twitter_batch.py"
    )
 