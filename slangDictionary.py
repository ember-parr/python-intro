webSlang = ["LOL", "WYD", "IMHO", "IDK"]

print("Choose an option to get started: ")
print("--- Enter SEARCH to search for a word in the dictionary")
print("--- Enter ADD to add a new word to the dictionary")
print("--- Enter VIEW to view a list of words in the dictionary")
print("--- Enter EXIT to exit the dictionary")
app_start = input().lower()

if app_start == "search":
    user_addition = input("What word would you like to add?\n")
    if user_addition.upper() in webSlang:
        print(user_addition + " is in the dictionary!")
    else:
        print(user_addition.capitalize() + " is not found.")
        user_addition_addNew = input("Would you like to add " + user_addition.capitalize() + " to the dictionary? (y/n) - ")
        if user_addition_addNew == "n":
            print("no problem... bye!")
        else: 
            webSlang.append(user_addition.upper())
            print("You added a word to the dictonary!")
            print()
            print("updated webSlang list:")
            print(webSlang)
            print()
elif app_start == "add":
    print("not yet an option... ")
    print()
elif app_start == "view":
    for acronym in webSlang:
        print(acronym)
    print()
else:
    input("press any key to exit")