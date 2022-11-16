import unittest
from unittest.mock import Mock

from ml_project.models.train_model import get_data, train_model  # noqa


class TestTrainModel(unittest.TestCase):
    def test_get_data(self):
        pass
        # X, y = get_data()

    def test_train_model(self):
        pass
        train_model.cfg = Mock()
        train_model()


if __name__ == "__main__":
    unittest.main()
