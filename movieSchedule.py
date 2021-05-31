import sys

current_movies = {
    'The Grinch': '11:00am',
    'Hardball': '1:00pm'
}



menuChoice = input("Would you like to see a list of current movies? (y/n) \n").lower()
if menuChoice == "y":
    print("\033c")
    print("Current movies available: ")
    for movie in current_movies:
        print("  ", movie)
    print("------")
    user_movieChoice = input("What movie would you like showtimes for? \n")
elif menuChoice == "n":
    user_movieChoice = input("What movie would you like showtimes for? \n")
else:
    print("invalid entry -- exiting program")
    sys.exit()

print("still goin... ")