import pytest
from fastapi.testclient import TestClient
from sklearn.exceptions import NotFittedError
from sklearn.linear_model import LogisticRegression

from . import fastapi_app
from .fastapi_app import app
from .schemas import DataPoint

client = TestClient(app)
test_data = DataPoint(
    **{
        "age": 0.8461538461538461,
        "sex": 0.0,
        "cp": 2.0,
        "trestbps": 1.8333333333333333,
        "chol": 0.6714285714285714,
        "fbs": 0.0,
        "restecg": 1.0,
        "thalach": 0.046875,
        "exang": 1.0,
        "oldpeak": -0.4166666666666667,
        "slope": 0.0,
        "ca": 1.0,
        "thal": 1.0,
    }
)


def test_predict_loaded() -> None:
    response = client.post("/predict", json=test_data.dict())

    assert response.status_code == 200

    json_resp = response.json()
    assert "prediction" in json_resp
    assert json_resp["prediction"] in [0, 1]


@pytest.mark.parametrize(
    "key, value",
    [("age", "NANANA"), ("cp", 4), ("fbs", 2), ("exang", -10), ("slope", -1)],
)
def test_predict_code_400(key, value) -> None:
    test_data_cp = test_data.dict()
    test_data_cp[key] = value
    res = client.post("/predict", json=test_data_cp)
    print(res.text)
    assert res.status_code == 400


def test_predict_not_loaded(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(fastapi_app, "model", LogisticRegression())
    with pytest.raises(NotFittedError):
        client.post("/predict", json=test_data.dict())
