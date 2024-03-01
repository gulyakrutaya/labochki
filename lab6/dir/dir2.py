import os

def test_path(path):

    if not os.path.exists(path):
        print("Path does not exist.")
        return
    
    if not os.access(path, os.R_OK):
        print("Path is not readable.")
    else:
        print("Path is readable.")
    
    if not os.access(path, os.W_OK):
        print("Path is not writable.")
    else:
        print("Path is writable.")
    
    if not os.access(path, os.X_OK):
        print("Path is not executable.")
    else:
        print("Path is executable.")


path = 'C:\\Users\\gulbe\\OneDrive\\Рабочий стол\\PP2\\lab4'

test_path(path)
