import os

file="C:\\Users\\gulbe\\OneDrive\\Рабочий стол\\PP2\\lab6\\dir\\dir8text.txt"

def deletor(f):

    if not os.path.exists(f):
        print("path does not exist")
    else:
        if not os.access(f, os.X_OK):
            print("you do not have access to this file")
        else:
            os.remove(f)
            print("you have successfully deleted the file")
deletor(file)