import sys
import ctypes

# Check root privilegies
if ctypes.windll.shell32.IsUserAnAdmin != 0: raise Exception('Run with admin privilegies')

args = sys.argv
# Remove the file name argument
args.pop(0)

if len(args) == 0: raise Exception('Missing args')

if args[0] == 'list':
    from read import get_all_symlinks
    # Remove the selected action
    args.pop(0)
    get_all_symlinks(*args)
elif args[0] == 'create':
    from create import create_symlink
    # Remove the selected action
    args.pop(0)
    create_symlink(*args)
else:
    message = '''
Invalid "{}" argument
Available arguments
    - list: Display all the symlinks of the given path
    - create: Create new symlink
'''
    print(message.format(args[0]))
