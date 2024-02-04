
nums=input("enter numbers: ").split()

myList=[int(x) for x in nums]

def filter_prime(l):
    primeList=[]
    
    for num in l:
        div=2
        while div<num:
            if num%div!=0:
                div+=1
            else:
                break
        if num==div and num>1:
            primeList.append(num)

    print(primeList)

filter_prime(myList)
