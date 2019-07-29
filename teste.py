import os

destination = '/run/media/yzakius/backup/backup/yzakius/'
source = '/home/yzakius/'
backup_cmd = f'sudo rsync -azvP --delete {source} {destination}'

if os.path.exists(destination):
    os.system(backup_cmd)
else:
    print("Where is my hd? =(")
