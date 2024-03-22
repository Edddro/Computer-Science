'''
Author: Edward Drobnis
Date: March 21, 2024
Title: Spending
Description: Calculates the percentages of items based on the total items purchased
'''

print("Enter the amount spent last month on the following items:")
food = float(input("Food: $"))
clothing = float(input("Clothing: $"))
entertainment = float(input("Entertainment: $"))
rent = float(input("Rent: $"))

cost = (food + clothing + entertainment + rent) / 100
food /= cost
clothing /= cost
entertainment /= cost
rent /= cost

print("\n{:<15}{:>11}".format("Category", "Budget"))
print("{:<20}{:.2f} %".format("Food", food))
print("{:<20}{:.2f} %".format("Clothing", clothing))
print("{:<20}{:.2f} %".format("Entertainment", entertainment))
print("{:<20}{:.2f} %".format("Rent", rent))