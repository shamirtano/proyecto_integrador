from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('elt_pipeline_dag', start_date=datetime(2023, 11, 1), schedule_interval='@daily') as dag:
    run_notebook = BashOperator(
        task_id='run_project_notebook',
        bash_command='papermill /app/Project.ipynb /app/output.ipynb'
    )