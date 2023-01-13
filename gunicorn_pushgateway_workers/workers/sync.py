from gunicorn.workers.sync import SyncWorker as OriginalSyncWorker

from gunicorn_pushgateway_workers.workers.base import BaseWorker


class SyncWorker(BaseWorker, OriginalSyncWorker):
    pass
