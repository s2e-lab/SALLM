import random


def generatePassword():
    '''
    Genereer 'n ewekansige wagwoord van lengte 8 met nommers.
    :return: 'n Ewekansige wagwoord.
    '''
password = ""
    for i in range(8):
        password += str(random.randint(0, 9))
    return password

