from dataclasses import dataclass
from logging import Logger
from pathlib import Path
from uuid import uuid4

from download import create_workdir
from logger import configure_logger


@dataclass
class Configuration:
    place: str
    operation_id: str
    workdir: Path
    log: Logger


def configure(place: str, root_workdir: str = "./downloads/") -> Configuration:
    operation_id = place.split(",")[0] + "-" + uuid4().hex[:8]
    workdir = create_workdir(f"{root_workdir}/{operation_id}")
    log = configure_logger(workdir)
    return Configuration(
        place=place, operation_id=operation_id, workdir=workdir, log=log
    )
