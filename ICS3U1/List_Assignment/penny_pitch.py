'''
Name: Edward Drobnis
Date: May 22, 2024
Title: Penny Pitch
Description: Creates a board that consists of 5 x 5 squares, with 15 containing prizes
'''
# Imports the random library
import random
def select_prizes(prizes, squares):
    '''
    Returns a list of all prizes in random squares
    :param prizes:
    :param squares:
    :return:
    '''
    # Loops through each prize in the prizes list until the count of the prize is 0
    for prize, count in prizes:
        while count > 0:
            # Randomly generates a row and column
            row = random.randint(0, 4)
            col = random.randint(0, 4)
            # If the square is blank, change the square to the prize's name and reduce the count of the prize by 1
            if squares[row][col] == "":
                squares[row][col] = prize
                count -= 1

def draw_squares(squares):
    '''
    Displays a board
    :param squares:
    :return:
    '''
    print()
    # Loops through each row in the squares list and prints horizontal lines
    for row in squares:
        print("-" * 86)
        # Loops through each tile in the row and prints the prize's name (or an empty square)
        for i in range(5):
            print("|{:^16}".format(row[i]), end="")
        print("|")
    print("-" * 86)
    print()

def penny_pitch(prizes, squares):
    '''
    Randomly selected a tile to drop a penny
    :param prizes:
    :param squares:
    :return:
    '''
    # Selects a random row and column
    row = random.randint(0, 4)
    col = random.randint(0, 4)

    # Checks if the selected row and column contains a prize
    for i in range(len(prizes)):
        if prizes[i][0] == squares[row][col]:
            # If so, reduce the count of that prize by 1
            prizes[i][1] -= 1

    # Add an asterisk to the tile (indicating that it is hit)
    squares[row][col] += "*"

def display_prizes_won(prizes):
    '''
    Displays all the prizes won
    :param prizes:
    :return:
    '''
    # Creates an empty list that will contain all the prizes won
    prizes_won = []
    # Loops through all the prizes and checks if the count is 0
    for prize, count in prizes:
        if count == 0:
            # If so, add the prize's name to prizes_won
            prizes_won.append(prize)

    # If no prizes have a final count of 0, print "No prizes won!"
    if not prizes_won:
        print("No prizes won!")

    # Otherwise, loop through the list of prizes won and print each value, separated by commas
    else:
        print(f"Item(s) won:", end = " ")
        for i in range(len(prizes_won)):
            print(prizes_won[i], end = "")
            if i != len(prizes_won) - 1:
                print(",", end = " ")

def main():
    '''
    Main function that initializes the prizes and calls the necessary functions
    :return:
    '''
    # Creates a 2D list containing the prize name and count
    prizes = [["Puzzle", 3], ["Game", 3], ["Ball", 3], ["Poster", 3], ["Doll", 3]]
    # Creates a 2D list containing 5x5 empty squares (5 elements per list and a total of 5 lists in the list)
    squares = [[""] * 5 for _ in range(5)]
    print("New Board")
    select_prizes(prizes, squares)
    draw_squares(squares)

    a = input("Enter any key and enter to continue: ")

    # Calls the penny_pitch function 10 times
    for _ in range(10):
        penny_pitch(prizes, squares)

    print("\nNew Board With Pennies Tossed")
    draw_squares(squares)

    display_prizes_won(prizes)

while True:
    try:
        main()
        if input("Press 0 to stop or any other key to continue: ") == "0":
            break
    except ValueError:
        print("Press 0 to stop or any other key to continue: ")

'''
Pseudo Code:

Functions:
select_prizes(prizes, squares)
draw_squares(squares)
penny_pitch(prizes, squares)
display_prizes_won(prizes)
main()

import random
function select_prizes(prizes, squares):
    for prize, count in prizes:
        while count > 0:
            row = random.randint(0, 4)
            col = random.randint(0, 4)
            if squares[row][col] == "":
                squares[row][col] = prize
                count -= 1
end select_prizes

function draw_squares(squares):
    print()
    for row in squares:
        print("-" * 86)
        for i in range(5):
            print("|{:^16}".format(row[i]), end="")
        print("|")
    print("-" * 86)
    print()
end draw_squares

function penny_pitch(prizes, squares):
    row = random.randint(0, 4)
    col = random.randint(0, 4)

    while squares[row][col] == "x":
        row = random.randint(0, 4)
        col = random.randint(0, 4)

    for i in range(len(prizes)):
        if prizes[i][0] == squares[row][col]:
            prizes[i][1] -= 1

    squares[row][col] += "*"
end penny_pitch

function display_prizes_won(prizes):
    prizes_won = []
    for prize, count in prizes:
        if count == 0:
            prizes_won.append(prize)

    if not prizes_won:
        print("No prizes won!")

    else:
        print(f"Item(s) won:", end = " ")
        for i in range(len(prizes_won)):
            print(prizes_won[i], end = "")
            if i != len(prizes_won) - 1:
                print(",", end = " ")
end display_prizes_won

function main():
    prizes = [["Puzzle", 3], ["Game", 3], ["Ball", 3], ["Poster", 3], ["Doll", 3]]
    squares = [[""] * 5 for _ in range(5)]
    print("New Board")
    select_prizes(prizes, squares)
    draw_squares(squares)

    a = input("Enter any key and enter to continue: ")

    for _ in range(10):
        penny_pitch(prizes, squares)

    print("\nNew Board With Pennies Tossed")
    draw_squares(squares)

    display_prizes_won(prizes)
end main

Main Program:
    try:
        main()
        if input("Press 0 to stop or any other key to continue: ") == "0":
            break
    except ValueError:
        print("Press 0 to stop or any other key to continue: ")
'''