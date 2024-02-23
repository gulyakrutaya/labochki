import re

s=input("enter a string: ")

x=re.split("[A-Z]", s)

new_s=""

for i in x:
    new_s=new_s+" "+i

print(new_s)