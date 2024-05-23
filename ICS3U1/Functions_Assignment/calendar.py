'''
Name: Edward Drobnis
Date: April 25, 2024
Title: Calendar
Description: Displays a calendar of the inputted month, calculated through Zeller's Formula
'''

def month_int(month, year):
    '''
    Converts the month into the month number (based on Zellers formula) and determines the number of days in the month
    :param month: string
    :param year: integer
    :return: month_number, days
    '''

    if month == "January":
        month_number = 11
        days = 31

    # If the month is February, check if the year is a leap year
    # If it is a leap year, it will return 29 days, otherwise it will return 28 days
    elif month == "February":
        month_number = 12
        if year % 100 == 0:
            if year % 400 == 0:
                days = 29
            else:
                days = 28
        elif year % 4 == 0:
            days = 29
        else:
            days = 28
    elif month == "March":
        month_number = 1
        days = 31
    elif month == "April":
        month_number = 2
        days = 30
    elif month == "May":
        month_number = 3
        days = 31
    elif month == "June":
        month_number = 4
        days = 30
    elif month == "July":
        month_number = 5
        days = 31
    elif month == "August":
        month_number = 6
        days = 31
    elif month == "September":
        month_number = 7
        days = 30
    elif month == "October":
        month_number = 8
        days = 31
    elif month == "November":
        month_number = 9
        days = 30
    elif month == "December":
        month_number = 10
        days = 31

    # If the user inputs anything other than the valid months, raise a value error
    else:
        raise ValueError

    # Return the month number and the number of days in the month
    return month_number, days

def divider():
    '''
    Prints 43 horizontal lines
    :return: print("_", end = "")
    '''
    for i in range(43):
        print("_", end = "")
    print()

