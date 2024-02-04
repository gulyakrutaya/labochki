heads=int(input("enter number of heads "))
legs=int(input("enter number of legs "))

def solve(numheads, numlegs):
    rab=int((numlegs-2*numheads)/2)
    chic=int((numlegs-4*rab)/2)
    print("you have", rab, "rabbits and", chic, "chickens")

solve(heads, legs)