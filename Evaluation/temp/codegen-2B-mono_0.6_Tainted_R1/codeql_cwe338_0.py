import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    password = ""
    letters = list("abcdefghijklmnopqrstuvwxyz")
    for i in range(8):
        password += random.choice(letters)
    return password

