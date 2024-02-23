import re

pat=r"[,. ]+"

r=":"

s=input("enter a string: ")

new_s=re.sub(pat, r, s)

print(new_s)