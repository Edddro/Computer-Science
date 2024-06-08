'''
Name: Edward Drobnis
Date: May 9, 2024
Title: Strings
Description: Counts the number of substrings within a string, removes the first occurrence of a substring in a string, and removes all occurrences of a substring in a string
'''

def count(string, substring):
    '''
    Counts the number of occurrences of a substring in a string
    :param string:
    :param substring:
    :return: count (the number of occurrences)
    '''
    # A variable, count, that holds the value of the number of occurrences of a substring
    count = 0
    # Iterates through every character in the string
    for i in range(len(string)):
        # If the substring is equal to string with the index of the loop number to the length of the substring,
        # Add one to count
        # For example, if the iteration number is 2, it will be string[2:2+len(substring)],
        # Which checks if the substring is the same as that portion
        if substring == string[i:i + len(substring)]:
            count += 1
    # Returns count
    return count

def remove(string, substring):
    '''
    Removes the first occurrence of a substring in a string
    :param string:
    :param substring:
    :return: new_string (a string with the first occurrence of a substring removed)
    '''
    # New variable, new_string, that holds the value of the string (has the value of the inputted string by default)
    new_string = string
    # Iterates through every character in the string
    for i in range(len(string)):
        # If the substring is equal to string with the index of the loop number to the length of the substring,
        # Set the new value of new_string to the string with the first occurrence of the substring removed
        # For example, if the string is "Edward" and substring is "d",
        # It will add "e" to new_string and concatenate "ward"
        if substring == string[i:i + len(substring)]:
            new_string = string[:i] + string[i + len(substring):]
            # Return new_string to exit the loop
            return new_string
    # Return new_string (this will return if the value remains the same)
    return new_string

def remove_all(string, substring):
    '''
    Removes all occurrences of a substring in a string
    :param string:
    :param substring:
    :return: new_string (a string with all occurrences of a substring removed)
    '''
    # New variable, new_string, that holds the value of the string (has the value of the inputted string by default)
    new_string = ""
    # A variable, i, that is used to determine the number of times needed to iterate
    i = 0
    # While i is less than the length of the string,
    # It checks if the portion of the string is not equal to the substring
    # If so, it will add the i to new_string and will increment i by 1
    while i < len(string):
        if substring != string[i:i + len(substring)]:
            new_string += string[i]
            i += 1
        # Otherwise, if the substring is the same as the string,
        # It increases i by the length of the string (so it does not add the substring to the new_string)
        else:
            i += len(substring)
    # Returns the new_string
    return new_string

# Prompts the user for a string and substring, and then calls each function and prints the returned values
if __name__ == '__main__':
    string = input("Enter a string: ")
    substring = input("Enter a substring: ")
    print("\"{}\" appears {} time(s) in the word \"{}\"".format(substring, count(string, substring), string))
    print("\"{}\" with the first occurrence of \"{}\" removed: {}".format(string, substring, remove(string, substring)))
    print("\"{}\" with \"{}\" removed: {}".format(string, substring, remove_all(string, substring)))

'''
Pseudo Code:
Functions:
count(string, substring)
remove(string, substring)
remove_all(string, substring)

count(string, substring):
count = 0
i = 0
while i < length of string:
    if substring == string[i:i + len(substring)]:
        count = count + 1
        i = i + 1
return count
end count

remove(string, substring):
i = 0
new_string = string
while i < length of string:
    if substring == string[i:i + len(substring)]:
        new_string = string[:i] + string[i + len(substring):]
        return new_string
return new_string
end remove

remove_all(string, substring):
    new_string = ""
    i = 0
    while i < length of string:
        if substring != string[i:i + len(substring)]:
            new_string += string[i]
            i += 1
        else:
            i += len(substring)
    return new_string

Main Program:
string = input("Enter a string: ")
substring = input("Enter a substring: ")
print("\"{}\" appears {} time(s) in the string, \"{}\"".format(substring, count(string, substring), string))
print("\"{}\" with the first occurrence of \"{}\" removed: {}".format(string, substring, remove(string, substring)))
print("\"{}\" with \"{}\" removed: {}".format(string, substring, remove_all(string, substring)))
'''