def squares(a, b):
    for i in range(a, b+1):
        yield i**2


a=int(input("enter number a: "))
b=int(input("enter number b: "))

for square in squares(a, b):
    print(square)
