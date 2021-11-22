import json
from matplotlib.font_manager import json_load
from osmnx import settings, config, graph, io, geocode_to_gdf, project_gdf
import uuid

utn = settings.useful_tags_node
oxna = settings.osm_xml_node_attrs
oxnt = settings.osm_xml_node_tags
utw = settings.useful_tags_way
oxwa = settings.osm_xml_way_attrs
oxwt = settings.osm_xml_way_tags
utn = list(set(utn + oxna + oxnt))
utw = list(set(utw + oxwa + oxwt))
config(all_oneway=True, useful_tags_node=utn, useful_tags_way=utw)


def download(place: str, operation_id=uuid.uuid4(), workdir="./downloads") -> str:
    print(f"Downloading map for: {place} ...")
    output_file = f"{workdir}/{operation_id}/osm"
    gph = graph.graph_from_place(place, network_type="drive")
    io.save_graph_shapefile(gph, filepath=output_file)
    with open(f"{workdir}/{operation_id}/administrative.geojson", "w") as fp:
        json.dump(download_administrative_geojson(place), fp)
    return output_file


def download_administrative_geojson(place: str) -> str:
    city = geocode_to_gdf(place)
    return json.loads(city.to_json())
