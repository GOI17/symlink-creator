import os

def create_symlink(source: str, destination: str) -> None:
    if len(source) == 0:
        raise Exception('Source is missing')

    if len(destination) == 0:
        raise Exception('Destination is missing')

    # Print routes
    print('Path where is located: {}'.format(source))
    print('Path to place the symlink: {}'.format(destination))

    os.symlink(src=source, dst=destination, target_is_directory=True)