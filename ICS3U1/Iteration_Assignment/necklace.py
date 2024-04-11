'''
Name: Edward Drobnis
Date: April 10, 2024
Title: Necklace
Description: Calculates the sum of the two previous numbers and displays the ones digit until it matches the starting values
'''

starting = int(input("Enter the first starting number: "))
ending = int(input("Enter the second starting number: "))

previousSum = starting
sum = ending
nextSum = (starting + ending) % 10
print(previousSum, sum, nextSum, end = " ")

while sum != starting or nextSum != ending:
    previousSum = sum
    sum = nextSum
    nextSum = (previousSum + sum) % 10
    print(nextSum, end = " ")