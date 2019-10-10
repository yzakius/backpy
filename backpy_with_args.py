import argparse
import os

TEST_MODE = False


class BackupWithEqualSourceAndDestination(Exception):
    pass


def is_directory(path: str) -> str:
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f'{path} is not a valid directory.')


def is_writable_directory(path: str) -> str:
    if is_directory(path) and not os.access(path, os.W_OK):
        raise argparse.ArgumentTypeError(f'{path} is not a writable directory.')
    return path


def is_file(filename: str) -> str:
    if os.path.isfile(filename) and os.access(filename, os.R_OK):
        return filename
    else:
        raise argparse.ArgumentTypeError(f'{filename} is not a readable file.')


def notify(message: str):
    print(f'    - {message}')


def backup(source: str, destination: str, exclude_from: str = None):
    if os.path.abspath(source) == os.path.abspath(destination):
        raise BackupWithEqualSourceAndDestination(f'Source and destination are equal: {source}')

    backup_cmd = f'rsync -azvP --delete {source} {destination}'
    if exclude_from:
        backup_cmd += f' --exclude-from={exclude_from}'
    if not TEST_MODE:
        os.system(backup_cmd)
    notify(f'{source} -> {destination}')


def init():
    parser = argparse.ArgumentParser(description='A simple backup tool written in python.')
    parser.add_argument('--source', dest='sources', type=is_directory, metavar='DIR', nargs='+', required=True,
                        help='Source directories.')
    parser.add_argument('--destination', dest='destinations', type=is_writable_directory, metavar='DIR', nargs='+',
                        required=True,
                        help='Destination directories.')
    parser.add_argument('--exclude-from', dest='exclude_from', type=is_file, metavar='FILE',
                        help='File with pattern of files and directories to exclude.')
    args = parser.parse_args()

    sources = args.sources
    # sources = [source for source in args.sources if is_directory(source)]
    sources = [os.path.abspath(source) for source in sources]

    destinations = args.destinations
    # destinations = [destination for destination in args.destinations if is_writable_directory(destination)]
    destinations = [os.path.abspath(destination) for destination in destinations]
    exclude_from = args.exclude_from

    for source in sources:
        for destination in destinations:
            backup(source, destination, exclude_from)


if __name__ == '__main__':
    init()
