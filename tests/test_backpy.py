from backpy.backpy import backup


def test_returns_error_when_the_destination_does_not_exist():
    source = "/path/test/"
    dest = "/path/test/"
    test = backup(source, dest)
    assert test == "Error: Where is my HD? =("
