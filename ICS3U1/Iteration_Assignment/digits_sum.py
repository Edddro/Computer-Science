'''
Name: Edward Drobnis
Date: April 10, 2024
Title: Digits Sum
Description: Calculates the sum of all the digits
'''

number = int(input('Enter a positive integer: '))
sum = 0

while number > 0:
    sum += number % 10
    number //= 10

print("The sum of the digits is: {}".format(sum))