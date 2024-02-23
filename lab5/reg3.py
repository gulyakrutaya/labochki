import re

pat=r"[a-z_]+"

s=input("enter a string: ")

if re.match(pat, s):
    print("string has matched")

else:
    print("string has not matched")