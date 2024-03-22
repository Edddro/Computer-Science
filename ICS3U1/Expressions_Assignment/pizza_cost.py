'''
Author: Edward Drobnis
Date: March 19, 2024
Title: Pizza Cost
Description: Calculates the cost of making a pizza
'''

diameter = float(input('Enter the diameter of the pizza in inches: '))

materials = 0.05 * diameter ** 2

cost = materials + 1 + 0.75

print("The cost of making the pizza is: $" + '{:.2f}'.format(cost))