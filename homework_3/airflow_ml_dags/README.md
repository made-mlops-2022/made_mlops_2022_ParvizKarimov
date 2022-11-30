## Homework 3

To run everything:

1. Create FERNET_KEY

```
export FERNET_KEY=$(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")
```

2. Run `docker compose` from this folder

```
docker-compose up --build
```

Now you can access `airflow` on `localhost:8080`.

To run DAG tests:

3. Execute `pytest` on docker:

```
docker exec -it airflow-examples-main_scheduler_1 pytest tests/
```

NOTE: When starting docker compose, you may notice something like "PASSWORD is not set". It is completely normal unless you want to send us messages on failures and retries :). If you want to - contact us, we'll create temporary password just for you.
An example of how this looks will be attached to PR.
