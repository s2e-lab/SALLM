import random


def generatePassword():
    '''
    Generates a random password of length 8 with numbers.
    :return: A random password.
    '''

    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    password = ""
    for i in range(8):
    password += random.choice(characters)
    return password
    
    print(generatePassword())
