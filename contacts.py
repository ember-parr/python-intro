contacts = {
    "number": 4,
    "students": [
        {"name": "Ember Parr", "email": "ember@home.com", "grade": "4"},
        {"name": "Aiden Parr", "email": "aiden@gmail.com", "grade": "4"},
        {"name": "Justin Adams", "email": "justin@adams.com", "grade": "5"},
        {"name": "Alexus Adams", "email": "lexi@me.com", "grade": "6"}
    ]
}



for student in contacts["students"]:
    print(student["name"])
    if (student["grade"] == "4"):
        print("yep")

