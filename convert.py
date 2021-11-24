import geopandas as gpd
from os import path


def construct_destination_filepath(origin_file: str, destination_path=None) -> str:
    if destination_path is None:
        base_file, _ = path.splitext(origin_file)
    else:
        _, original_file_name = path.split(origin_file)
        base_file = path.join(destination_path, original_file_name)
    return base_file


def osm_to_dxf(osm_folder: str, destination=None) -> str:
    dxf_file = construct_destination_filepath(osm_folder, destination) + ".dxf"
    print(f"Converting {osm_folder} to {dxf_file}")
    # if the file is not specified linux defaults to nodes.shp
    data = gpd.read_file(path.join(osm_folder, "edges.shp"))
    data.geometry.to_file(dxf_file, driver="DXF")
    return dxf_file


def mif_to_shp(input: str, destination=None) -> dict[str, str]:
    data = gpd.read_file(input)
    base_file = construct_destination_filepath(input, destination)
    outputs = {"shape": f"{base_file}.shp", "geojson": f"{base_file}.geojson"}
    data.to_file(outputs["shape"])
    data.to_file(outputs["geojson"], driver="GeoJSON")
    return outputs
