'''
Author: Edward Drobnis
Date: March 20, 2024
Title: Project
Description: Calculates the percentages of time taken for different tasks
'''

print("Enter the number of minutes spent on each of the following project tasks:\n")
design = float(input("Designing: "))
code = float(input("Coding: "))
debug = float(input("Debugging: "))
test = float(input("Testing: "))

time = (design + code + debug + test) / 100
design /= time
code /= time
debug /= time
test /= time

print("\n{:<15}{:>11}".format("Task", "% Time"))
print("{:<20}{:.2f} %".format("Designing", design))
print("{:<20}{:.2f} %".format("Coding", code))
print("{:<20}{:.2f} %".format("Debugging", debug))
print("{:<20}{:.2f} %".format("Testing:", test))