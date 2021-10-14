import geopandas as gpd


def osm_to_dxf(file_name: str, output: str) -> None:
    data = gpd.read_file(file_name)
    data.geometry.to_file(output, driver="DXF")


def mif_to_shp(input:str, output: str) -> None:
    data = gpd.read_file(input)
    outputs = { "shape": f"{output}.shp", "geojson": f"{output}.geojson"}
    data.to_file(outputs["shape"])
    data.to_file(outputs["geojson"], driver="GeoJSON")
    print("Exported files: ", outputs)


def main():
    osm_to_dxf("downloads/Alicante, Spain.dxf", "downloads/alicante_spain.osm")
    mif_to_shp("downloads/shapegraph-map.axial.mif", "downloads/shapegraph-map.axial")
    mif_to_shp("downloads/shapegraph-map.segment.mif", "downloads/shapegraph-map.segment")
