class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0
    

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length=length

    def area(self):
        return self.length**2


length=int(input("enter the length of the square: "))
sq=Square(length)
print("the area of the square is", sq.area())

sh=Shape()
print("the area of the shape is", sh.area())
            