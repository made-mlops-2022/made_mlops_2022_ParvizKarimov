from tests.conftest import assert_dag_dict_equal
from airflow.models import DagBag


def test_data_generator_dag_loading(dagbag: DagBag):
    dag = dagbag.get_dag(dag_id="model_inference")
    assert dagbag.import_errors == {}
    assert dag is not None
    assert len(dag.tasks) == 4


def test_data_generator_dag_structure(dagbag: DagBag):
    assert_dag_dict_equal(
        {
            "wait_for_data": ['docker-airflow-predict'],
            "wait_for_preprocessor": ['docker-airflow-predict'],
            "wait_for_model": ['docker-airflow-predict'],
            "docker-airflow-predict": []
        },
        dagbag.get_dag(dag_id='model_inference'),
    )