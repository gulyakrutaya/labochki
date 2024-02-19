num=int(input("enter number: "))

def sq(n):
    for i in range(1, n+1):
        if i**2<n:
            yield i**2


for nums in sq(num):
    print(nums)