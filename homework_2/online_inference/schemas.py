from pydantic import BaseModel, conint


class DataPoint(BaseModel):
    age: float
    sex: conint(ge=0, le=1)
    cp: conint(ge=0, le=3)
    trestbps: float
    chol: float
    fbs: conint(ge=0, le=1)
    restecg: conint(ge=0, le=2)
    thalach: float
    exang: conint(ge=0, le=1)
    oldpeak: float
    slope: conint(ge=0, le=2)
    ca: conint(ge=0, le=3)
    thal: conint(ge=0, le=2)


class Prediction(BaseModel):
    prediction: conint(ge=0, le=1)
