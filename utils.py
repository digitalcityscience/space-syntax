from enum import Enum
from pathlib import Path


class Status(Enum):
    WORKING = 1
    FINISHED = 0
    ERROR = -1


def create_status_file(directory: Path, status: Status) -> None:
    if Path.is_dir(directory):
        # delete WORKING status so that the status can only be in one of the final states
        Path.unlink(directory.joinpath(Status.WORKING.name), missing_ok=True)
        Path.touch(directory.joinpath(status.name))


def create_workdir(workdir: str = "./downloads") -> Path:
    path = Path(workdir)
    path.mkdir(exist_ok=True, parents=True)
    return path
