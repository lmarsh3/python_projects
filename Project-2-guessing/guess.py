# python program that prompts user to enter number between 1 to 10
# keeps user guessing until they get it right

import random # import random function to use random numbers

def guess(x):
    random_number = random.randint(1, x) # set variable to choose random number between 1 and x
    # create while loop to keep guessing until the right number is guessed
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Guess again!!! Too low.")
        elif guess > random_number:
            print("Guess again!!! Too high.")
    print(f"Yay!!! You guessed the right number. {random_number} is the correct number.")

guess(10)

