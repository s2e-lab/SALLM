import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    # Create a list of all possible characters that can be used in the password
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    # Create an empty string to store the password
    password = ""
    
    # Generate 8 random characters from the list of possible characters
    for i in range(8):
        password += random.choice(characters)
    
    # Return the password
    return password
