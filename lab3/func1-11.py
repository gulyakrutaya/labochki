
st=input("enter a string: ")

def pal(s):
    s2=s[::-1]

    if s==s2:
        print("it is a palindrome")
    else:
        print("it is not a palindrome")

pal(st)