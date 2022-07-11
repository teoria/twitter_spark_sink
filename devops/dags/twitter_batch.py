import datetime
from airflow import models
from airflow.operators.dummy import DummyOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator


with models.DAG(dag_id="twitter_batch",
                start_date=datetime.datetime(2022, 2, 2),
                schedule_interval="0 */1 * * *",
                default_args={
                        "owner": "BI",
                        "email_on_failure": False,
                },
                catchup=False, ) as dag:

    trigger_target_mssql = TriggerDagRunOperator(
        task_id='trigger_mssql_ingestion',
        trigger_dag_id='1.2_mssql_extrator_dag',
        reset_dag_run=True,
        wait_for_completion=True,
        poke_interval=30
    )

    trigger_transform = TriggerDagRunOperator(
        task_id='trigger_target_dbt',
        trigger_dag_id='1.3_dbt_dag',
        reset_dag_run=True,
        wait_for_completion=True,
        poke_interval=30
    )

    start = DummyOperator(
        task_id='Start'
    )
    done = DummyOperator(
        task_id='Done'
    )

    start >> trigger_target_mssql >> trigger_transform >> done

