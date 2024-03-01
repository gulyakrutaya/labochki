
list=[1, 2, 3, 4]

def pr(l):
    p=1

    for i in l:
        p=eval("p*i")

    return p

print("product is:", pr(list))