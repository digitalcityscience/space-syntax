from download import download, download_administrative_geojson
import json
import os


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
        print("Fixture", fixture)
        print("Result", result)
        assert result == fixture 

