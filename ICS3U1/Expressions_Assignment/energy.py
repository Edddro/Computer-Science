'''
Author: Edward Drobnis
Date: March 19, 2024
Title: Energy
Description: Calculates the amount of energy and number of light bulbs that can be powered
'''

mass = float(input("Enter the mass in kilograms: "))

speed = 3 * 10 ** 8
energy = mass * speed ** 2
bulbs = energy / 360000

print("The energy produced in Joules is =", '{:.1e}'.format(energy))
print("The number of 100-watt light bulbs powered =", '{:.1e}'.format(bulbs))