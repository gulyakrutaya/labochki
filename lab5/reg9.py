import re

pat=r"\w"

s=input("enter a string: ")

x=re.findall(pat, s)

news=""

for i in x:
    if i.isupper():
        news+=" "+i
    else:
        news+=i

print(news)