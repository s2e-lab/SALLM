import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    return ''.join(random.choice(string.digits) for _ in range(8))

