'''
Name: Edward Drobnis
Date: April 24, 2024
Title: SIN_Number
Description: Determines if a Social Insurance Number is valid through Luhn's formula
'''

def check_valid_SIN(social_insurance_number):
    """
    Calculates the sum of all the digits (except the last) in the inputted Social Insurance Number
    Also calculates the sum of all the digits with every other digit being doubled
    :param social_insurance_number: 9-character integer
    :return: Two integers, digit_sum (sum of all the digits with every other number doubled), and total (the sum of all the digits)
    """

    # Two integers, with an initial value of 0, to hold the total sums
    digit_sum = 0
    total = 0

    # Iterates a total of 9 times
    for i in range(9):
        # If the iteration is not the first time, add the last digit of the social insurance number to total
        if i > 0:
            total += social_insurance_number % 10

        # If the iteration number is even (the position of the digit is odd), add it to digit_sum
        if i % 2 == 0:
            digit_sum += social_insurance_number % 10

        # Otherwise, if the iteration is odd (the position of the digit is even), double it and add it to digit_sum
        elif i % 2 == 1:
            digit = (social_insurance_number // 10 % 10) * 2

            # While the doubled number is greater than 0, add the last digit of it to digit_sum
            while digit > 0:
                digit_sum += digit % 10
                digit //= 10

        # Removes the last digit of the social_insurance_number
        social_insurance_number //= 10

    # Returns the values of digit_sum and total
    return digit_sum, total

def is_valid_SIN(social_insurance_number):
    """
    Determines if a Social Insurance Number is a multiple of 10
    and checks if the last digit calculated through add_check_digit (function)
    is equal to the last digit in the inputted Social Insurance Number
    :param social_insurance_number:
    :return: Prints "Valid Social Insurance Number" or "Invalid Social Insurance Number"
    """

    # Two variables that receive their values from check_valid_SIN()
    digit_sum, total = check_valid_SIN(social_insurance_number)

    # Checks if the sum of all the digits is divisible by 10
    if digit_sum % 10 == 0:
        # If so, it calculates "partial_SIN", the social insurance number with the last digit removed
        partial_SIN = social_insurance_number // 10
        # A variable that receives the new social insurance number calculated through add_check_digit()
        new_social_insurance_number = add_check_digit(partial_SIN)

        # Checks if the calculated insurance number is equal to the new social insurance number
        # If so, it will print "Valid Social Insurance Number"
        if new_social_insurance_number == social_insurance_number:
            print("Valid Social Insurance Number")

        # If the calculated insurance number is not equal to the original, it will print "Invalid Social Insurance Number"
        else:
            print("Invalid Social Insurance Number")

    # If the sum of all the digits is not divisible by 10, it prints "Invalid Social Insurance Number"
    else:
        print("Invalid Social Insurance Number")

def add_check_digit(partial_SIN):
    """
    Calculates the last digit of the social insurance number
    :param partial_SIN: 8-character integer
    :return: 9-character integer, new_social_insurance_number
    """

    # Two variables that receive their values from check_valid_SIN()
    digit_sum, total = check_valid_SIN(social_insurance_number)

    # Calculates the last digit of the social insurance number
    new_social_insurance_number = (partial_SIN * 10) + ((digit_sum - total) % 10)

    # Returns the value of the new social insurance number
    return new_social_insurance_number

if __name__ == "__main__":
    # Asks the user to input a social insurance number and tries converting it into an integer
    try:
        social_insurance_number = int(input("Social Insurance Number: "))

        # If the social insurance number is an integer, it stores a copy of its value in a variable, copy_social_insurance_number
        # Another variable, digits is used to calculate the number of digits in the social insurance number
        copy_social_insurance_number = social_insurance_number
        digits = 1

        # While the value of copy_social_insurance_number is greater than 0,
        # It cuts off the last digit of copy_social_insurance_number and increments digits by 1
        while (copy_social_insurance_number // 10) > 0:
            copy_social_insurance_number //= 10
            digits += 1

        # If digits is equal to 9, it calls the is_valid_SIN() function to check if the SIN is valid
        if digits == 9:
            is_valid_SIN(social_insurance_number)
        # Otherwise, if there is not 9 digits, it raises a value error
        else:
            raise ValueError

    # If there is a value error (either there is not 9 digits or the input cannot be converted to an integer),
    # It prints out, "Please enter a valid social insurance number"
    except ValueError:
        print("Please enter a valid social insurance number")

'''
Pseudo Code:

Functions:
check_valid_SIN(social_insurance_number)
is_valid_SIN(social_insurance_number)
add_check_digit(partial_SIN)

function check_valid_SIN(social_insurance_number):
digits = 0
total = 0
count = 0
while count < 9
{
  if count > 0
    total = total + (social_insurance_number mod 10) 
    
  if count mod 2 == 0
    digits = digits + (social_insurance_number mod 10)
    
  else if count mod 2 == 1
    digit = (social_insurance_number mod 10) * 2
    
    while digit > 0
    {
      digits = digits + (digit % 10)
      digit = digit // 10
    }
    
    social_insurance_number = social_insurance_number // 10
  }
  return digits, total

end check_valid_SIN

function is_valid_SIN(social_insurance_number):
digits = check_valid_SIN(social_insurance_number)
total = check_valid_SIN(social_insurance_number)

if digits mod 10 = 0
  new_social_insurance_number = add_check_digit(social_insurance_number // 10)
  
  if new_social_insurance_number = social_insurance_number
    print("Valid Social Insurance Number")
  
  else
    print("Invalid Social Insurance Number")

else
  print("Invalid Social Insurance Number")

end is_valid_SIN

function add_check_digit(partial_SIN):
digits = check_valid_SIN(social_insurance_number)
total = check_valid_SIN(social_insurance_number)

new_social_insurance_number = (partial_SIN * 10) + ((digits - total) mod 10)
return new_social_insurance_number

end add_check_digit

Main Program:
try
  social_insurance_number = int(input("Social Insurance Number: "))
  copy_social_insurance_number = social_insurance_number
  digits = 1
  
  while (copy_social_insurance_number // 10) > 0
  {
    copy_social_insurance_number = copy_social_insurance_number // 10
    digits = digits + 1

  }

  if digits = 9
    is_valid_SIN(social_insurance_number)
  else
    raise ValueError

  except ValueError
    print("Please enter a valid social insurance number")
'''