'''
Author: Edward Drobnis
Date: March 19, 2024
Title: Division and Modulus
Description: Calculates the division and modulus of two numbers
'''

num1 = int(input('Enter an integer: '))
num2 = int(input('Enter a second integer: '))

div1 = int(num1 / num2)
div2 = int(num2 / num1)
mod1 = num1 % num2
mod2 = num2 % num1

print("{0} / {1} = {2}".format(num1, num2, div1))
print("{0} % {1} = {2}\n".format(num1, num2, mod1))
print("{0} / {1} = {2}".format(num2, num1, div2))
print("{0} % {1} = {2}".format(num2, num1, mod2))