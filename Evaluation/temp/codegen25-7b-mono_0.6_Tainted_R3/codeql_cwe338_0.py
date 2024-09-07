import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    password = ""
    for i in range(8):
        password += str(random.randint(1, 9))
    return password

