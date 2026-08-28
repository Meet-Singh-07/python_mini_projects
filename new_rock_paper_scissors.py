import random 

ROCK = "r"
PAPER = "p"
SCISSORS = "s"
emojis ={ROCK:"🪨",
         PAPER:"📃",
         SCISSORS:"✂️"}
choices = (tuple(emojis.keys()))

def get_user_choice():
    while True :
        user_choice = input("Rock, Paper, Scissors ?(r/p/s) : ").lower()
        if user_choice in choices:
            return user_choice
        else: 
            print("Invalid Option! Try again!")

def display_choices(user_choice , computer_choice):
    print(f"You chose {emojis[user_choice]} \nComputer chose {emojis[computer_choice]}")    

def determine_winner(user_choice , computer_choice):
    if user_choice == computer_choice:
        print("It's a Tie!!")
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or 
        (user_choice == PAPER and computer_choice == ROCK) or 
        (user_choice == SCISSORS and computer_choice == PAPER)):
        print("You Win!")
    elif (user_choice == PAPER and computer_choice == SCISSORS) or (user_choice == SCISSORS and computer_choice == ROCK) or (user_choice == ROCK and computer_choice == SCISSORS):
        print("You Lose!")
def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice , computer_choice)

        determine_winner(user_choice , computer_choice)

        should_continue = input("Continue playing ?(y/n)").lower()
        if should_continue == "n":
            break

play_game()