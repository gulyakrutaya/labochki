
nums=input("enter numbers: ").split()
mylist=[int(x) for x in nums]


def isPrime(x):
    if x<2:
        return False
    for i in range(2, x):
        if x%i==0:
            return False
    return True


primes=filter(lambda n:isPrime(n), mylist)
print(list(primes))