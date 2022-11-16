import logging
from typing import List, Union

import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler


class DataTransformer(BaseEstimator, TransformerMixin):
    def __init__(
        self,
        scaler: Union[StandardScaler, MinMaxScaler, RobustScaler],
        num_features: List[str],
    ) -> None:
        logging.info("Initialised DataTransformer.")
        self.scaler = scaler
        self.num_features = num_features

    def fit(self, X: pd.DataFrame) -> "DataTransformer":
        logging.info("DataTransformer fitting to data...")

        self.scaler = self.scaler.fit(X[self.num_features])

        logging.info("DataTransformer fitted to data.")

        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        logging.info("Transforming data...")

        X_ = X.copy()
        transformed = pd.DataFrame(
            self.scaler.transform(X_[self.num_features]),
            columns=self.num_features,
        )
        for feature in transformed:
            X_[feature] = transformed[feature]

        logging.info("Data transformed.")

        return X_
