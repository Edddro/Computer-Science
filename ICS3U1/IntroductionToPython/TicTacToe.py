'''
Author: Edward Drobnis
Date: March 4, 2024
Title: TicTacToe
Description: Displays a TicTacToe grid
'''

print(" ___ ___ ___")
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            print("| x ", end="")
            continue
        print("|", end = "")
        print("___", end = "")
    print("|")