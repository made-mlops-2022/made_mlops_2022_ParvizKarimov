import unittest

import pandas as pd
from hydra import compose, initialize
from sklearn.exceptions import NotFittedError
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
from sklearn.utils.validation import check_is_fitted

from ml_project.conf.config import TargetDataset
from ml_project.features.transformer import DataTransformer


class TestTransformer(unittest.TestCase):
    def setUp(self) -> None:
        self.num_features = ["age", "trestbps", "chol", "thalach", "oldpeak"]
        self.transformerMinMax = DataTransformer(
            scaler=MinMaxScaler(), num_features=self.num_features
        )
        self.transformerStandard = DataTransformer(
            scaler=StandardScaler(), num_features=self.num_features
        )
        self.transformerRobust = DataTransformer(
            scaler=RobustScaler(), num_features=self.num_features
        )

    def test_transformer(self):
        with initialize(version_base=None, config_path="../../conf/dataset"):
            cfg: TargetDataset = compose(config_name="test_dataset")

            df = pd.read_csv(cfg.folder_path + cfg.name)
            for transformer in [
                self.transformerMinMax,
                self.transformerRobust,
                self.transformerStandard,
            ]:
                with self.assertRaises(NotFittedError):
                    check_is_fitted(transformer.scaler)
                transformer = transformer.fit(df)
                self.assertIsNone(check_is_fitted(transformer.scaler))

                transform = transformer.transform(df)
                self.assertIsInstance(transform, pd.DataFrame)
                self.assertFalse((transform == df).all().all())


if __name__ == "__main__":
    unittest.main()
