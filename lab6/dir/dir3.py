import os

def test_path(path):

    if not os.path.exists(path):
        print("Path does not exist.")
        return
    else:
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    



path = 'C:\\Users\\gulbe\\OneDrive\\Рабочий стол\\PP2\\lab4'

test_path(path)