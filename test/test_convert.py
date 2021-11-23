from cgitb import reset
import filecmp
import os
from convert import osm_to_dxf


def test_osm_to_dxf(tmpdir):
    shape_file = os.path.join(
        os.path.dirname(__file__),
        "fixtures",
        "Balchik_Bulgaria",
        "osm.shp",
    )
    fixture_file = os.path.join(
        os.path.dirname(__file__),
        "fixtures",
        "Balchik_Bulgaria",
        "osm.dxf",
    )

    result = osm_to_dxf(shape_file, tmpdir)
    assert os.path.isfile(result)
    assert filecmp.cmp(fixture_file, result)
