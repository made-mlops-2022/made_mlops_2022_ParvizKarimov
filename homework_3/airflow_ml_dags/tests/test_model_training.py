from tests.conftest import assert_dag_dict_equal
from airflow.models import DagBag


def test_data_generator_dag_loading(dagbag: DagBag):
    dag = dagbag.get_dag(dag_id="model_training")
    assert dagbag.import_errors == {}
    assert dag is not None
    assert len(dag.tasks) == 4


def test_data_generator_dag_structure(dagbag: DagBag):
    assert_dag_dict_equal(
        {
            "wait_for_data": ['docker-airflow-preprocess'],
            "docker-airflow-preprocess": ['docker-airflow-split'],
            "docker-airflow-split": ['docker-airflow-train'],
            "docker-airflow-train": []
        },
        dagbag.get_dag(dag_id='model_training'),
    )