import joblib
import logging
import pandas as pd
import hydra
from ml_project.conf.config import PredictConfig, Dataset
from hydra.core.config_store import ConfigStore
from hydra.utils import instantiate

cs = ConfigStore.instance()
cs.store(name='base_predict', node=PredictConfig)
cs.store(name='test_dataset', node=Dataset)


@hydra.main(version_base=None, config_path="../conf", config_name="predict")
def predict(cfg: PredictConfig):
    logging.info("Loading data...")

    df_predict = pd.read_csv(cfg.dataset.folder_path + cfg.dataset.name).drop('condition', axis=1, errors='ignore')

    logging.info("Loading model...")

    model = joblib.load(cfg.model_path)

    logging.info("Predicting...")

    y_pred = pd.DataFrame(model.predict(df_predict))
    y_pred.to_csv(cfg.predict_path, index=False)

    logging.info("Prediction done.")


if __name__ == '__main__':
    predict()
