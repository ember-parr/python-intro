import random

gameChoices = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(gameChoices)
user_choice = input("enter one --> Rock, Paper or Scissors\n").capitalize()


if computer_choice == user_choice:
    print("TIE GAME!")
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("Rock smashes scissors... you WIN!")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("Scissors cut paper... you WIN!")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("Paper covers rock... you WIN!")
else:
    print("Computer chose " + computer_choice + " you LOST!")