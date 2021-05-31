import sys

current_movies = {
    'The Grinch': ['11:00am', "2:00pm", "4:15pm", "7:45pm"],
    'Hardball': ['11:00am', "2:00pm", "6:15pm", "7:45pm"],
    'Sharknado': ['9:00am', "12:00pm", "4:30pm", "7:45pm"],
    'Sharkboy and Lavagirl': ['10:20am', "2:00pm", "4:15pm", "7:45pm"]
}

all_movies = {
    "expiredMovies": [
        {"name": "Jurassic Park", "rating": "pg13"},
        {"name": "Johnny Cash", "rating": "pg"}
    ],
    "currentMovies": [
        {   "name": 'When Harry Met Sally',
            "rating": "pg13",
            "showtimes": ['11:00am', "2:00pm"],
            "freePopcorn": "no"
        },
        {   "name": 'Terminator',
            "rating": "pg13",
            "showtimes": ['11:00am', "2:00pm"],
            "freePopcorn": "yes"
        },
        {
            "name": "The Martian",
            "rating": "pg",
            "showtimes": ['11:00am', "2:00pm"],
            "freePopcorn": "yes"
        },
        {
            "name": "Battlefarce",
            "rating": "R",
            "showtimes": ['11:00am', "2:00pm"],
            "freePopcorn": "no"
        }
    ]
}


print("Please choose an option:")
print("enter [t] to see all movie titles currently playing")
print("enter [a] to view all movie titles and their showtimes")
print("enter [s] to search for a movie title")
print("enter [p] to view free popcorn movie offers")
menuChoice = input().lower()




if menuChoice == "t":
    print("\033c")
    print("Current movies available: ")
    for movie in current_movies:
        print("  ", movie)
    print("------")
    user_movieInput = input("What movie would you like showtimes for? \n")
elif menuChoice == "s":
    user_movieInput = input("What movie would you like showtimes for? \n")
elif menuChoice == "a":
    print("\033c")
    print("Current movie showtimes: ")
    for movie in current_movies:
        print("  ", movie)
        for time in current_movies.get(movie):
            print("   -- ", "playing at: ", time)
        print()
elif menuChoice == "p":
    print("\033c")
    for movie in all_movies["currentMovies"]:
        if (movie["freePopcorn"] == "yes"):
            print(movie["name"])
    input()
else:
    print("invalid entry -- exiting program")
    sys.exit()
    

user_movieInput = user_movieInput.title()
showtime = current_movies.get(user_movieInput)
print()
if user_movieInput in current_movies:
    if showtime == None:
        print(user_movieInput, "is not playing today")
    else:
        print(user_movieInput, "is playing today at:")
        for time in showtime:
            print("   ", time)
else:
    print("movie not found", user_movieInput)