
myList=input("enter elements: ").split()



def uq(l):
    newL=[]

    for x in l:
        if l.count(x)>1:
            continue
        else:
            newL.append(x)


    print(newL)

uq(myList)