from enum import Enum

from pydantic import BaseSettings


class Impl(str, Enum):
    THREAD = "thread"
    PROCESS = "process"


class Config(BaseSettings):
    ENABLED: bool = False
    INTERVAL: int = 60
    HOST: str
    JOB: str
    IMPL: Impl = Impl.THREAD

    class Config:
        env_prefix = "PUSH_GETAWAY_"


config: Config = Config()  # type: ignore
