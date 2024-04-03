'''
Name: Edward Drobnis
Date: March 27, 2024
Title: Package Check
Description: Checks if a package fits the weight and package size requirements
'''

weight = float(input("Enter the package weight in kilograms: "))
length = float(input("Enter the package length in centimetres: "))
width = float(input("Enter the package width in centimetres: "))
height = float(input("Enter the package height in centimetres: "))

volume = length * width * height

if 100000 < volume and 27 < weight:
    print("Too heavy and too large.")
elif 100000 < volume:
    print("Too large.")
elif 27 < weight:
    print("Too heavy.")