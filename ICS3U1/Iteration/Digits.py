'''
Name: Edward Drobnis
Date: April 9, 2024
Title: Digits
Description: Counts the number of digits in a number
'''

number = abs(float(input("Number: ")))
digits = 1

while number // 10 > 0:
    number = number // 10
    digits += 1

print(f"Number of digits: {digits}")