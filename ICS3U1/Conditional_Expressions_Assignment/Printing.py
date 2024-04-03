'''
Name: Edward Drobnis
Date: March 27, 2024
Title: Printing
Description: Outputs the cost of printing
'''

copies = int(input("Enter the number of copies to be printed: "))

if copies <= 99:
    cost = 0.3
elif copies <= 499:
    cost = 0.28
elif copies <= 749:
    cost = 0.27
elif copies <= 1000:
    cost = 0.26
else:
    cost = 0.25

totalCost = cost * copies

print("Price per copy is: ${:.2f}".format(cost))
print("Total cost is: ${:.2f}".format(totalCost))