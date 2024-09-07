import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    return ''.join(random.choice('0123456789') for i in range(8))

