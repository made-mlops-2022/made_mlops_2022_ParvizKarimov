import joblib
import logging
import pandas as pd
import hydra
from ml_project.conf.config import TrainConfig, Split, TargetDataset
from hydra.core.config_store import ConfigStore
from hydra.utils import instantiate
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
import json


cs = ConfigStore.instance()
cs.store(name='base_train', node=TrainConfig)
cs.store(group='split', name='base_stratified_split', node=Split)
cs.store(group='split', name='base_simple_split', node=Split)
cs.store(name='train_dataset', node=TargetDataset)


def get_data(file_path: str, target_col: str):
    logging.info("Loading data to train model...")

    df = pd.read_csv(file_path)
    X, y = df.drop(target_col, axis=1), df[target_col]

    logging.info("Data loaded.")

    return X, y

@hydra.main(version_base=None, config_path="../conf", config_name="train")
def train_model(cfg: TrainConfig):
    X, y = get_data(cfg.dataset.folder_path + cfg.dataset.name, cfg.dataset.target)

    clf = instantiate(cfg.model)

    if cfg.fit == 'split':
        logging.info("Splitting data...")

        if cfg.split.split_method == 'stratified':
            X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, **cfg.split.params)
        else:  # split_method == 'simple'
            X_train, X_test, y_train, y_test = train_test_split(X, y, **cfg.split.params)

    logging.info("Fitting classifier...")

    if cfg.fit == 'split':
        clf.fit(X_train, y_train)
        
        metrics = {
            "accuracy": accuracy_score(y_test, clf.predict(X_test)),
            "f1": f1_score(y_test, clf.predict(X_test))
        }

        logging.info("Saving metrics...")

        metric_path = cfg.model_path.rpartition('/')[0] + '/metrics.json'
        with open(metric_path, 'w+') as file:
            json.dump(metrics, file)

        logging.info("Metrics saved into %(metric_path)s." % {"metric_path": metric_path})

    else:
        clf.fit(X, y)

    logging.info("Saving model...")

    joblib.dump(clf, cfg.model_path)

    logging.info("Training finished.")


if __name__ == '__main__':
    train_model()
