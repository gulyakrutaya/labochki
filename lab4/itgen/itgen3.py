n=int(input("enter number: "))

def evgen(n):
    for i in range (0, n+1):
        if i%3==0 and i%4==0:
            yield i

evlist=[x for x in evgen(n)]
print(*evlist, sep=", ")