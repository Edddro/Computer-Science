'''
Name: Edward Drobnis
Date: April 2, 2024
Title: Bacteria Growth
Description: Calculates the number of bacteria present at a given time
'''
import math

n = int(input("Enter initial bacteria amount: "))
k = float(input("Enter a constant value for k: "))
t = float(input("Enter the growth time period in hours: "))

y = n * math.e ** (k * t)

print("{:.0f} bacteria will be present after {:.1f} hours".format(y, t))