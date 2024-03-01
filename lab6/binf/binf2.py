
str="aaa"

def c(s):
    
    up=sum(1 for i in s if i.isupper())
    lo=sum(1 for k in s if k.islower())

    return up, lo

u, l=c(str)

print("Uc num:", u, "\nLC num:", l)