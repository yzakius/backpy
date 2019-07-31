import os

# TODO: use command line parameter
# TODO: also use a configuration file
# ENHANCEMENT: inform destinations not found
# ENHANCEMENT: when running script without source and target, suggest using last valid configuration
sources = []
destinations = []
destinations = [destination for destination in destinations if os.path.exists(destination)]


def notify(message):
    print(f'    - {message}')
    # TODO: use libnotify notifications


def backup(source, destination):
    backup_cmd = f'sudo rsync -azvP --delete {source} {destination}'
    # os.system(backup_cmd)
    notify(f'{source} -> {destination}')


for source in sources:
    for destination in destinations:
        backup(source, destination)
