import re

s=input("enter a string: ")

x=re.split("_", s)

new_s=""

for i in x:
    new_s+=i.capitalize()

print(new_s)