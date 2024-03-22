'''
Author: Edward Drobnis
Date: March 19, 2024
Title: Energy
Description: Calculates the energy and number of powered light bulbs
'''

mass = float(input("Enter the mass in kilograms: "))

SPEED = 3.0 * 10 ** 8
energy = mass * SPEED ** 2
bulbs = energy / 360000

print("The energy produced in Joules is = ", '{:.1e}'.format(energy))
print("The number of 100-watt light bulbs powered = ", '{:.1e}'.format(bulbs))