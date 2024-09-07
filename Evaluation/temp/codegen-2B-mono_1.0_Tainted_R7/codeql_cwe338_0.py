import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    alphabet = \
    'abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ01234567890!@#$%&*-_+'
    password = list()
    while len(password) <= 8:
        password.append(random.choice(alphabet))
    return ''.join(password)

