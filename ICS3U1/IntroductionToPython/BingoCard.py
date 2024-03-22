'''
Author: Edward Drobnis
Date: March 4, 2024
Title: BingoCard
Description: Displays a Bingo Card
'''

import random

bingo = "BINGO"
print("-" * 46)

for i in range(6):
    for j in range(5):
        if i == 0:
            print("| {:^6s}".format(bingo[j]), end=" ")
        elif i == 3 and j == 2:
            print("| {:^6s}".format("BINGO"), end=" ")
        else:
            num = str(random.randint(0, 99))
            print("| {:^6s}".format(num), end=" ")
    print("|")
    print("-" * 46)