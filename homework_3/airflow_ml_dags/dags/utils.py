import os

DATA_PATH = "/home/ippk93/mlops/homework_3/airflow_ml_dags/data"

def wait_for_file(path: str) -> bool:
    return os.path.exists(path)