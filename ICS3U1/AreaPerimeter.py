'''
Author: Edward Drobnis
Date: March 7, 2024
Title: AreaPerimeter
Description: Calculates the area and perimeter of a rectangle
'''

length = float(input("Length: "))
width = float(input("Width: "))

area = "{:.2f}".format(length * width)
perimeter = "{:.2f}".format(2 * (length + width))

print(f"Area: {area}\nPerimeter: {perimeter}")