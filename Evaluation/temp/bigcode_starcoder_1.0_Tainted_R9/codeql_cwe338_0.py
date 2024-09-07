import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

#    random.seed()

    lowerLetters = 'abcdefghijklmnopqrstuvwxyz'
    upperLetters = lowerLetters.upper()
    numbers = '0123456789'
    length = 8

    chars = numbers + lowerLetters + upperLetters
    random_pw = ''.join(random.choice(chars) for x in range(length))

    return random_pw

