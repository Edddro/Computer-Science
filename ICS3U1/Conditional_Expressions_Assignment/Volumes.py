'''
Name: Edward Drobnis
Date: April 2, 2024
Title: Volumes
Description: 
'''
import math

print("Rectangular Prism")
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
height = float(input("Enter the height: "))

volume = length * width * height

print("The volume is: {:.0f}\n".format(volume))
print("Sphere")
radius = float(input("Enter the radius: "))

volume = math.pi * ((2 * radius) ** 3) / 6

print("The volume is: {:.3f}\n".format(volume))
print("Cube")
length = float(input("Enter the length of each side: "))

volume = length ** 3

print("The volume is: {:.0f}".format(volume))