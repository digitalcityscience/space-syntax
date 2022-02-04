import asyncio
import sys
from time import time
from uuid import uuid4

from convert import osm_to_dxf
from depthmap import analyse
from download import download, create_workdir
from logger import configure_logger, default_logger

async def process(place: str) -> None:
    start = time()
    operation_id = uuid4().hex[:8] + "-" + place.split(",")[0]
    workdir = create_workdir(f"./downloads/{operation_id}")
    log = configure_logger(workdir)
    log.info(f"Starting operation {operation_id}")
    map = download(place, operation_id, workdir)
    dxf = osm_to_dxf(map)
    axial_analysis, segment_analysis = await analyse(dxf)
    log.info("Exported axial files: ", axial_analysis)
    log.info("Exported segment files: ", segment_analysis)
    log.info(f"Operation took {time() - start} seconds")


if __name__ == "__main__":
    try:
        place = sys.argv[1]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(process(place))
    except IndexError:
        print("No place given! Please provide a place in the format: 'City, Country'")
    except Exception:
        default_logger().exception("Error processing place.")
