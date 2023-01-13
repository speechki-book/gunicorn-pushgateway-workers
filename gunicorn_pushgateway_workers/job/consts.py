from gunicorn_pushgateway_workers.config import Impl
from gunicorn_pushgateway_workers.job.base import (
    PushToGetawayProcess,
    PushToGetawayThread,
)

IMPL_MAP = {
    Impl.THREAD: PushToGetawayThread,
    Impl.PROCESS: PushToGetawayProcess,
}
