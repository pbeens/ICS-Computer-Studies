from random import *

# generate a random number between 1 and 100 (inclusive)
num = randint(1,100)

# loop until the random number is guessed
while True:
    guess = int(input('Enter your guess: '))
    # guess is too high
    if guess > num:
        print("Lower!")
    # guess is too low
    elif guess < num:
        print("Higher!")
    # guess is correct!
    else:
        print("Good guess!")
        break


