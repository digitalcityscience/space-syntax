import asyncio
import sys
from time import time
import datetime
from convert import osm_to_dxf
from depthmap import analyse
from download import download
from logger import default_logger
import config
import utils


async def process(cfg: config.Configuration) -> None:
    start = time()
    utils.create_status_file(cfg.workdir, utils.Status.WORKING)
    config.dump_config_file(cfg)
    cfg.log.info(f"Starting operation {cfg.operation_id}")
    cfg.log.info("Downloading osm files...")
    map = download(place, cfg.operation_id, cfg.workdir)
    cfg.log.info(
        f"Downloading osm files took {datetime.timedelta(seconds=(time() - start))}"
    )
    dxf = osm_to_dxf(map)
    axial_analysis, segment_analysis = await analyse(dxf, cfg.analysis)
    cfg.log.info("Exported axial files: ", axial_analysis)
    cfg.log.info("Exported segment files: ", segment_analysis)
    cfg.log.info(
        f"Operation {cfg.operation_id} took {datetime.timedelta(seconds=(time() - start))}"
    )
    utils.create_status_file(cfg.workdir, utils.Status.FINISHED)


if __name__ == "__main__":
    cfg = None
    try:
        place = sys.argv[1]
        cfg = config.configure(place)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(process(cfg))
    except IndexError:
        print("No place given! Please provide a place in the format: 'City, Country'")
    except Exception:
        if cfg is not None:
            utils.create_status_file(cfg.workdir, utils.Status.ERROR)
        default_logger().exception("Error processing place.")
