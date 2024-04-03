'''
Name: Edward Drobnis
Date: April 2, 2024
Title: Trigonometry Functions
Description: Converts an angle in degrees into sine, cosine, and tangent
'''
import math

degrees = float(input("Enter an angle in degrees: "))
sine = math.sin(math.radians(degrees))
cosine = math.cos(math.radians(degrees))
tangent = math.tan(math.radians(degrees))

print("Sin({:.0f}) = {:.3f}".format(degrees, sine))
print("Cos({:.0f}) = {:.3f}".format(degrees, cosine))
print("Tan({:.0f}) = {:.3f}".format(degrees, tangent))