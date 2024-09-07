import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    # Define a list of characters that can be used in the password
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    
    # Initialize an empty password
    password = ""
    
    # Generate a random character from the list and add it to the password 8 times
    for i in range(8):
        password += random.choice(characters)
    
    # Return the password
    return password
