import enum
from dataclasses import dataclass
from logging import Logger
from pathlib import Path
from typing import List, Union
from uuid import uuid4

import jsonpickle

from logger import configure_logger
from utils import create_workdir

Num = Union[int, str]


@dataclass
class AxialAnalysisConfiguration:
    radii: List[Num]


default_axial = AxialAnalysisConfiguration(radii=[3, "n"])


class SegmentAnalysisType(enum.Enum):
    ANGULAR_TULIP = "tulip"  # (Angular Tulip - Faster)
    ANGULAR_TULIP_CHOICE = "tulip -sic"  # (Angular Tulip - Faster include choice )
    ANGULAR_FULL = "angular"  # (Angular Full - Slower)
    TOPOLOGICAL = "topological"
    METRIC = "metric"


class SegmentAnalysisTulipRadiusType(enum.Enum):
    STEPS = "steps"
    METRIC = "metric"
    ANGULAR = "angular"


@dataclass
class SegmentAnalysisConfiguration:
    type: SegmentAnalysisType
    radius_type: SegmentAnalysisTulipRadiusType
    # (4 to 1024, 1024 approximates full angular)
    tulip_bins: int
    radii: List[Num]


default_segment = SegmentAnalysisConfiguration(
    type=SegmentAnalysisType.ANGULAR_TULIP,
    radius_type=SegmentAnalysisTulipRadiusType.METRIC,
    tulip_bins=1024,
    radii=[300, 1000, "n"],
)


@dataclass
class AnalysisConfiguration:
    axial: AxialAnalysisConfiguration
    segment: SegmentAnalysisConfiguration


DEFAULT_ANALYSIS_CONFIG = AnalysisConfiguration(
    axial=default_axial, segment=default_segment
)


@dataclass
class Configuration:
    place: str
    operation_id: str
    workdir: Path
    log: Logger
    analysis: AnalysisConfiguration


def configure(place: str, root_workdir: str = "./downloads/") -> Configuration:
    operation_id = place.split(",")[0] + "-" + uuid4().hex[:8]
    workdir = create_workdir(f"{root_workdir}/{operation_id}")
    log = configure_logger(workdir)
    return Configuration(
        place=place,
        operation_id=operation_id,
        workdir=workdir,
        log=log,
        analysis=DEFAULT_ANALYSIS_CONFIG,
    )


def dump_config_file(config: Configuration) -> None:
    with open(Path.joinpath(config.workdir, "config.json"), "w", encoding="utf-8") as f:
        f.write(jsonpickle.dumps(config))  # type: ignore
