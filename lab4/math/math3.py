import math

n=int(input("num of sides: "))
l=float(input("length of a side: "))

print("area is:", n * math.pow(l, 2) / (4 * math.tan(math.pi / n)))