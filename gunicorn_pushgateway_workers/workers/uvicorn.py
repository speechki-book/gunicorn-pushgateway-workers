from uvicorn.workers import UvicornWorker as OriginalUvicornWorker

from .base import BaseWorker


class UvicornWorker(BaseWorker, OriginalUvicornWorker):
    pass
