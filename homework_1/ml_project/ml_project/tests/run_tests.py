import unittest

from ml_project.tests.data.test_make_dataset import TestMakeDataset  # noqa
from ml_project.tests.features.test_transformer import TestTransformer  # noqa
from ml_project.tests.generate_fake_dataset import generate
from ml_project.tests.models.test_predict_model import TestPredict  # noqa
from ml_project.tests.models.test_train_model import TestTrainModel  # noqa

if __name__ == "__main__":
    generate()
    unittest.main()
