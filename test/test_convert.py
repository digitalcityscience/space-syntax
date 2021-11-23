import filecmp
import os
from convert import construct_destination_filepath, mif_to_shp, osm_to_dxf


def fixture_path(file: str) -> str:
    return os.path.join(os.path.dirname(__file__), "fixtures", "Balchik_Bulgaria", file)


def test_osm_to_dxf(tmpdir):
    shape_file = fixture_path("osm.shp")
    fixture_file = os.path.join(
        os.path.dirname(__file__),
        "fixtures",
        "Balchik_Bulgaria",
        "osm.dxf",
    )

    result = osm_to_dxf(shape_file, tmpdir)
    assert os.path.isfile(result)
    assert filecmp.cmp(fixture_file, result)


def test_construct_destination_filepath_with_destination():
    result = construct_destination_filepath("/some/path/and.file", "/new/path")
    assert "/new/path/and.file" == result


def test_construct_destination_filepath_without_destination():
    result = construct_destination_filepath("/some/path/and.file")
    assert "/some/path/and" == result


def test_mif_to_shp(tmpdir):
    mif_file = fixture_path("osm.axial.mif")
    result = mif_to_shp(mif_file, tmpdir)
    assert os.path.isfile(result["shape"])
    assert os.path.isfile(result["geojson"])
    assert filecmp.cmp(result["shape"], fixture_path("osm.axial.shp"))
    assert filecmp.cmp(result["geojson"], fixture_path("osm.axial.geojson"))
