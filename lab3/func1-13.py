import random


userName=input("Hello! What is your name? \n")

guessNumber = random.randint(1, 20)

print("Well,", userName, ", I am thinking of a number between 1 and 20. \nTake a guess.")

userInput=int(input())


def game(num, numOfg):

    numOfg+=1

    if num>guessNumber:
        print("Your guess is too great \nTake a guess")
        inp=int(input())
        game(inp, numOfg)

    elif num<guessNumber:
        print("Your guess is too low \nTake a guess")
        inp=int(input())
        game(inp, numOfg)

    else:
        print("Good job,", userName+"!", "You guessed my number in", numOfg, "guesses!")

game(userInput, 0)