num=int(input("enter number: "))

def s(n):
    while n>=0:
        yield n
        n-=1


for nums in s(num):
    print(nums)