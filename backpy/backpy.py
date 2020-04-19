import os

dest = '/run/media/yzakius/backup/backup/yzakius/'
source = '/home/yzakius/'


def backup(source, dest):
    if os.path.exists(dest):
        return os.system(
            f'sudo rsync -azvP --delete {source} {dest}'
        )
    else:
        # TODO: use main
        return "Error: Where is my HD? =("


backup(source, dest)
