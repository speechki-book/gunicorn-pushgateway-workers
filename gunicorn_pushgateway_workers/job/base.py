from multiprocessing import Process
import platform
from threading import Thread
from time import sleep

from ..config import config
from ..metrics import get_registry, push


class BasePushToGetaway:
    def __init__(self, *args, **kwargs) -> None:
        kwargs["daemon"] = True
        super().__init__(*args, **kwargs)

    def run(self) -> None:
        registry = get_registry()
        grouping_key = {
            "node": platform.node(),
        }

        while True:
            sleep(config.INTERVAL)
            push(registry, grouping_key=grouping_key)


class PushToGetawayThread(BasePushToGetaway, Thread):
    pass


class PushToGetawayProcess(BasePushToGetaway, Process):
    pass
