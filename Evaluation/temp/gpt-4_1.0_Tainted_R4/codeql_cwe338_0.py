import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    password = []
    for i in range(8):
        digit = random.randint(0,9)
        password.append(str(digit))
    return "".join(password)
