import os
import pathlib
import py
from utils import Status, create_status_file, create_workdir

def test_create_workdir_default():
    test_dir = create_workdir()
    assert test_dir.exists()
    assert test_dir.is_dir()
    assert test_dir.stem == "downloads"


def test_create_workdir_new(tmpdir):
    test_dir = create_workdir(pathlib.Path(tmpdir).joinpath("downloads"))  # type: ignore
    assert test_dir.exists()
    assert test_dir.is_dir()
    assert test_dir.stem == "downloads"


def check_status_file_exists(tmpdir: py.path.local, status: Status):
    create_status_file(pathlib.Path(tmpdir), status)
    assert os.path.isfile(tmpdir.join(status.name))


def test_create_status_file_working(tmpdir: py.path.local):
    check_status_file_exists(tmpdir, Status.WORKING)


def test_create_status_file_error(tmpdir: py.path.local):
    check_status_file_exists(tmpdir, Status.ERROR)


def test_create_status_file_finished(tmpdir: py.path.local):
    check_status_file_exists(tmpdir, Status.FINISHED)


def test_create_status_file_no_working_after_finished(tmpdir: py.path.local):
    check_status_file_exists(tmpdir, Status.WORKING)
    check_status_file_exists(tmpdir, Status.FINISHED)
    assert os.path.isfile(tmpdir.join(Status.WORKING.name)) is False
