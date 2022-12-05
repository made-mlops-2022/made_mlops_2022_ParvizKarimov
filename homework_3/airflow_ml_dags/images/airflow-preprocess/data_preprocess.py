import os
import pandas as pd
import click
from sklearn.preprocessing import StandardScaler
import joblib

@click.command("data-preprocess")
@click.option("--input-dir")
@click.option("--output-dir")
@click.option("--preprocessor-dir")
def data_preprocess(input_dir: str, output_dir: str, preprocessor_dir: str):
    data = pd.read_csv(os.path.join(input_dir, "data.csv"))
    target = pd.read_csv(os.path.join(input_dir, "target.csv"))

    scaler = StandardScaler()
    preprocessed = pd.DataFrame(scaler.fit_transform(X=data, y=target))

    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(preprocessor_dir, exist_ok=True)

    preprocessed.to_csv(os.path.join(output_dir, "data.csv"), index=False)
    target.to_csv(os.path.join(output_dir, "target.csv"), index=False)

    joblib.dump(scaler, os.path.join(preprocessor_dir, "preprocessor.joblib"))


if __name__ == '__main__':
    data_preprocess()