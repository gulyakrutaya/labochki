from func1_4 import filter_prime 
from func1_7 import has_33 

listok=list(map(int, input.split("enter your numbers: ")))

def filter33(input_list):
    prime_list = filter_prime(input_list)
    return has_33(prime_list)


print(filter33(listok))