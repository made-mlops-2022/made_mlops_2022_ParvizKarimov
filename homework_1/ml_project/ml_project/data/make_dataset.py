import logging

import hydra
import pandas as pd
from hydra.core.config_store import ConfigStore
from hydra.utils import instantiate

from ml_project.conf.config import DatasetMaker, Preprocessor
from ml_project.features.transformer import DataTransformer

cs = ConfigStore.instance()
cs.store(name="base_dataset_maker", node=DatasetMaker)
cs.store(group="preprocessing", name="base_preprocessor", node=Preprocessor)


@hydra.main(
    version_base=None, config_path="../conf", config_name="make_dataset"
)
def make_dataset(cfg: DatasetMaker) -> None:
    logging.info("Loading raw dataset...")

    load_path = cfg.folder_path + cfg.name
    save_path = cfg.save_folder_path + cfg.name

    df = pd.read_csv(load_path, index_col=False)

    logging.info("Preprocessing dataset...")

    transformer = DataTransformer(
        scaler=instantiate(cfg.preprocessing.scaler),
        num_features=cfg.features_to_process["numerical"],
    ).fit(df)
    df = transformer.transform(df)

    logging.info("Saving dataset...")

    df.to_csv(save_path, index=False)

    logging.info("Dataset saved to %(save_path)s." % {"save_path": save_path})


if __name__ == "__main__":
    make_dataset()
