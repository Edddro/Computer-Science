'''
Name: Edward Drobnis
Date: April 11, 2024
Title: Math Computations
Description: Calculates the sum, average, maximum, and minimum of the values entered
'''

sum = 0
counter = 0
max = float("-inf")
min = float("inf")

while True:
    number = float(input("Enter a non-negative floating-point value: "))

    if number < 0:
        break

    else:
        sum += number
        counter += 1

        if max < number:
            max = number

        if min > number:
            min = number

if counter == 0:
    counter = 1

print("{:<15}{:<15}{:<15}{}".format("Sum", "Average", "Maximum", "Minimum"))
print("{:<15.2f}{:<15.2f}{:<15.2f}{:.2f}".format(sum, sum / counter, max, min))