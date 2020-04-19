import os
import tempfile
import pytest
from backpy.backpy import backup


@pytest.fixture()
def cleandir():
    newpath = tempfile.mkdtemp()
    os.chdir(newpath)


def test_returns_error_when_the_destination_does_not_exist():
    source = "/path/test/"
    dest = "/path/test/"
    test = backup(source, dest)
    assert test == "Error: Where is my HD? =("


@pytest.mark.usefixtures("cleandir")
# TODO: Renomear nome do teste
def test_if_sync_works():
    os.mkdir("source")
    for i in range(10):
        open(f"./source/file{i}.txt", "w+")
    os.mkdir("dest")
    source = "./source/"
    dest = "./dest/"
    backup(source, dest)
    for i in range(10):
        assert os.path.exists(f"./dest/file{i}.txt") == True
