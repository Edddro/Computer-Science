'''
Author: Edward Drobnis
Date: March 19, 2024
Title: Three Digits
Description: Splits a three-digit number into a hundreds-place, tens-place, and ones-place
'''

number = int(input('Enter a three-digit number: '))

hundreds = number // 100
tens = number // 10 % 10
ones = number % 10

print("\nThe hundreds-place digit is: {}".format(hundreds))
print("The tens-place digit is: {}".format(tens))
print("The ones-place digit is: {}".format(ones))