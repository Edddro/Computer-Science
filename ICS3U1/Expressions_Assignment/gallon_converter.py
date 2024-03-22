'''
Author: Edward Drobnis
Date: March 22, 2024
Title: Gallon Converter
Description: Converts gallons to quarts, pints, cups, and tablespoons
'''

gallons = float(input("Enter the number of gallons: "))

quarts = gallons * 4
pints = quarts * 2
cups = pints * 2
tablespoons = cups * 16

print("In {:.1f} gallons there are:".format(gallons))
print("{:.1f} quarts".format(quarts))
print("{:.1f} pints".format(pints))
print("{:.1f} cups".format(cups))
print("{:.1f} tablespoons".format(tablespoons))