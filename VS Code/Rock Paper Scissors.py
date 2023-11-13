import random

valid_inputs = ["rock", "paper", "scissors"]
play = True
valid = False

while play == True:
    user_score = 0
    computer_score = 0

    while user_score < 2 and computer_score < 2:
        computer = random.choice(valid_inputs)
        user = input("Enter Rock, Paper, or Scissors. ").lower()
        if user == "rock":
            if computer == "rock":
                print("It's a Tie, You Both Picked Rock.")
            elif computer == "scissors":
                print("You Won, Rock Beats Scissors.")
                user_score += 1
            elif computer == "paper":
                print("You Lost, Paper Beats Rock.")
                computer_score += 1

        elif user == "paper":
            if computer == "rock":
                print("You Won, Paper Beats Rock.")
                computer_score += 1
            elif computer == "scissors":
                print("You Lost, Scissors Beats Paper.")
                computer_score += 1
            elif computer == "paper":
                print("It's a Tie, You Both Picked Paper.")

        elif user == "scissors":
            if computer == "rock":
                print("You Lost, Rock Beats Scissors.")
                computer_score += 1
            elif computer == "scissors":
                print("It's a Tie, You Both Picked Paper.")
            elif computer == "paper":
                print("You Won, Scissors Beats Paper.")
                user_score += 1

        else:
             print("Not a Valid Input.")
    if computer_score > user_score:
        print("You Lose, You Only Won", user_score,
              "Times, But the Computer Won", computer_score, "Times")
    else:
        print("You Won! You Won", user_score,
              "Times, But the Computer Won", computer_score, "Times")
    
    
    while not valid:
        again = input("Do you want to play again? y/n ").lower()
        if again == "y" or again == "yes":  
            print("Ok")
            valid = True
        elif again == "n" or again == "no":  
            play = False
            valid = True
            print(":(")
        else:
            print("Not a Valid Input.")
            
    
        


    
