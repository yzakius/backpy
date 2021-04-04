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
def test_if_sync_works():
    os.mkdir("source")
    for i in range(10):
        open(f"./source/file{i}.txt", "w+")
    os.mkdir("dest")
    source = "./source/"
    dest = "./dest/"
    backup(source, dest)
    for i in range(10):
        assert os.path.exists(f"./dest/file{i}.txt")


@pytest.mark.usefixtures("cleandir")
def test_returns_message_sync_when_sync_complete():
    os.mkdir("source")
    for i in range(10):
        open(f"./source/file{i}.txt", "w+")
    os.mkdir("dest")
    source = "./source/"
    dest = "./dest/"
    result = backup(source, dest)
    nl = "\n"
    usage = f"- Begin Usage: 0 {nl} - End Usage: 0"
    free = f"- Begin Free Space: 4 {nl} - End Free Space: 4"
    message = f"Backup is done! {nl} {usage} {nl} {free} {nl} "
    assert result == message


# TODO: See a way to mock a directory size
# def test_returns_correct_difference_of_disk_space():
#     pass
