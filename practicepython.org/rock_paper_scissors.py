import random
import json

choices = ["rock", "paper", "scissors"]
score_file_name = "rps_score.txt"

try:
    with open(score_file_name, "r") as score_file:
        score_dic = json.loads(score_file.read())
        print(score_dic)
except(FileNotFoundError, ValueError):
    print("To je vasa prva igra.")
    score_dic = {"You": 0, "Computer": 0}


def score_up(contender, file_name, score):
    if contender == "Computer":
        score[contender] += 1
    elif contender == "You":
        score[contender] += 1
    else:
        print("Something went wrong!")
    with open(file_name, "w") as score_file2:
        score_file2.write(json.dumps(score))


while True:
    computer_choice = random.choice(choices)
    user_choice = input("Rock, paper or scissors? ").lower()
    print(f"Computer: {computer_choice}")
    if user_choice == "rock" and computer_choice == "paper":
        print("Computer won!")
        score_up("Computer", score_file_name, score_dic)
        break
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You won!")
        score_up("You", score_file_name, score_dic)
        break
    elif user_choice == "paper" and computer_choice == "scissors":
        print("Computer won!")
        score_up("Computer", score_file_name, score_dic)
        break
    elif user_choice == "paper" and computer_choice == "rock":
        print("You won!")
        score_up("You", score_file_name, score_dic)
        break
    elif user_choice == "scissors" and computer_choice == "rock":
        print("Computer won!")
        score_up("Computer", score_file_name, score_dic)
        break
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You won!")
        break
    elif user_choice not in choices:
        print("Wrong choice, try again!")
    else:
        print("It's a tie, try again!")
