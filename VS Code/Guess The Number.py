import random

play = True

while play:
    correct_num = False
    rand_num = random.randrange(1, 100)
    valid = False
    guess = ''
    while not valid or not correct_num:
        guess = input("Guess a Number Between 1 and 100 or type \"0\" to give up: ")
        if guess == 0:
            break
        if guess.isdigit() and 1 <= int(guess) <= 100:
            valid = True
            if int(guess) == rand_num:
                correct_num = True
                print("Correct, The Number Was", rand_num)
            elif int(guess) > rand_num:
                print("The Number is Lower")
            elif int(guess) < rand_num:
                print("The Number is Higher")
        else:
            print('Not a Valid Input')
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