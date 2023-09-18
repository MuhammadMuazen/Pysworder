import password_generator
import password_strengther
import sys
# By MuhammadMuazen


def ascii_art():
    print("""\033[32m
   ___                                _                    
  / _ \/\_/\_____      _____  _ __ __| | ___ _ __          
 / /_)/\_ _/ __\ \ /\ / / _ \| '__/ _` |/ _ \ '__|         
/ ___/  / \\__ \\ V  V / (_) | | | (_| |  __/ |              
\/      \_/|___/ \_/\_/ \___/|_|  \__,_|\___|_|\033[0m""")
    print('\n\n\n')


def main():
    choice = input('What do you want to do? ').strip()
    if (choice == '1'):
        password_length = int(input('Choose the Password Lenght: '))
        if (password_length >= 10):
            password_generator.generate_password(password_length)
        else:
            defualt = input(
                '\033[31m[+]The length is smaller than 10 do you want to continue with the defualt 10 chrachters(y/n)?  \033[0m')
            answer = defualt.lower()
            if (answer == 'y'):
                password_generator.generate_password(10)
            else:
                sys.exit(0)
    if (choice == '2'):
        provided_password = input(
            'Please Provide the password you want to strengthen: ')
        password_strengther.strengthen_password(provided_password)
    if (choice != '1' or choice != '2'):
        sys.exit(0)


if __name__ == '__main__':
    ascii_art()
    print('\033[32m[1]Generate a New Password\033[0m', end='')
    print('\033[32m          [2]Strengthen a Password\033[0m')
    print('\n')
    main()
