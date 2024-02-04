class myClass:
    def __init__(self):
        self.str=""

    def getString(self):
        self.str=input("enter a string: ")

    def printString(self):
        print(self.str.upper())

s=myClass()
s.getString()
s.printString()