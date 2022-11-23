## Homework 2

Model inference in `fastapi_app.py`. It contains `/predict` and `/health` endpoints.

"Workability" may be checked either via running `requests_script.py` or checking through `localhost:8000/docs`. 

`/predict` endpoint has some unittests.

### Running everything

To run docker:

- Pull:
```docker pull ippk93/mlops_hw```

- Run:
```docker run -it -p 8000:8000 ippk93/mlops_hw```

Check "workability":

- Run tests: 
```pytest```

- Check requests script (from this dir in local machine)
```python requests_script.py```

- Via FastAPI Swagger - run in following URL:
```localhost:8000/docs```

### About model:

Model is loaded from ya-disk (via yadisk lib). Script in `load_model.py`. It should automatically run with docker container. Loading paths are stored in `.env` file.

### About image optimisations:

We've tried to make it in 2 ways:

1) Load from `alpine` images. Both `python:3.9-alpine` and `alpine` were used, final version via `alpine` is stored in `Dockerfile.alpine` file. Build takes about 20 minutes and resulting image is about 1gb (which is better than plain `python:3.9` image but not much).

2) Load from `python:3.9-slim` image. This one takes about a minute to build and uses ~540mb memory (which is a little confusing:) ). 

Also, `.dockerignore` files were used to not copy unneed files&directories. Number of layers (i.e. commands in Dockerfile) is kept as little as we could come up to.

That said, the final version is the second one, it was loaded to DockerHub.

### About validation

Simple validation checks are performed by choosing correct `pydantic` types in their respective models. Nothing special, only type and range checks. Status code on validation error is overriden to 400 (default was 422).

### Other

Note that already preprocessed data is needed for model to make predictions.

Data for running `requests_script.py` is stored in `data` folder.

Just in case something goes wrong with model loading from disk, you can change `MODEL_PATH` parameter in `.env` file to the model in `models` folder.
It is not needed otherwise (you can even delete it if you want).