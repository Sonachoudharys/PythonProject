'''
Task: Guessing Game
Write a Python program that generates a
random number between 1 and 100. The
user should then try to guess the number.
The program should provide hints such as
"too high" or "too low" until the correct
number is guessed.
'''

import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Keep asking until the user guesses correctly
while True:
    guess = int(input("Enter your guess (1-100): "))
    
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("Correct! You guessed the number.")
        break

'''
Output:

Enter your guess (1-100): 65
Too low
Enter your guess (1-100): 70
Too low
Enter your guess (1-100): 80
Too low
Enter your guess (1-100): 90
Too high
Enter your guess (1-100): 85
Too low
Enter your guess (1-100): 87
Too low
Enter your guess (1-100): 89
Correct! You guessed the number.

'''