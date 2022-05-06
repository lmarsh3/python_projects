# computer checks and guesses the correct number from 1 to 10

import random # import random function to use random numbers

def computer_guess(x):
    
    low = 1
    high = x
   
    feedback = '' # empty feedback string

    while feedback != 'c': # while feedback loop to check when guess is not correct
        if low != high: # checks to make sure low != high when guessing
            guess = random.randint(low, high)
        else:
            guess = low # could be high as low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)???').lower
        if feedback == 'h':
            high = guess - 1 # if too high, go down -1
        elif feedback == 'l':
            low = guess + 1 # if too low, go up + 1
    print(f'YAY!!! The computer guessed your number {guess} correctly!!!')

computer_guess(10)