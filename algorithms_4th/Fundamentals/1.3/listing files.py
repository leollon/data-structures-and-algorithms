"""1.3.43 Listing files.
A folder is a list of files and folders. Write a program that takes the
name of a folder as a command-line argument and prints out all of the files contained
in that folder, with the contents of each folder recursively listed (indented) under that
folder’s name.
"""
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Listing files.")
parser.add_argument('-d', '--dir', help='Specify a directory to list files')


def list_files(dir, indent=4):
    for p in Path(dir).iterdir():
        if p.is_dir():
            print(' ' * indent + str(p).rsplit('/', maxsplit=1)[-1])
            list_files(p, indent + 4)
        else:
            print(' ' * indent + str(p).rsplit('/', maxsplit=1)[-1])


if __name__ == "__main__":
    dir = parser.parse_args()
    if not dir.dir:
        dir.dir = '.'
    print(dir.dir.rsplit('/', maxsplit=1)[-1])
    list_files(dir.dir)
