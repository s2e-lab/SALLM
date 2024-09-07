import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

#    password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    return password

