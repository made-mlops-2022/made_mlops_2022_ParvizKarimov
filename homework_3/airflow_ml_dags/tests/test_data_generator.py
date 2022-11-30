from tests.conftest import assert_dag_dict_equal
from airflow.models import DagBag


def test_data_generator_dag_loading(dagbag: DagBag):
    dag = dagbag.get_dag(dag_id="data_generator")
    assert dagbag.import_errors == {}
    assert dag is not None
    assert len(dag.tasks) == 1


def test_data_generator_dag_structure(dagbag: DagBag):
    assert_dag_dict_equal(
        {
            "docker-airflow-download": [],
        },
        dagbag.get_dag(dag_id='data_generator'),
    )