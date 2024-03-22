'''
Author: Edward Drobnis
Date: March 19, 2024
Title: Coin Change
Description: Calculates the minimum number of coins necessary to make a change.
'''

change = int(input("Enter the change in cents: "))

quarters = change // 25
change -= quarters * 25
dimes = change // 10
change -= dimes * 10
nickels = change // 5
change -= nickels * 5
pennies = change // 1

print("\nThe minimum number of coins is:")
print("{:>14} {}".format("Quarters:", quarters))
print("{:>11} {}".format("Dimes:", dimes))
print("{:>13} {}".format("Nickels:", nickels))
print("{:>13} {}".format("Pennies:", pennies))