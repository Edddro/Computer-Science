'''
Name: Edward Drobnis
Date: April 10, 2024
Title: Cubes Sum
Description: Calculates the sum of all the digits cubed
'''

number = int(input('Enter a positive integer: '))
sum = 0

while number > 0:
    sum += (number % 10) ** 3
    number //= 10

print("The sum of the cubes of the digits is: {}".format(sum))