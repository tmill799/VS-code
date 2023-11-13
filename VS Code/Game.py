import random

def hangman():
    words = (
        "Banana", "Elephant", "Computer", "Guitar", "Mountain",
        "Sunshine", "Chocolate", "Pizza", "Butterfly", "Library",
        "Diamond", "Fireworks", "Dragon", "Rainbow", "Strawberry",
        "Elephant", "Telephone", "Watermelon", "Football", "Universe",
        "Jellyfish", "Adventure", "Snowflake", "Parrot", "Pancake",
        "Lighthouse", "Cactus", "Bicycle", "Moonlight", "Starfish",
        "Candle", "Octopus", "Raincoat", "Tiger", "Umbrella",
        "Zebra", "Penguin", "Rocket", "Volcano", "Sunflower",
        "Helicopter", "Dolphin", "Eagle", "Kangaroo", "Lion"
    )
    play = True

    while play:
        attempts = 7
        selected_word = random.choice(words).lower()
        word_test = set(selected_word)
        correct_letters = []
        guessed_letters = []
        guess = ''

        print(f"\nThere are {len(selected_word)} letters.\n")

        while len(word_test) != len(correct_letters) and guess != "end" and attempts > 0:
            valid = False
            guess = input("Guess a letter or type \"end\" to give up: ").lower()

            while not valid and guess != "end":
                if guess in guessed_letters:
                    print("\nYou already guessed this letter.")
                    guess = input("\nGuess a letter or type \"end\" to give up: ").lower()
                elif len(guess) == 1 and guess.isalpha() and guess in selected_word:
                    valid = True
                    correct_letters.append(guess)
                    guessed_letters.append(guess)
                elif len(guess) == 1 and guess.isalpha() and guess not in selected_word:
                    valid = True
                    attempts -= 1
                    guessed_letters.append(guess)
                    print(f"\nThere are no '{guess}'s in the word.")
                    print(f"You have {attempts} guesses left.")
                else:
                    print("\nNot a valid character.")
                    guess = input("\nGuess a letter or type \"end\" to give up: ").lower()

            print("\nWord: ", end="")
            for x in selected_word:
                if x in correct_letters:
                    print(x, end=" ")
                else:
                    print("_", end=" ")
            
            print("\n")
        if len(word_test) == len(correct_letters):
            print("Yay, You Won!\n")
        elif guess == "end":
            print("I Can't Belive You Rage Quit.  :(\n")
        elif attempts <= 0:
            print(f"Aw Man, You Lost.  :(\n{selected_word}\n")

        
        valid = False
        while not valid:
            again = input("Would You Like to Play Again? Y/N").lower()
            if again == "y" or again == "yes":
                valid = True
            elif again == "n" or again == "no":
                play = False
                valid = True
            else:
                print("Not a Valid Input")

def RPS():
    valid_inputs = ["rock", "paper", "scissors"]
    play = True

    while play == True:
        user_score = 0
        computer_score = 0

        while user_score < 2 and computer_score < 2:
            computer = random.choice(valid_inputs)
            user = input("\nEnter Rock, Paper, or Scissors. ").lower()
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
        
        valid = False
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

def Guess_The_Number():
    play = True

    while play:
        correct_num = False
        rand_num = random.randrange(1, 100)
        valid = False
        guess = ''
        while not valid or not correct_num:
            guess = input("\nGuess a Number Between 1 and 100 or type \"end\" to give up: ")
            if guess == 'end':
                break
            if guess.isdigit() and 1 <= int(guess) <= 100:
                valid = True
                if int(guess) == rand_num:
                    correct_num = True
                    print("\nCorrect, The Number Was", rand_num)
                elif int(guess) > rand_num:
                    print("\nThe Number is Lower")
                elif int(guess) < rand_num:
                    print("\nThe Number is Higher")
            else:
                print('\nNot a Valid Input')
        valid = False

        while not valid:
            again = input("\nDo you want to play again? y/n ").lower()
            if again == "y" or again == "yes":
                valid = True
            elif again == "n" or again == "no":
                play = False
                valid = True
            else:
                print("\nNot a Valid Input.")



valid = False
play = True
while play:
    while not valid:
        game = input("What Game Do You Want To Play?\n\n-RPS\n\n-HangMan\n\n-Guess The Number\n\n").lower()
        if game == "rps" or game == "rock paper scissors" or game == "r.p.s":
            valid = True
            RPS()
        elif game == "hangman" or game == "hang man":
            valid = True
            hangman()
        elif game == "guess the number" or game == "gtn" or game == "g.t.n":
            valid = True
            Guess_The_Number()
        else:
            print("Not a Valid Game")
    again = input("\nDo you want to play a different game? y/n ").lower()
    if again == "y" or again == "yes":  
        valid = False
    elif again == "n" or again == "no":  
        play = False
        valid = True
        print(":(")
    else:
        print("Not a Valid Input.")