from osmnx import settings, config, graph, io
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


def download(place: str, operation_id = uuid.uuid4()) -> str:
    print(f"Downloading map for: {place} ...")
    output_file = f"./downloads/{operation_id}.osm"
    gph = graph.graph_from_place(place, network_type="drive")
    io.save_graph_shapefile(gph, filepath=output_file)
    return output_file
