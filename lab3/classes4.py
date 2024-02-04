import math

class Point:

    def __init__(self, x, y):
        self.x=x
        self.y=y

    def show(self):
        return f"({self.x}, {self.y})"
    def move(self, newx, newy):
        self.x=newx
        self.y=newy
    
    def dist(self, x1, x2, y1, y2):
        self.d=math.sqrt((x1-x2)**2+(y1-y2)**2)
        return self.d
    

x1=int(input("enter x coordinate: "))
y1=int(input("enter y coordinate: "))
p1=Point(x1, y1)

print("coordinates of the point:", p1.show())

x2=int(input("enter new x coordinate: "))
y2=int(input("enter new y coordinate: "))

p1.move(x2, y2)

print("new coordinates of the point:", p1.show())

x3=int(input("enter x coordinate of the 1 point: "))
y3=int(input("enter y coordinate of the 1 point: "))

x4=int(input("enter x coordinate of the 2 point: "))
y4=int(input("enter y coordinate of the 2 point: "))

print("the distance between them is", p1.dist(x3, x4, y3, y4))