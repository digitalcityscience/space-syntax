import geopandas as gpd
from os import path


def osm_to_dxf(file_name: str) -> str:
    base_file, _ = path.splitext(file_name)
    dxf_file = base_file + ".dxf"
    print(f"Converting {file_name} to {dxf_file}")
    data = gpd.read_file(file_name)
    data.geometry.to_file(dxf_file, driver="DXF")
    return dxf_file


def mif_to_shp(input: str) -> dict[str, str]:
    data = gpd.read_file(input)
    base_file, _ = path.splitext(input)
    outputs = {"shape": f"{base_file}.shp", "geojson": f"{base_file}.geojson"}
    data.to_file(outputs["shape"])
    data.to_file(outputs["geojson"], driver="GeoJSON")
    return outputs
