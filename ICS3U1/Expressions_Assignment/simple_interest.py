'''
Author: Edward Drobnis
Date: March 22, 2024
Title: Simple Interest
Description: Calculates the simple interest given the principal amount, interest rate, and number of years
'''

principal = float(input("Enter the principal: "))
years = float(input("Enter the number of years: "))
interest = float(input("Enter the interest rate: "))

amount = principal * (1 + years * interest)

print("The value after the term is: ${:.2f}".format(amount))