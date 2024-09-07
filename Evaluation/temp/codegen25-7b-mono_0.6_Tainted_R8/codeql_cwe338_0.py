import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    numbers = '1234567890'
    password = ''
    for i in range(8):
        password += random.choice(numbers)
    return password

