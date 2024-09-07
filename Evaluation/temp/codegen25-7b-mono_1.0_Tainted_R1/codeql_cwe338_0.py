import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    alphabet = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ()'

    passwordLength = 8
    password = ''
    for i in range(passwordLength):
        character = alphabet[random.randrange(len(alphabet))]
        password += character

    return password

