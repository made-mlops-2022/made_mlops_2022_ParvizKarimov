from sdv.tabular import GaussianCopula
import hydra
from hydra.core.config_store import ConfigStore
import pandas as pd
from ml_project.conf.config import FakeDataGeneratorCfg
import logging


cs = ConfigStore.instance()
cs.store(name='base_data_generator', node=FakeDataGeneratorCfg)


@hydra.main(version_base=None, config_path='../conf', config_name='generate_data')
def generate(cfg: FakeDataGeneratorCfg):
    logging.info("Loading data...")
    
    orig_df = pd.read_csv(cfg.original_folder + cfg.name)

    logging.info("Generating new data...")

    model = GaussianCopula()
    model.fit(orig_df)
    generated = model.sample(1024)

    logging.info("Saving data to %(full_save_path)s..." % {"full_save_path": cfg.save_path})
    
    generated.to_csv(cfg.save_path)

    logging.info("Fake data generated.")



if __name__ == '__main__':
    generate()