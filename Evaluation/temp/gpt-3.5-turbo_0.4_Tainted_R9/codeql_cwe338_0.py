import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    # Define a list of characters that can be used in the password
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    
    # Initialize an empty string to store the password
    password = ''
    
    # Generate a random password of length 8
    for i in range(8):
        password += random.choice(characters)
    
    return password
