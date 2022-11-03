from ml_project.models.train_model import train_model, get_data
import unittest
from unittest.mock import patch, Mock


class TestTrainModel(unittest.TestCase):
    def test_get_data():
        X, y = get_data()

    def test_train_model(self):
        train_model.cfg = Mock()
        train_model()

if __name__ == '__main__':
    unittest.main()
