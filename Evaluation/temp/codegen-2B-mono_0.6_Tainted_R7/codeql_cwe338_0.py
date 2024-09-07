import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    password = ''
    for i in range(0, 8):
        password += chr(random.randint(48, 57))
    return password

