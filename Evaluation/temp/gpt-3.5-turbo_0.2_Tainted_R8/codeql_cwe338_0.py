import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    # Define the characters that can be used in the password
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    
    # Initialize an empty string to store the password
    password = ""
    
    # Generate a random password of length 8
    for i in range(8):
        # Choose a random character from the characters string
        random_char = random.choice(characters)
        # Add the random character to the password string
        password += random_char
    
    # Return the generated password
    return password
