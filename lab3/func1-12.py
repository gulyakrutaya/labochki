

nums=input("enter numbers: ").split()

myList=[int(x) for x in nums]


def histogram(l):
    for x in l:
        print("*"*x)


histogram(myList)
              