import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    password = ""
    for x in range(8):
        password = password + str(random.randint(0, 9))
    return password

