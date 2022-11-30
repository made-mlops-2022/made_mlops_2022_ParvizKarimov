import os
import pandas as pd

import click

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score
import json

import joblib


@click.command("train")
@click.option("--input-dir")
@click.option("--output-dir")
def train(input_dir: str, output_dir: str):
    X_train = pd.read_csv(os.path.join(input_dir, "X_train.csv"))
    y_train = pd.read_csv(os.path.join(input_dir, "y_train.csv"))

    model = SVC(kernel='rbf')
    model.fit(X_train, y_train)


    X_valid = pd.read_csv(os.path.join(input_dir, "X_valid.csv"))
    y_valid = pd.read_csv(os.path.join(input_dir, "y_valid.csv"))

    y_pred = model.predict(X_valid)

    metrics = {
        'accuracy': accuracy_score(y_valid, y_pred),
        'f1': f1_score(y_valid, y_pred)
    }

    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, "metrics.json"), 'w+') as file:
        json.dump(metrics, file)
    
    joblib.dump(model, os.path.join(output_dir, "model.joblib"))




if __name__ == '__main__':
    train()