'''
Name: Edward Drobnis
Date: April 2, 2024
Title: Quadratic Equation
Description: Displays the roots of a quadratic
'''
import math

a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
c = float(input("Enter value for c: "))

discriminant = b ** 2 - 4 * a * c

if discriminant < 0:
    print("There are no real roots")
elif discriminant == 0:
    root = -b / (2 * a)
    print("The root (vertex) is: {:.1f}".format(root))
else:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("The roots are {:.2f} and {:.2f}".format(root1, root2))