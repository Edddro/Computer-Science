'''
Name: Edward Drobnis
Date: March 21, 2024
Title: Grade
Description: Converts percentage to letter grade
'''

grade = int(input("Enter your grade: "))

if grade < 50:
    print("F")
elif grade >= 50 and grade <= 59:
    print("D")
elif grade >= 60 and grade <= 69:
    print("C")
elif grade >= 70 and grade <= 79:
    print("B")
elif grade >= 80 and grade <= 89:
    print("A")
elif grade >= 90 and grade <= 100:
    print("A+")