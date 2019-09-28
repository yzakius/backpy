import argparse
import os


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


parser = argparse.ArgumentParser(description='A simple backup tool written in python.')
parser.add_argument('--source', dest='sources', type=is_directory, metavar='DIR', nargs='+', required=True,
                    help='Source directories.')
parser.add_argument('--destination', dest='destinations', type=is_writable_directory, metavar='DIR', nargs='+',
                    required=True,
                    help='Destination directories.')
parser.add_argument('--exclude-from', dest='exclude_from', type=is_file, metavar='FILE',
                    help='File with pattern of files and directories to exclude.')
args = parser.parse_args()


# sources = [source for source in args.sources if is_directory(source)]
# destinations = [destination for destination in args.destinations if is_writable_directory(destination)]
sources = args.sources
destinations = args.destinations


def notify(message: str):
    print(f'    - {message}')


def backup(source: str, destination: str):
    backup_cmd = f'rsync -azvP --delete {source} {destination}'
    if args.exclude_from:
        backup_cmd += f' --exclude-from={args.exclude_from}'
    os.system(backup_cmd)
    notify(f'{source} -> {destination}')


def init():
    for source in sources:
        for destination in destinations:
            backup(source, destination)


if __name__ == '__main__':
    init()
