import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    password = ""
    for i in range(8):
        rand_choice = random.choice('0123456789')
        password += rand_choice
    return password

