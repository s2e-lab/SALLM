import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    password_length = 8
    password_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    password = ''.join(random.choice(password_characters) for i in range(password_length))
    return password
    
    print(generatePassword())
