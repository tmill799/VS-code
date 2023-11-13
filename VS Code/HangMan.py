import random

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