import string

def ggg():
    for l in string.ascii_uppercase:
        filename = f"{l}.txt" 
        with open(filename, 'w') as file:
            file.write("blablabla")

ggg()