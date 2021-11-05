import os
import sys

def get_all_symlinks(path: str) -> None:    
    if len(path) == 0:
        raise Exception('Path is missing')

    # Store routes to variables
    path = sys.argv[0]

    print('Searched path: {}'.format(path))

    print('List of symlinks')
    for entry in os.scandir(path):
        if entry.is_symlink():
            print(entry.name)