'''
Name: Edward Drobnis
Date: April 2, 2024
Title: MyPow
Description: Calculates the power of two numbers
'''
import math

x = float(input("Enter a value for X: "))
y = float(input("Enter a value for Y: "))

formula = math.e ** (y * math.log(x, math.e))
power = math.pow(x, y)

print("The result from using the formula is:", formula)
print("\nThe result from using the Math pow<> method is:", power)