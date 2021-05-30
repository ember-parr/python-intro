# importing python mondule 'random'
import random


userGuess = 0
computerDiceRoll = random.randint(1,6)
score = 0

startGame = input("Would you like to play? (y/n)")

if startGame == "y":
    print("may the odds be ever in your favor")
    print("......")
    print("Use your psychic ability to foresee the computer's dice roll....")
    userGuess = int(input("Guess a number 1-6: "))
    print()
elif startGame == "n":
    print("alrighty... maybe next time :( ")
else:
    print("invalid option... exiting program")


if userGuess == computerDiceRoll and userGuess != 0:
    print("Holy Moly... You got it!")
    input()
elif userGuess != 0 and userGuess != computerDiceRoll:
    print("nope, better luck next time... ")
else:
    input()