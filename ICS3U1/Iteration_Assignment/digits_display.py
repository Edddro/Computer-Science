'''
Name: Edward Drobnis
Date: April 10, 2024
Title: Digits Display
Description: Displays the digits of a number on a new line
'''

number = int(input('Enter a positive integer: '))
number2 = number
digits = 0

while (number2 // 10) > 0:
    number2 //= 10
    digits += 1

for i in range(digits, -1, -1):
    number2 = number // (10 ** i) % 10
    print(number2)