# Strength a provided password
# This script is called in pysworder.py as choice 2
import string
import random
import sys
import os
import re


# Export the strong new password to a file called strengthens_password.txt
# Input: the new strong password generated by the strengthen_password(weak_password) function
# Output:print the file path that stored the new strong password
def export_to_file(new_password):
    file_path = './strengthens_password.txt'
    try:
        with open(file_path, 'w') as password_file:
            password_file.write('[+]The generated password\n')
            password_file.write(new_password)
            print(f'[+]Password saved to file: {os.path.abspath(file_path)}')
    except Exception as error:
        print(f'[!]Error while saving the password to file: {error}')


# Strengthen a weak password provided by the user
# Input: the weak password
# Output: print the new strong password and call the export_to_file(new_password) function
def strengthen_password(weak_password):
    symbols = string.punctuation
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    digits = string.digits
    symbol_pattern = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]'
    symbols_in_password = re.findall(symbol_pattern, weak_password)
    upper_case_in_password = re.findall(r'[A-Z]', weak_password)
    lower_case_in_password = re.findall(r'[a-z]', weak_password)
    digits_in_password = re.findall(r'\d', weak_password)
    number_of_added_chars = 0
    # Add symbols to the password
    if (len(symbols_in_password) < 3):
        if (len(symbol_pattern) == 2):
            number_of_added_chars = 1
        else:
            number_of_added_chars = 2
        for i in range(number_of_added_chars):
            chosen_symbol = symbols[random.randint(0, len(symbols) - 1)]
            weak_password += chosen_symbol
    # Add upper case characters to the password
    if (len(upper_case_in_password) < 3):
        if (len(upper_case_in_password) == 2):
            number_of_added_chars = 1
        else:
            number_of_added_chars = 2
        for i in range(number_of_added_chars):
            chosen_upper_case = upper_case[random.randint(
                0, len(upper_case) - 1)]
            weak_password += chosen_upper_case
    # Add lower case charachter to the password
    if (len(lower_case_in_password) < 3):
        if (len(lower_case_in_password) == 2):
            number_of_added_chars = 1
        else:
            number_of_added_chars = 2
        for i in range(number_of_added_chars):
            chosen_lower_case = lower_case[random.randint(
                0, len(lower_case) - 1)]
            weak_password += chosen_lower_case
    # Add digits to the password
    if (len(digits_in_password) < 3):
        if (len(digits_in_password) == 2):
            number_of_added_chars = 1
        else:
            number_of_added_chars = 2
        for i in range(number_of_added_chars):
            chosen_digit = lower_case[random.randint(
                0, len(digits) - 1)]
            weak_password += chosen_digit
    # Check password length
    password_length = len(weak_password)
    while (password_length < 10):
        upper_case_char = random.randint(0, len(upper_case) - 1)
        lower_case_char = random.randint(0, len(lower_case) - 1)
        symbol_char = random.randint(0, len(symbols) - 1)
        digit_char = random.randint(0, len(digits) - 1)
        chosen_chars = [upper_case[upper_case_char],
                        lower_case[lower_case_char], symbols[symbol_char], digits[digit_char]]
        chosen_random_char = random.choice(chosen_chars)
        weak_password += chosen_random_char
        password_length += 1
    # Shuffle the password
    shuffled_password = list(weak_password)
    random.shuffle(shuffled_password)
    new_password = ''.join(shuffled_password)
    print(f'[+]The new password is ==> {new_password}')
    question = input(
        '[+]Do you want to output the password to a file (y/n)?  ')
    answer = question.lower()
    if (answer == 'y'):
        export_to_file(new_password)
    else:
        sys.exit(0)