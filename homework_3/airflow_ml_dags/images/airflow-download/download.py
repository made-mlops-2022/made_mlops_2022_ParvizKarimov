import os

import pandas as pd
import click
from sklearn.datasets import make_classification


@click.command("download")
@click.argument("output_dir")
def download(output_dir: str):
    X, y = make_classification(n_samples=10000, n_features=2, n_informative=2, n_redundant=0, n_repeated=0,
                               n_classes=2, n_clusters_per_class=1, class_sep=2, flip_y=0.2, weights=[0.5, 0.5], random_state=17)

    os.makedirs(output_dir, exist_ok=True)

    pd.DataFrame(X).to_csv(os.path.join(output_dir, "data.csv"), index=False)
    pd.DataFrame(y).to_csv(os.path.join(output_dir, "target.csv"), index=False)


if __name__ == '__main__':
    download()
