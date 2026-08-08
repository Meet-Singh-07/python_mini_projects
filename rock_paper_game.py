import random

def get_choices():
    player_choice = input("Enter a choice (Rock , Paper, Scissors) :")
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    choices = { "Player" : player_choice, 
               "Computer" : computer_choice}
    return choices

def check_win(player,computer):
    print("You chose :", player , ", Computer chose :", computer )
    #print("You chose :" + player + "Computer chose :" + computer )
    #print(f"You chose : {player} , Computer chose : {computer}")
    if player == computer:
        return "It's a tie!" 
    elif player == "Rock":
        if computer == "Scissors":
            return "Rock smashes Scissors! You win."
        else:
            return "Paper covers the Rock! You lose."
    elif player == "Paper":
            if computer == "Scissors":
                return "Scissors cuts Paper! You loss."
            else:
                return "Paper covers the Rock! You win." 
    elif player == "Scissors":
            if computer == "Paper":
                return "Scissors cuts Paper! You win."
            else:
                return "Rock smashes Scissors! You lose!"

choices = get_choices()
result = check_win(choices["Player"], choices["Computer"])
print(result)




