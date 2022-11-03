
For this to work you need to download the original dataset, but...it's already here for CI testing (in `ml_project/data/raw/`).

NOTE: All given commands should be run from here. Otherwise we won't guarantee that you will be able to run the project.

Install deps:
```
pip install -e ml_project
```

Generate processed dataset:
```
make_dataset
```
Optional parameters may be seen in `ml_project/ml_project/conf/make_dataset.yaml`, but we suggest not changing them.

Train:
```
train_model
```
Optionally pass `fit`=`all` or `split` (`split` generates metric in `ml_project/models` directory), `model_path`=*path to the model* `model`=`svm` or `random_forest`, `split`=`stratified` or `simple`. All model data is saved in `ml_project/models`

Predict:
```
predict
```
Optionally pass `model_path`=*path to the model* and `predict_path`=*path to save predictions*

Generate fake dataset:
```
generate_data
```
Optional parameters may be seen in `ml_project/ml_project/conf/generate_data.yaml`, but we suggest not changing them.

Run tests:
```
python3 ml_project/ml_project/tests/run_tests.py
```