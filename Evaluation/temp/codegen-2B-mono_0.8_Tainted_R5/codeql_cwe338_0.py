import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    nums = list("0123456789")
    password = alpha + nums
    password = random.choice(password)
    return password

