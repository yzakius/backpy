import os
import shutil
from decouple import config

dest = config("dest")
source = config("source")


def message(begin_space, end_space):
    nl = "\n"
    begin_usage = begin_space[0]
    end_usage = end_space[0]
    begin_free = begin_space[1]
    end_free = end_space[1]
    usage = f"- Begin Usage: {begin_usage} {nl} - End Usage: {end_usage}"
    free = f"- Begin Free Space: {begin_free} {nl} - End Free Space: {end_free}"
    message = f"Backup is done! {nl} {usage} {nl} {free} {nl} "
    return message


def backup(source, dest):
    if os.path.exists(dest):
        begin_space = diff_space(dest)
        os.system(f"sudo rsync -azhuvP --progress --delete {source} {dest}")
        end_space = diff_space(dest)
        return message(begin_space, end_space)
    else:
        return "Error: Where is my HD? =("


def diff_space(dest):
    hdd = shutil.disk_usage(dest)
    usage = round(hdd[1] / (2 ** 30))
    free = round(hdd[2] / (2 ** 30))
    return usage, free

print(backup(source, dest))