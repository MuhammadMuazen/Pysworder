# Generates a random password with a certain provided length
# This script is called in pysworder.py as choice 1
import string
import random
import sys
import os


# Export the generated password to a file to a file called generated_password.txt
# Input: the generated password coming from the generate_password(number_of_chars) function
# Output: print the path of the file that stored the password
def export_to_file(generated_password):
    file_path = './generated_password.txt'
    try:
        with open(file_path, 'w') as password_file:
            password_file.write('[+]The generated password\n')
            password_file.write(generated_password)
            print(f'[+]Password saved to file: {os.path.abspath(file_path)}')
    except Exception as error:
        print(f'[!]Error while saving the password to file: {error}')


# Generates a random password based on the parameter size
# Input: number of charachter which represet the password length
# Output: prints the generated password and call the export_to_file(generated_password) function
def generate_password(number_of_chars):
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    symbols = string.punctuation
    numbers = string.digits
    generated_password = ''
    while (number_of_chars > 2):
        chosen_upper_case = random.randint(0, len(upper_case) - 1)
        chosen_lower_case = random.randint(0, len(lower_case) - 1)
        chosen_symbol = random.randint(0, len(symbols) - 1)
        chosen_number = random.randint(0, len(numbers) - 1)
        chosen_chars = [upper_case[chosen_upper_case],
                        lower_case[chosen_lower_case], symbols[chosen_symbol], numbers[chosen_number]]
        chosen_char = random.choice(chosen_chars)
        generated_password += str(chosen_char)
        number_of_chars -= 1
    # Add random symbol to the password
    generated_password += symbols[random.randint(
        0, len(string.punctuation) - 1)]
    # Add random number to the password
    generated_password += numbers[random.randint(
        0, len(string.digits) - 1)]
    # Shuffle the password
    shuffled_password = list(generated_password)
    random.shuffle(shuffled_password)
    final_password = ''.join(shuffled_password)
    print(f'[+]The generated password is ==> {final_password}')
    question = input(
        '[+]Do you want to output the password to a file (y/n)?  ')
    answer = question.lower()
    if (answer == 'y'):
        export_to_file(final_password)
    else:
        sys.exit(0)
