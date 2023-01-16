from enum import Enum

from pydantic import BaseSettings, validator


class Impl(str, Enum):
    THREAD = "thread"
    PROCESS = "process"


class Config(BaseSettings):
    ENABLED: bool = False
    INTERVAL: int = 60
    HOST: str = ""
    JOB: str = ""
    IMPL: Impl = Impl.THREAD

    @validator("HOST", "JOB")
    def reqired_if_enabled(cls, v, values):
        if values["ENABLED"] and not v:
            raise ValueError("Required")
        return v

    class Config:
        env_prefix = "PUSH_GETAWAY_"


config: Config = Config()  # type: ignore
