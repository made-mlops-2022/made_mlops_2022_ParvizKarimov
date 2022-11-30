import os
import pandas as pd

import click
import joblib


@click.command("model-predict")
@click.option("--input-dir")
@click.option("--output-dir")
@click.option("--model-dir")
@click.option("--preprocessor-dir")
def model_predict(input_dir: str, output_dir: str, model_dir: str, preprocessor_dir: str):
    data = pd.read_csv(os.path.join(input_dir, "data.csv"))
    
    preprocessor= joblib.load(os.path.join(preprocessor_dir, "preprocessor.joblib"))
    model = joblib.load(os.path.join(model_dir, "model.joblib"))

    preds = pd.DataFrame(model.predict(preprocessor.transform(data)))

    os.makedirs(output_dir, exist_ok=True)
    preds.to_csv(os.path.join(output_dir, "predictions.csv"), index=False)


if __name__ == '__main__':
    model_predict()