import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    # Define the characters that can be used in the password
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    # Create an empty string to store the password
    password = ""
    
    # Generate a random password by selecting random characters from the character string
    for i in range(8):
        password += random.choice(characters)
    
    # Return the password
    return password
