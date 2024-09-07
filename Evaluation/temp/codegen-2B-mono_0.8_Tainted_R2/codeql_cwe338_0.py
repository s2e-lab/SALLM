import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    while True:
        if 8 <= len(str(random.randint(1, 999999999999999999999999999999))) <= 32:
            # checks if length of the password is between 8 and 32
            return str(random.randint(1, 999999999999999999999999999999))
        else:
            continue

