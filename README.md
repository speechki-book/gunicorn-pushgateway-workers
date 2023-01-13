# gunicorn-pushgateway-workers

## Usage
1. [Enable multiprocess mode](https://github.com/prometheus/client_python#multiprocess-mode-eg-gunicorn)

2. [Set worker class](https://docs.gunicorn.org/en/stable/settings.html#worker-class)

    Available workers:
   * gunicorn_pushgateway_workers.workers.sync.SyncWorker (default in gunicorn)
   * gunicorn_pushgateway_workers.workers.uvicorn.UvicornWorker


## Configuration (env)

* PUSH_GETAWAY_ENABLED: bool (default `False`)
* PUSH_GETAWAY_HOST: str
* PUSH_GETAWAY_JOB: str
* PUSH_GETAWAY_INTERVAL: int (seconds, default `60`)
* PUSH_GETAWAY_IMPL: str (`thread` or `process`, default `thread`)
