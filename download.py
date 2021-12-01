import json
from osmnx import settings, config, graph, io, geocode_to_gdf
import uuid
from typing import Any
from pathlib import Path

utn = settings.useful_tags_node
oxna = settings.osm_xml_node_attrs
oxnt = settings.osm_xml_node_tags
utw = settings.useful_tags_way
oxwa = settings.osm_xml_way_attrs
oxwt = settings.osm_xml_way_tags
utn = list(set(utn + oxna + oxnt))
utw = list(set(utw + oxwa + oxwt))
config(all_oneway=True, useful_tags_node=utn, useful_tags_way=utw)

def create_workdir(workdir="./downloads") -> Path:
    path = Path(workdir)
    path.mkdir()
    return path

def download(place: str, operation_id=uuid.uuid4(), workdir="./downloads") -> str:
    print(f"Downloading map for: {place} ...")
    output_file = f"{workdir}/{operation_id}/osm.shp"
    io.save_graph_shapefile(
        download_drive_graph_from_place(place), filepath=output_file
    )
    with open(f"{workdir}/{operation_id}/administrative.geojson", "w") as fp:
        json.dump(download_administrative_geojson(place), fp)
    return output_file


def download_drive_graph_from_place(place: str) -> Any:
    return graph.graph_from_place(place, network_type="drive")

def download_administrative_geojson(place: str) -> Any:
    city = geocode_to_gdf(place)
    return json.loads(city.to_json())
