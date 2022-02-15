import config
from logger import LOGGER_NAME


def test_configure(tmpdir):
    configuration = config.configure("TestCity", tmpdir)
    assert configuration.place == "TestCity"
    assert configuration.log.name == LOGGER_NAME
    assert configuration.workdir.match("TestCity-*")
    assert "TestCity" in configuration.operation_id
