
nums=input("enter numbers: ").split()

myList=[int(x) for x in nums]

def has_33(l):
    for i in range(1, len(l)):
        if l[i]==3 and l[i-1]==3:
            return True
    return False

if has_33(myList):
    print("True")
else:
    print("False")