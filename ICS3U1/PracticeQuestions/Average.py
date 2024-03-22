'''
Author: Edward Drobnis
Date: March 8, 2024
Title: Average
Description: Calculates the average of three user-inputted numbers
'''

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average: ", '{:.2f}'.format(average))