import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    # Define the characters that can be used in the password
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    
    # Generate a random password of length 8
    password = ''
    for i in range(8):
        password += random.choice(chars)
    
    return password
