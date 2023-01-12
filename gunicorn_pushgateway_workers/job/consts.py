from ..config import Impl
from .base import PushToGetawayProcess, PushToGetawayThread

IMPL_MAP = {
    Impl.THREAD: PushToGetawayThread,
    Impl.PROCESS: PushToGetawayProcess,
}
