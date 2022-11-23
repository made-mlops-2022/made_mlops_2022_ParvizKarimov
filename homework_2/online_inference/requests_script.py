import logging
import os

import pandas as pd
import requests
from dotenv import load_dotenv

from schemas import DataPoint

logging.basicConfig(level=logging.INFO)

load_dotenv()


def main() -> None:
    logging.info("Checking model health...")

    req = requests.get("http://0.0.0.0:8000/health")

    if req.status_code != 200:
        logging.error(
            "Model is not ready to make predictions. Stopping script."
        )
        return

    DATA_PATH = os.environ.get("DATA_PATH")
    logging.info(f"Loading data from {DATA_PATH}...")

    data = pd.read_csv("data/data.csv", index_col=False)
    dict_data = list(
        map(
            lambda x: DataPoint(**x),
            data.drop("condition", axis=1).to_dict("records"),
        )
    )

    logging.info("Senging data...")

    results = {"prediction": []}
    for data_point in dict_data:
        req = requests.post(
            "http://0.0.0.0:8000/predict", json=data_point.dict()
        )
        results["prediction"].append(req.json()["prediction"])

    logging.info("Saving predictions...")

    pd.DataFrame(results).to_csv("data/predictions.csv", index=False)

    logging.info("Done.")


if __name__ == "__main__":
    main()
