import os
from datetime import timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from docker.types import Mount
from airflow.sensors.python import PythonSensor
from airflow.operators.python import PythonOperator

from utils import wait_for_file, DATA_PATH


default_args = {
    "owner": "PK",
    "email": ["ippk9393@gmail.com", "karimov.pd@phystech.edu"],
    "email_on_failure": True,
    "email_on_retry": True,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}
def throw_error(**context):
    raise ValueError('Intentionally throwing an error to send an email.')



with DAG(
        "model_inference",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=days_ago(2),
) as dag:
    wait_for_data = PythonSensor(
        task_id="wait_for_data",
        python_callable=wait_for_file,
        op_kwargs={'path': 'data/raw/{{ ds }}/data.csv'},
        timeout=600,
        poke_interval=10,
        retries=100,
        mode="poke"
    )

    wait_for_preprocessor = PythonSensor(
        task_id="wait_for_preprocessor",
        python_callable=wait_for_file,
        op_kwargs={'path': '{{ var.value.preprocessor_dir }}/preprocessor.joblib'},
        timeout=600,
        poke_interval=10,
        retries=100,
        mode="poke"
    )

    wait_for_model = PythonSensor(
        task_id="wait_for_model",
        python_callable=wait_for_file,
        op_kwargs={'path': "{{ var.value.model_dir }}/model.joblib"},
        timeout=600,
        poke_interval=10,
        retries=100,
        mode="poke"
    )

    predict = DockerOperator(
        image="airflow-predict",
        command="--input-dir /data/raw/{{ ds }} --output-dir /data/predictions/{{ ds }} --preprocessor-dir {{ var.value.preprocessor_dir }} --model-dir {{ var.value.model_dir }}",
        task_id="docker-airflow-predict",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=DATA_PATH, target="/data", type='bind')]
    )

    [wait_for_data, wait_for_preprocessor, wait_for_model] >> predict

