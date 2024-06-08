'''
Name: Edward Drobnis
Date: May 21, 2024
Title: Sorted Grades
Description: Prompts users to enter grades, delete grades, see all grades, and see the lowest and highest grades
'''

# Creates a list containing 10 zeros
grades = list(0 for i in range(10))

def sort_grades():
    '''
    Function to sort graded in descending order
    :return:
    '''
    # Loops through each grade in grades (except for the last one)
    for i in range(len(grades) - 1):
        # Loops through each grade in grades (starts at i + 1, where i is the outer loop iteration)
        for j in range(i + 1, len(grades)):
            # Compares two grades and checks if the one on the left is smaller than the one on the right
            if grades[i] < grades[j]:
                # If so, swap the values of those two grades
                grades[i], grades[j] = grades[j], grades[i]
def add_grade(grade):
    '''
    Function to add grade to the grades list and sort it in descending order
    :param grade:
    :return: "Successfully added {grade}% to the list" or "List is full. Please remove a grade and try again."
    '''
    # Loops through each element in grades
    for i in range(len(grades)):
        # If the current grade is 0, it gets deleted, the user-inputted grade is added, and the grades are sorted
        if grades[i] == 0:
            del grades[i]
            grades.append(grade)
            sort_grades()
            return print("Successfully added {}% to the list\n".format(grade))
    # If no zeros are found in the grades list, it states to remove a grade first
    return print("List is full. Please remove a grade and try again.\n")

def delete_grade(grade):
    '''
    Function to remove a grade from grades
    :param grade:
    :return:
    '''
    # Checks if the highest number in grades is 0,
    # If true, it will return "No grades were entered"
    if grades[0] == 0:
        return print("No grades were entered. Please enter a grade and try again.\n")

    # Otherwise, it will loop through each grade until it finds the user-inputted grade
    for i in range(len(grades)):
        # If it finds the user-inputted grade, it removes it from the list and adds a 0 to the end of the list
        if grade == grades[i]:
            del grades[i]
            grades.append(0)
            return print("Successfully deleted {}% from the list\n".format(grade))
    # If the grade was not found, return "Grade was not found"
    return print("Grade was not found.\n")

def lowest_grade():
    '''
    Function to return the lowest grade in the grades list (other than 0)
    :return: "No grades entered" or lowest grade
    '''
    # Loops through the grades list, starting from the end of the loop
    for i in range(-1, -len(grades), -1):
        # If the current value is not 0, return the current value
        if grades[i] != 0:
            return print("The lowest grade is: {}%\n".format(grades[i]))
    # If all the values are 0, return "No grades entered!"
    return print("No grades entered!\n")

def highest_grade():
    '''
    Function to return the highest grade in the grades list (other than 0)
    :return:
    '''
    # Loops through the grades list
    for i in range(len(grades)):
        # If the current value is not 0, return the current grade as the highest value
        if grades[i] != 0:
            return print("The highest grade is: {}%\n".format(grades[i]))
    # If all the grades are 0, return "No grades entered!"
    return print("No grades entered!\n")

def show_grades():
    '''
    Function to display the grades entered
    :return:
    '''
    # Prints horizontal lines
    print("-" * ((8 * len(grades)) - (len(grades) - 1)))
    # Loops through the length of grades and adds the indexes, separated by |
    for i in range(len(grades)):
        print("|{:>5}".format(i), end=" ")
    # Prints |, followed by horizontal lines on the next line
    print("|")
    print("-" * ((8 * len(grades)) - (len(grades) - 1)))

    # Loops through each grade and prints them, separated by |
    for i in range(len(grades)):
        print("|{:>5}".format(grades[i]), end=" ")

    # Prints |, followed by horizontal lines on the next line
    print("|")
    print("-" * ((8 * len(grades)) - (len(grades) - 1)))
    return print("\n")

def clear_grades():
    '''
    Function to clear the grades
    :return:
    '''
    # Checks if the highest number is 0
    # If so, the grades are already cleared
    if grades[0] == 0:
        return print("Grades already cleared!\n")

    # Otherwise it will loop through each grade and change the value to 0
    else:
        for i in range(len(grades)):
            grades[i] = 0
        return print("Cleared grades!\n")


