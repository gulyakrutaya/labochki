
def aaa(f):
    listtof=[1, 2, 3]

    with open(f, "a") as file:
        file.write(", ".join(str(i) for i in listtof))


def bbb(f):
    with open(f, "r") as file:
        print(file.read())


filename="C:\\Users\\gulbe\\OneDrive\\Рабочий стол\\PP2\\lab6\\dir\\dir4text.txt"

aaa(filename)

bbb(filename)