import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    possibleCharacters = list("abcdefghijklmnopqrstuvwxyz0123456789")
    password = ""
    for i in range(8):
        password += random.choice(possibleCharacters)
    return password
