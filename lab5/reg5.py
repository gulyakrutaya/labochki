import re

pat=r"a[a-zA-Z-_0-9]*b"

s=input("enter a string: ")

if re.match(pat, s):
    print("string has matched")

else:
    print("string has not matched")