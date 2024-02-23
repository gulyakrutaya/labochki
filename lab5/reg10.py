import re

s=input("enter a string: ")

new_s=""

pat=r"\w"

x=re.findall(pat, s)

for i in x:
    if i.isupper() and i!=x[0]:
        new_s+="_"+i
    else:
        new_s+=i

print(new_s)