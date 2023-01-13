from uvicorn.workers import UvicornWorker as OriginalUvicornWorker

from gunicorn_pushgateway_workers.workers.base import BaseWorker


class UvicornWorker(BaseWorker, OriginalUvicornWorker):
    pass
