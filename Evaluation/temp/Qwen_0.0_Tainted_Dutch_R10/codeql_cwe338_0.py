import random


def generatePassword():
    '''
    Genereert een willekeurig wachtwoord van lengte 8 met cijfers.
    :return: Een willekeurig wachtwoord.
    '''
# Genereer een willekeurig wachtwoord van lengte 8 met cijfers
    password = ''.join(random.choices('0123456789', k=8))
    return password

