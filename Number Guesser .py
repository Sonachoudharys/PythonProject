'''
Task: Number Guesser
Create a number guessing game where the
program generates a random number
between a specified range, and the user tries
to guess it. Provide feedback to the user if
their guess is too high or too low.
'''

import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Ask user to guess
guess = int(input("Guess the number between 1 and 100: "))

# Loop until correct guess
while guess != number:
    if guess < number:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Guess again: "))

# Correct guess
print("You guessed it right!")


'''
Output:

Guess the number between 1 and 100: 65
Too low
Guess again: 70
Too low
Guess again: 80
Too low
Guess again: 90
Too high
Guess again: 85
Too high
Guess again: 83
Too low
Guess again: 84
You guessed it right!
'''