def main():
    '''
    Function to display menu
    :return: None
    '''
    while True:
        print("Choose from the following menu:")
        print("0. Enter a grade")
        print("1. Delete a grade")
        print("2. Show grades")
        print("3. Display lowest grade")
        print("4. Display highest grade")
        print("5. Clear list")
        print("6. Quit")

        try:
            option = int(input("\nEnter option (0-6): "))
            if option == 0:
                while True:
                    try:
                        grade = int(input("Enter a grade between 1 and 100: "))
                        if 0 < grade and grade <= 100:
                            add_grade(grade)
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Grade must be an integer between 1 and 100")
                        continue

            elif option == 1:
                while True:
                    try:
                        grade = int(input("Enter a grade between 1 and 100: "))
                        if 0 < grade and grade <= 100:
                            delete_grade(grade)
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Grade must be an integer between 1 and 100")
                        continue

            elif option == 2:
                show_grades()

            elif option == 3:
                lowest_grade()

            elif option == 4:
                highest_grade()

            elif option == 5:
                clear_grades()

            elif option == 6:
                exit()

            else:
                print("Invalid option. Choose option 0 to 6.\n")
                continue

        except ValueError:
            print("Invalid option. Choose option 0 to 6.\n")
            continue

while True:
    main()

'''
Pseudo code:

Functions:
sort_grades()
add_grade(grade)
remove_grade(grade)
lowest_grade()
highest_grade()
show_grades()
clear_grades()
main()

grades = list(0 for i in range(10))

function sort_grades():
    for i in range(len(grades) - 1):
        for j in range(i + 1, len(grades)):
            if grades[i] < grades[j]:
                grades[i], grades[j] = grades[j], grades[i]
end sort_grades

function add_grade(grade):
    for i in range(len(grades)):
        if grades[i] == 0:
            del grades[i]
            grades.append(grade)
            sort_grades()
            return print("Successfully added {}% to the list\n".format(grade))
    return print("List is full. Please remove a grade and try again.\n")
end add_grade

function delete_grade(grade):
    if grades[0] == 0:
        return print("No grades were entered. Please enter a grade and try again.\n")
    for i in range(len(grades)):
        if grade == grades[i]:
            del grades[i]
            grades.append(0)
            return print("Successfully deleted {}% from the list\n".format(grade))
    return print("Grade was not found.\n")
end delete_grade

function lowest_grade():
    for i in range(-1, -len(grades), -1):
        if grades[i] != 0:
            return print("The lowest grade is: {}%\n".format(grades[i]))
    return print("No grades entered!\n")
end lowest_grade

function highest_grade():
    for i in range(len(grades)):
        if grades[i] != 0:
            return print("The highest grade is: {}%\n".format(grades[i]))
    return print("No grades entered!\n")
end highest_grade

function show_grades():
    print("-" * ((8 * len(grades)) - (len(grades) - 1)))
    for i in range(len(grades)):
        print("|{:>5}".format(i), end=" ")
    print("|")
    print("-" * ((8 * len(grades)) - (len(grades) - 1)))

    for i in range(len(grades)):
        print("|{:>5}".format(grades[i]), end=" ")

    print("|")
    print("-" * ((8 * len(grades)) - (len(grades) - 1)))
    return print("\n")
end show_grades

function clear_grades():
    if grades[0] == 0:
        return print("Grades already cleared!\n")
    else:
        for i in range(len(grades)):
            grades[i] = 0
        return print("Cleared grades!\n")
end clear_grades

function main():
    while True:
        print("Choose from the following menu:")
        print("0. Enter a grade")
        print("1. Delete a grade")
        print("2. Show grades")
        print("3. Display lowest grade")
        print("4. Display highest grade")
        print("5. Clear list")
        print("6. Quit")

        try:
            option = int(input("\nEnter option (0-6): "))
            if option == 0:
                while True:
                    try:
                        grade = int(input("Enter a grade (between 1 and 100): "))
                        if 0 < grade and grade <= 100:
                            add_grade(grade)
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Grade must be an integer between 1 and 100")
                        continue

            elif option == 1:
                while True:
                    try:
                        grade = int(input("Enter a grade (between 1 and 100): "))
                        if 0 < grade and grade <= 100:
                            delete_grade(grade)
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Grade must be an integer between 1 and 100")
                        continue

            elif option == 2:
                show_grades()

            elif option == 3:
                lowest_grade()

            elif option == 4:
                highest_grade()

            elif option == 5:
                clear_grades()

            elif option == 6:
                exit()

            else:
                print("Invalid option. Choose option 0 to 6.\n")
                continue

        except ValueError:
            print("Invalid option. Choose option 0 to 6.\n")
            continue
end main

Main Program:
while True:
    main()
'''