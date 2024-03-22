'''
Author: Edward Drobnis
Date: March 8, 2024
Title: Difference
Description: Calculates the difference of two user-inputted numbers
'''

num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

difference = num1 - num2

print("The difference of", num1, "and", num2, "is:", '{:.2f}'.format(difference))