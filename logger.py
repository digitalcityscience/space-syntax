import logging
from pathlib import Path

LOGGER_NAME = "space-syntax"

def configure_logger(workdir: Path = Path.cwd()) -> logging.Logger:
    logger = default_logger()
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(Path(workdir).joinpath("logfile.log"))
    formatter = logging.Formatter(
        "%(asctime)s : %(levelname)s : %(name)s : %(message)s"
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger


def default_logger() -> logging.Logger:
    return logging.getLogger(LOGGER_NAME)
