from threading import Lock

from gunicorn_pushgateway_workers.config import config
from gunicorn_pushgateway_workers.job.consts import IMPL_MAP

JOB_CLASS = IMPL_MAP[config.IMPL]


class BaseWorker:
    __lock = Lock()
    __started = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__start()

    @classmethod
    def __start(cls):
        if not config.ENABLED:
            return

        with cls.__lock:
            if cls.__started:
                return

            JOB_CLASS().start()
            cls.__started = True
