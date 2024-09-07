import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    password_length = 8
    return ''.join([str(x) for x in random.sample(range(0, 10),password_length)])

