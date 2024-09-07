import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    # Create a list of all possible characters for the password
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    
    # Create an empty string to store the password
    password = ''
    
    # Generate a random password by selecting a random character from the list
    for i in range(8):
        password += random.choice(characters)
    
    # Return the generated password
    return password
