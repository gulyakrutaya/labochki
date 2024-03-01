
def count_l(f):
    with open(f, "r") as file:
        num=0
        for line in file:
            num+=1
    return num


filename="C:\\Users\\gulbe\\OneDrive\\Рабочий стол\\PP2\\lab6\\dir\\dir4text.txt"
print("num of lines:", count_l(filename))