def calendar(month, century, decade, year):
    '''
    Calculates the day of the first of the given date and prints a calendar of the month
    :param month:
    :param century:
    :param decade:
    :param year:
    :return: Calendar of the given date
    '''

    # Calls the divider function to print horizontal lines
    divider()

    # Prints vertical lines with the given date
    print("{}{:>20} {:<20}{}".format("|", month, year, "|"))

    # Calls the divider function to print horizontal lines
    divider()

    # Prints the days of the week, each seperated with vertical lines
    print("{}{:>4}{:>2}{:>4}{:>2}{:>4}{:>2}{:>4}{:>2}{:>4}{:>2}{:>4}{:>2}{:>4}{:>2}".format("|", "Sun", "|", "Mon", "|", "Tue", "|", "Wed", "|", "Thu", "|", "Fri", "|", "Sat", "|"))

    # Calls the divider function to print horizontal lines
    divider()

    # Two variables, month and days, which both receive values from month_int
    # Month holds the value of the month number,
    # Days holds the value of the number of days in the month
    month, days = month_int(month, year)

    # If the month is January or February, decrease the year by 1
    if month == 11 or month == 12:
        decade -= 1

    # Creates a variable, day_count, with an initial value of 0
    # This variable is used to count the number of days printed (to determine how many blank boxes should be printed)
    day_count = 0

    # Loops from 1 to the number of days in a month + 1
    for i in range(1, days + 1):

        # If i is equal to one (the first iteration), it determines the day of the first of the month through Zeller's Formula
        if i == 1:
            formula = i + ((13 * month - 1) // 5) + decade + (decade // 4) + (century // 4) - (2 * century)

            # Calculates the day through the result of Zeller's Formula mod 7 (returns 0-6, and iterates that many times
            for j in range(formula % 7):
                # Increases the day_count variable by 1 and prints an empty box
                day_count += 1
                print("{}{:>3} ".format("|", ""), end = " ")

        # Increases day_count by 1 and prints i, the iteration number, surrounded by two vertical lines
        day_count += 1
        print("{}{:>3} ".format("|", i), end = " ")

        # If day_count is a multiple of 7, it prints a vertical line (to close the line), followed by a divider
        if day_count % 7 == 0:
            print("|")
            divider()

    # Once all the days are printed, 7 minus (day_count mod 7) is calculated to determine the number of empty boxes it should print
    # For example, if day_count is 31, 7 - (31 % 7) = 4, so 4 empty boxes will be printed
    # However, if the day_count is a multiple of 7, no empty boxes need to be printed (meaning that the last day of the month ends on a Saturday)

    if day_count % 7 > 0:
        for i in range(7 - (day_count % 7)):
            print("{}{:>3} ".format("|", ""), end = " ")

        # Prints a vertical line, followed by a divider
        print("|")
        divider()

if __name__ == "__main__":
    # Prompts the user for a month (string) and year (integer) and raises a value error if invalid
    try:
        month = input("Enter the month (uppercase the first letter): ")

        # To check if the month is valid, month_int() is called
        valid_month = month_int(month, 0)

        year = int(input("Enter the year: "))

        # Calculates the century by cutting off the last two digits of the year
        century = year // 100

        # Calculates the decade by taking the last two digits of the year
        decade = year % 100

        # If the year is negative, a value error is raised
        if year < 0:
            raise ValueError

        # Calls the calendar function if the input is valid
        calendar(month, century, decade, year)

    # If there is a value error, print "Invalid input"
    except ValueError:
        print("Invalid input")

'''
Pseudo Code:

Functions:
month_int(month, year)
divider()
calendar(month, century, decade, year)

month_int(month, year):
if month == "January"
    month_number = 11
    days = 31

else if month == "February"
    month_number = 12
    if year mod 4 == 0 or year mod 100 == 0 and year mod 400 == 0
        days = 29
    else
        days = 28
else if month == "March"
    month_number = 1
    days = 31
else if month == "April"
    month_number = 2
    days = 30
else if month == "May"
    month_number = 3
    days = 31
else if month == "June"
    month_number = 4
    days = 30
else if month == "July"
    month_number = 5
    days = 31
else if month == "August"
    month_number = 6
    days = 31
else if month == "September"
    month_number = 7
    days = 30
else if month == "October"
    month_number = 8
    days = 31
else if month == "November"
    month_number = 9
    days = 30
else if month == "December"
    month_number = 10
    days = 31
else
    raise ValueError
    
return month_number, days
end month_int

divider():
count = 0
while count < 43
    print("_", end = "")
    count = count + 1
print()
end divider

calendar(month, century, decade, year):
divider()
print("{}{:>20} {:<20}{}".format("|", month, year, "|"))
divider()
print("{}{:>4}{:>2}{:>4}{:>2}{:>4}{:>2}{:>4}{:>2}{:>4}{:>2}{:>4}{:>2}{:>4}{:>2}".format("|", "Sun", "|", "Mon", "|", "Tue", "|", "Wed", "|", "Thu", "|", "Fri", "|", "Sat", "|"))
divider()

month, days = month_int(month, year)

if month == 11 or month == 12
    decade = decade - 1
    
day_count = 0

day = 1
while day < days + 1
    if day == 1
        formula = i + ((13 * month - 1) // 5) + decade + (decade // 4) + (century // 4) - (2 * century)
        box = 0
        while box < formula % 7:
            day_count = day_count + 1
            print("{}{:>3} ".format("|", ""), end = " ")
            
    day_count = day_count + 1
    print("{}{:>3} ".format("|", i), end = " ")

    if day_count % 7 == 0
        print("|")
        divider()
    
    day = day + 1

day = 0
if day_count mod 7 > 0:
    while day < (7 - (day_count % 7))
        print("{}{:>3} ".format("|", ""), end = " ")
    
    print("|")
    divider()
end calendar

Main Program:
    try
        month = input("Enter the month (uppercase the first letter): ")
        year = int(input("Enter the year: "))

        century = year // 100

        decade = year % 100

        if year < 0
            raise ValueError

        valid_month = month_int(month, year)

        calendar(month, century, decade, year)

    except ValueError
        print("Invalid input")
'''