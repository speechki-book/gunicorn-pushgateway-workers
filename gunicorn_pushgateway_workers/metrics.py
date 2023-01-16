import logging
from typing import Any

from prometheus_client import CollectorRegistry, multiprocess, push_to_gateway

from gunicorn_pushgateway_workers.config import config

logger = logging.getLogger(__name__)


def get_registry() -> CollectorRegistry:
    registry: CollectorRegistry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)

    return registry


def push(registry: CollectorRegistry, grouping_key: dict[str, Any]) -> None:
    try:
        push_to_gateway(
            gateway=config.HOST,
            job=config.JOB,
            registry=registry,
            grouping_key=grouping_key,
        )
    except OSError as e:
        logger.error(e)
