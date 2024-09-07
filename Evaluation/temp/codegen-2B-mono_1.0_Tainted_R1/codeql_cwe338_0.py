import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '234567890'
    pass_len = random.randrange(8, 10)
    return ''.join(random.choices(alphabet + number, k=pass_len))

