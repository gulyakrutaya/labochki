import re

pat=r"[A-Z][a-z]+"

s=input("enter a string: ")

if re.match(pat, s):
    print("string has matched")

else:
    print("string has not matched")