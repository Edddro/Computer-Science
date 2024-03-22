'''
Author: Edward Drobnis
Date: March 19, 2024
Title: Order
Description: Calculates the price, tax, and total price for the given order
'''

burgers = int(input("Enter the number of burgers: "))
fries = int(input("Enter the number of fries: "))
sodas = int(input("Enter the number of sodas: "))

price = (burgers * 1.69) + (fries * 1.09) + (sodas * 0.99)
tax = price * 0.065
total = price + tax

print("Total before tax: ${:.2f}\nTax: ${:.2f}\nFinal total: ${:.2f}\n".format(price, tax, total))

tender = float(input("Enter amount tendered: $"))
change = tender - total
print("Change: ${0:.2f}".format(change))