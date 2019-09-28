#!./bin/python

import argparse
import os

parser = argparse.ArgumentParser(description='A simple backup tool written in python.')
parser.add_argument('--source', dest='sources', metavar='DIR', nargs='+',
                    help='Source directories')
parser.add_argument('--destination', dest='destinations', metavar='DIR', nargs='+',
                    help='Destination directories')
args = parser.parse_args()

# TODO: also use a configuration file
# ENHANCEMENT: inform destinations not found
# ENHANCEMENT: when running script without source and target, suggest using last valid configuration
sources = args.sources
destinations = args.destinations
destinations = [destination for destination in destinations if os.path.exists(destination)]


def notify(message):
    print(f'    - {message}')
    # TODO: use libnotify notifications


def backup(source, destination):
    # backup_cmd = f'rsync -azvP --delete {source} {destination} --exclude-from=exclude.txt'
    backup_cmd = f'rsync -azvP --delete {source} {destination}'
    os.system(backup_cmd)
    notify(f'{source} -> {destination}')


for source in sources:
    for destination in destinations:
        backup(source, destination)


# ENHANCEMENT: play an audio to indicate the end of the script
