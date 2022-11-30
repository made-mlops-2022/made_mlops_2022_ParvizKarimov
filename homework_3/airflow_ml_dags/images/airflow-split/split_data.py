import os
import pandas as pd

import click
from sklearn.model_selection import train_test_split


@click.command("split")
@click.option("--input-dir")
@click.option("--output-dir")
def split(input_dir: str, output_dir):
    data = pd.read_csv(os.path.join(input_dir, "data.csv"))
    target = pd.read_csv(os.path.join(input_dir, "target.csv"))
    
    X_train, X_valid, y_train, y_valid = train_test_split(data, target, train_size=0.8, shuffle=True, stratify=target)


    os.makedirs(output_dir, exist_ok=True)

    X_train.to_csv(os.path.join(output_dir, "X_train.csv"), index=False)
    X_valid.to_csv(os.path.join(output_dir, "X_valid.csv"), index=False)
    y_train.to_csv(os.path.join(output_dir, "y_train.csv"), index=False)
    y_valid.to_csv(os.path.join(output_dir, "y_valid.csv"), index=False)



if __name__ == '__main__':
    split()