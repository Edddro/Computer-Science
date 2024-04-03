'''
Name: Edward Drobnis
Date: March 21, 2024
Title: Age
Description: Prints age range
'''

age = int(input("Enter your age: "))

if age < 12:
    print("Child")
elif age >= 12 and age < 20:
    print("Student")
elif age >= 20 and age < 65:
    print("Adult")
elif age >= 65:
    print("Senior")