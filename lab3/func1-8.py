
nums=input("enter numbers: ").split()

myList=[int(x) for x in nums]



def has_007(l):
    for i in range(len(l)):
        if l[i]==0:
            for j in range(i+1, len(l)):
                if l[j]==7:
                    break
                elif l[j]==0:
                    for k in range(j+1, len(l)):
                        if l[k]==7:
                            return True
    return False



if has_007(myList):
    print("True")
else:
    print("False")