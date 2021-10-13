import geopandas as gpd

# Read file from Shapefile
input = "downloads/Alicante, Spain.osm"
data = gpd.read_file(input)

output = "downloads/Alicante, Spain.dxf"
data.geometry.to_file(output, driver="DXF")