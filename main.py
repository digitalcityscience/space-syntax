from uuid import uuid4
from depthmap import analyse
from download import download
from convert import mif_to_shp, osm_to_dxf
import sys
import asyncio
from time import time


async def process(place: str) -> None:
    start = time()
    operation_id = uuid4()
    print(f"Starting operation {operation_id}")
    map = download(place, operation_id)
    dxf = osm_to_dxf(map)
    axial_analysis, segment_analysis = await analyse(dxf)
    out_axial = mif_to_shp(axial_analysis)
    print("Exported axial files: ", out_axial)
    out_segment = mif_to_shp(segment_analysis)
    print("Exported segment files: ", out_segment)
    print(f"Operation took {time() - start} seconds")


if __name__ == "__main__":
    try:
        place = sys.argv[1]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(process(place))
    except IndexError:
        print("No place given! Please provide a place in the format: 'City, Country'")
