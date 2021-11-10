import asyncio
import sys
from time import time
from uuid import uuid4

from convert import osm_to_dxf
from depthmap import analyse
from download import download


async def process(place: str) -> None:
    start = time()
    operation_id = uuid4().hex[:8] + "-" + place.split(",")[0]
    print(f"Starting operation {operation_id}")
    map = download(place, operation_id)
    dxf = osm_to_dxf(map)
    axial_analysis, segment_analysis = await analyse(dxf)
    print("Exported axial files: ", axial_analysis)
    print("Exported segment files: ", segment_analysis)
    print(f"Operation took {time() - start} seconds")


if __name__ == "__main__":
    try:
        place = sys.argv[1]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(process(place))
    except IndexError:
        print("No place given! Please provide a place in the format: 'City, Country'")
