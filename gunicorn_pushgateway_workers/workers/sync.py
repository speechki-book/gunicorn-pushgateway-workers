from gunicorn.workers.sync import SyncWorker as OriginalSyncWorker

from .base import BaseWorker


class SyncWorker(BaseWorker, OriginalSyncWorker):
    pass
