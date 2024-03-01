import os

def list_specific(path):
    
    directories = [item for item in os.listdir(path) if os.path.isdir(item)]

    files = [item for item in os.listdir(path) if os.path.isfile(item)]

    return directories, files

def list_all(path):
    
    all_directories = []
    all_files = []

    w=os.walk(path)

    for (p, d, f) in w:
        all_directories.extend(d)
        all_files.extend(f)
    return all_directories, all_files

path = 'C:\\Users\\gulbe\\OneDrive\\Рабочий стол\\PP2\\lab4'

directories, files = list_specific(path)
print("Directories in this path:", directories)
print("Files in this path:", files)

all_directories, all_files = list_all(path)
print("All Directories in this path:", all_directories)
print("All Files in this path:", all_files)