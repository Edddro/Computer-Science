'''
Name: Edward Drobnis
Date: April 2, 2024
Title: Eggs
Description: Calculates the cost of eggs
'''

eggs = int(input("Enter the number of eggs purchased: "))
dozen = eggs // 12
eggs %= 12

if dozen <= 3:
    cost = 0.5
elif dozen <= 5:
    cost = 0.45
elif dozen <= 10:
    cost = 0.4
else:
    cost = 0.35

totalCost = (dozen * cost) + (eggs * cost / 12)

print("The bill is equal to: ${:.2f}".format(totalCost))