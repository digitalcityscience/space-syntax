import json
import os
from pathlib import Path

from download import download_administrative_geojson, download_drive_graph_from_place, create_workdir

def test_create_workdir_default():
    test_dir = create_workdir()
    assert test_dir.exists()
    assert test_dir.is_dir()
    assert test_dir.stem == "downloads"

def test_create_workdir_new(tmpdir):
    test_dir = create_workdir(Path(tmpdir).joinpath("downloads"))
    assert test_dir.exists()
    assert test_dir.is_dir()
    assert test_dir.stem == "downloads"    

def test_download_administrative_geojson():
    fixture_file = os.path.join(
        os.path.dirname(__file__),
        "fixtures",
        "Balchik_Bulgaria",
        "administrative.geojson",
    )
    with open(fixture_file, "r") as file:
        fixture = json.load(file)
        result = download_administrative_geojson("Balchik, Bulgaria")
        # place_id seems to differ from time to time
        result["features"][0]["properties"]["place_id"] = "XXX"
        fixture["features"][0]["properties"]["place_id"] = "XXX"
        assert result == fixture


def test_download_drive_graph_from_place():
    result = download_drive_graph_from_place("Balchik, Bulgaria")
    assert result.number_of_nodes() == 1766
    assert result.number_of_edges() == 2432
