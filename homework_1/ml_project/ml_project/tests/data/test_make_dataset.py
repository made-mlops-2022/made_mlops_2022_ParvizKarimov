import pathlib as pl
import unittest

from hydra import compose, initialize

from ml_project.conf.config import DatasetMaker
from ml_project.data.make_dataset import make_dataset


class TestMakeDataset(unittest.TestCase):
    def test_make_dataset_logging(self):
        with initialize(version_base=None, config_path="../../conf"):
            cfg: DatasetMaker = compose(config_name="test_make_dataset")
            with self.assertLogs(logger="root", level="INFO") as cm:
                make_dataset(cfg)
            logging_str = "".join(cm.output)
            self.assertIn("Loading", logging_str)
            self.assertIn("Preprocessing", logging_str)
            self.assertIn("Saving", logging_str)
            self.assertIn("Dataset saved ", logging_str)
            pl.Path(
                "ml_project/data/processed/fake_heart_cleveland_upload.csv"
            ).unlink(missing_ok=True)

    def test_make_dataset_saved(self):
        with initialize(version_base=None, config_path="../../conf"):
            cfg: DatasetMaker = compose(config_name="test_make_dataset")
            make_dataset(cfg)
            path = pl.Path(
                "ml_project/data/processed/fake_heart_cleveland_upload.csv"
            )
            self.assertEquals((str(path), path.is_file()), (str(path), True))


if __name__ == "__main__":
    unittest.main()
