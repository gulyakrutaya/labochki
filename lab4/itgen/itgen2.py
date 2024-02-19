n=int(input("enter number: "))

def evgen(n):
    for i in range (0, n+1):
        if i%2==0:
            yield i

evlist=[x for x in evgen(n)]
print(*evlist, sep=", ")