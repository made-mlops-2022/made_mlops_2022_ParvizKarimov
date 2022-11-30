import os
from datetime import timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from docker.types import Mount
from airflow.sensors.python import PythonSensor
from airflow.models import Variable

from utils import wait_for_file, DATA_PATH

default_args = {
    "owner": "PK",
    "email": ["ippk9393@gmail.com"],
    "email_on_failure": True,
    "email_on_retry": True,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
        "model_training",
        default_args=default_args,
        schedule_interval="@weekly",
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

    Variable.set("preprocessor_dir", "data/preprocessor/standard")
    preprocess = DockerOperator(
        image="airflow-preprocess",
        command="--input-dir /data/raw/{{ ds }} --output-dir /data/processed/{{ ds }} --preprocessor-dir {{ var.value.preprocessor_dir }}",
        task_id="docker-airflow-preprocess",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=DATA_PATH, target="/data", type='bind')]
    )

    split = DockerOperator(
        image="airflow-split",
        command="--input-dir /data/processed/{{ ds }} --output-dir /data/processed/{{ ds }}",
        task_id="docker-airflow-split",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=DATA_PATH, target="/data", type='bind')]
    )

    Variable.set("model_dir", "data/models/svc")
    train = DockerOperator(
        image="airflow-train",
        command="--input-dir /data/processed/{{ ds }} --output-dir {{ var.value.model_dir }}",
        task_id="docker-airflow-train",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=DATA_PATH, target="/data", type='bind')]
    )


    wait_for_data >> preprocess >> split >> train
