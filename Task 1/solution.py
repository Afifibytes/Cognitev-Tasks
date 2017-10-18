import os
import sys

if len(sys.argv) != 3:
    print("Usage: python solution.py extensions /path/to/directory")
    exit(1)

extensions = sys.argv[1].split(',')
path = os.listdir(sys.argv[2])

for ext in extensions:
    print("{}: ".format(ext), end="")
    for file in path:
        if file.endswith('.{}'.format(ext)):
            print(file, end=" ")
        if ext == 'c' and file.endswith('.h'):
            print(file, end=" ")
        if ext == 'pl' and file.endswith('pm'):
            print(file, end=" ")
        if ext == 'py' and file.endswith('pyc'):
            print(file, end=" ")
    print()
