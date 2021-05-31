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
    user_movieInput = input("What movie would you like showtimes for? \n")
elif menuChoice == "n":
    user_movieInput = input("What movie would you like showtimes for? \n")
else:
    print("invalid entry -- exiting program")
    sys.exit()
    

user_movieInput = user_movieInput.title()
showtime = current_movies.get(user_movieInput)
print()
if user_movieInput in current_movies:
    if showtime == None:
        print(user_movieInput, "is not playing today", showtime)
    else:
        print(user_movieInput, "is playing today at", showtime)
else:
    print("movie not found", user_movieInput)