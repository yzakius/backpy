# import pytest
# from argparse import ArgumentTypeError

# import backpy_with_args

# backpy_with_args.TEST_MODE = True


# def test_is_directory():
#     assert backpy_with_args.is_directory('/tmp') == '/tmp'
#     with pytest.raises(ArgumentTypeError):
#         assert backpy_with_args.is_directory('/this_is_not_a_dir')


# def test_is_writable_directory():
#     assert backpy_with_args.is_writable_directory('/tmp') == '/tmp'
#     with pytest.raises(ArgumentTypeError):
#         assert backpy_with_args.is_writable_directory('/root')


# def test_is_file():
#     assert backpy_with_args.is_file('/proc/version') == '/proc/version'
#     with pytest.raises(ArgumentTypeError):
#         backpy_with_args.is_file('/this_is_not_a_file')


# def test_backup_with_equal_source_and_destination():
#     with pytest.raises(Exception):
#         backpy_with_args.backup('/tmp/', '/tmp')
#     with pytest.raises(Exception):
#         backpy_with_args.backup('/tmp', '/tmp/')
