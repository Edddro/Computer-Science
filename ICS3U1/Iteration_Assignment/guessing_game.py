'''
Name: Edward Drobnis
Date: April 10, 2024
Title: Guessing Game
Description: Generates a random number between 1 and 50 that the user tries to guess
'''
import random

number = random.randint(1, 50)
low = 1
high = 50
guess = "None"
message = ""

print("{:<15}{:<15}{:<15}{:}".format("Current Low", "Current High", "Player Types", "Message Displayed"))
print("{:^14}{:^14}{:^14}{:^20}".format(low, high, guess, message))

while guess != number:
    guess = int(input(""))

    if guess < low or high < guess:
        message = "Not within the range."

    elif guess < number:
        message = "Too low."
        low = guess + 1

    elif guess > number:
        message = "Too high."
        high = guess - 1

    elif guess == number:
        message = "You guessed it!"

    print("{:^14}{:^14}{:^14}{:^20}".format(low, high, guess, message))