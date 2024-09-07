import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    password = random.sample('1234567890', 8)
    password = ''.join(password)
    return password

