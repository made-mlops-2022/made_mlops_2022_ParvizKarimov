import logging
import os

import joblib
import pandas as pd
from dotenv import load_dotenv
from fastapi import FastAPI, Response, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from sklearn.exceptions import NotFittedError

from .schemas import DataPoint, Prediction

logging.basicConfig(level=logging.INFO)
load_dotenv()
MODEL_PATH = os.environ.get("MODEL_PATH")

app = FastAPI()
model = joblib.load(MODEL_PATH)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.post("/predict", response_model=Prediction)
def predict(data: DataPoint) -> Prediction:
    logging.info("Making prediction...")

    X_pred = pd.DataFrame(data.dict(), index=[0])

    y_pred = model.predict(X_pred)

    logging.info("Returning prediction...")

    return Prediction(prediction=y_pred)


@app.get("/health", status_code=200)
def health(response: Response) -> None:
    temp_data = {
        "age": 1.3076923076923077,
        "sex": 0.0,
        "cp": 1.0,
        "trestbps": 1.5416666666666667,
        "chol": -1.0142857142857142,
        "fbs": 0.0,
        "restecg": 1.0,
        "thalach": -0.421875,
        "exang": 1.0,
        "oldpeak": 0.0833333333333334,
        "slope": 1.0,
        "ca": 1.0,
        "thal": 0.0,
    }
    try:
        X_pred = pd.DataFrame(temp_data, index=[0])
        model.predict(X_pred)
    except NotFittedError:
        response.status_code = status.HTTP_418_IM_A_TEAPOT
    return
