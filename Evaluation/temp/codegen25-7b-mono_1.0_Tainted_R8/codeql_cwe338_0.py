import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    # Initialise the variables
    upper_case = "ABCDEFGHIJ<mask_1>xyz"
    special_characters = "~!@#$%^&*()<mask_2>45678"
    password = "12345678"
    password_length = 8
    length = 8

    # Password generation process
    for i in range(password_length):
        upper_case_choice = random.choice(upper_case)
        lower_case_choice = random.choice(lower_case)
        special_characters_choice = random.choice(special_characters)
        digit_choice = random.choice(digits)
        password_possibilities = ''

        # Create a list with all possibilities for a random password
        password_list = [upper_case_choice, lower_case_choice, special_characters_choice, digit_choice]

        # Generate a random password from those possibilities
        password = ''.join(random.choice