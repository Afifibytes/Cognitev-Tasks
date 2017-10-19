import os
import sys

def main():
    if len(sys.argv) == 2:
        path = os.listdir()

    elif len(sys.argv) == 3:
        path = os.listdir(sys.argv[2])

    else:
        print("Usage: python solution.py extensions /path/to/directory")
        exit(1)

    extensions = sys.argv[1].split(',')
    print_files_ext(extensions, path)


def print_files_ext(extensions, path):
    """prints files names with specific extensions in a specific path"""

    for ext in extensions:
        ls = []
        for file in path:
            if file.endswith('.{}'.format(ext)):
                ls.append(file)
            elif ext == 'c' and file.endswith('.h'):
                ls.append(file)
            elif ext == 'pl' and file.endswith('pm'):
                ls.append(file)
            elif ext == 'py' and file.endswith('pyc'):
                ls.append(file)
        if not ls == []:
            print("{}: ".format(ext), end="")
            for i in ls:
                print(i, end=" ")
            print()

if __name__ == '__main__':
    main()
