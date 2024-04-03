'''
Name: Edward Drobnis
Date: April 2, 2024
Title: Car Payment
Description: Calculates the monthly car payment
'''

principal = float(input("Principal: "))
interest = float(input("Interest Rate: "))
months = float(input("Number of monthly payments: "))

payment = (principal * (interest / 12)) / (1 - (1 + interest / 12) ** -months)

print("The monthly payment is: ${:.2f}".format(payment))